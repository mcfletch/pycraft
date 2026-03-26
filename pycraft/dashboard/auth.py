"""Authentication for the Pycraft Dashboard.

Provides password hashing, credential storage, HMAC-signed session cookies,
and aiohttp middleware for protecting API routes.

Session cookies are signed with a secret key stored in the credentials file,
so sessions survive server restarts (default expiry: 7 days).
"""

import getpass
import hashlib
import hmac
import json
import logging
import os
import secrets
import pathlib
import time

from aiohttp import web

log = logging.getLogger(__name__)

DEFAULT_CREDENTIALS_FILE = pathlib.Path.home() / '.pycraft-dashboard-users.json'

SESSION_MAX_AGE = 86400 * 7  # 7 days in seconds


def _hash_password(password, salt=None):
    """Hash a password with PBKDF2-HMAC-SHA256.

    Returns (hash_hex, salt_hex).
    """
    if salt is None:
        salt = os.urandom(32)
    else:
        salt = bytes.fromhex(salt)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations=600_000)
    return dk.hex(), salt.hex()


def _credentials_path(path=None):
    return pathlib.Path(path) if path else DEFAULT_CREDENTIALS_FILE


def load_credentials(path=None):
    """Load the credentials file. Returns the full structure including users and secret."""
    p = _credentials_path(path)
    if not p.exists():
        return {}
    with open(p, 'r') as f:
        return json.load(f)


def save_credentials(credentials, path=None):
    """Save credentials to disk."""
    p = _credentials_path(path)
    with open(p, 'w') as f:
        json.dump(credentials, f, indent=2)
    os.chmod(p, 0o600)


def _get_or_create_secret(credentials_file=None):
    """Get the signing secret from the credentials file, creating one if needed."""
    creds = load_credentials(credentials_file)
    if '_secret' not in creds:
        creds['_secret'] = secrets.token_hex(32)
        save_credentials(creds, credentials_file)
    return creds['_secret']


def _get_users(credentials_file=None):
    """Get just the user entries (excluding internal keys like _secret)."""
    creds = load_credentials(credentials_file)
    return {k: v for k, v in creds.items() if not k.startswith('_')}


def add_user(username, password, credentials_file=None):
    """Add or update a user's credentials."""
    creds = load_credentials(credentials_file)
    pw_hash, salt = _hash_password(password)
    creds[username] = {'hash': pw_hash, 'salt': salt}
    # Ensure signing secret exists
    if '_secret' not in creds:
        creds['_secret'] = secrets.token_hex(32)
    save_credentials(creds, credentials_file)
    return True


def verify_password(username, password, credentials_file=None):
    """Verify a username/password against stored credentials."""
    users = _get_users(credentials_file)
    if username not in users:
        return False
    entry = users[username]
    pw_hash, _ = _hash_password(password, salt=entry['salt'])
    return secrets.compare_digest(pw_hash, entry['hash'])


def create_session_token(username, credentials_file=None):
    """Create an HMAC-signed session token encoding username and expiry."""
    secret = _get_or_create_secret(credentials_file)
    expires = int(time.time()) + SESSION_MAX_AGE
    payload = f'{username}:{expires}'
    sig = hmac.new(secret.encode(), payload.encode(), 'sha256').hexdigest()
    return f'{payload}:{sig}'


def verify_session_token(token, credentials_file=None):
    """Verify an HMAC-signed session token. Returns username or None."""
    if not token:
        return None
    parts = token.split(':')
    if len(parts) != 3:
        return None
    username, expires_str, sig = parts
    try:
        expires = int(expires_str)
    except ValueError:
        return None
    if time.time() > expires:
        return None
    secret = _get_or_create_secret(credentials_file)
    payload = f'{username}:{expires_str}'
    expected = hmac.new(secret.encode(), payload.encode(), 'sha256').hexdigest()
    if not hmac.compare_digest(sig, expected):
        return None
    # Verify user still exists
    if username not in _get_users(credentials_file):
        return None
    return username


def auth_required(credentials_file=None):
    """Return True if authentication is required (i.e. users have been configured)."""
    return len(_get_users(credentials_file)) > 0


@web.middleware
async def auth_middleware(request, handler):
    """Middleware that enforces authentication on /api/* routes.

    Fails closed: all /api/* routes require authentication unless the
    path is /api/auth/* (login/logout/status endpoints).
    Non-API paths (static files, SPA) are allowed so the login page can load.
    """
    path = request.path

    # Allow non-API paths (static files, SPA fallback)
    if not path.startswith('/api/'):
        return await handler(request)

    # Allow auth endpoints
    if path.startswith('/api/auth/'):
        return await handler(request)

    # Check session cookie
    credentials_file = request.app.get('credentials_file')
    token = request.cookies.get('pycraft_session')
    if token and verify_session_token(token, credentials_file):
        return await handler(request)

    return web.json_response({'error': 'Authentication required'}, status=401)


async def login_handler(request):
    """POST /api/auth/login — authenticate and set session cookie."""
    credentials_file = request.app.get('credentials_file')
    try:
        body = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid request body'}, status=400)

    username = body.get('username', '')
    password = body.get('password', '')

    if not username or not password:
        return web.json_response({'error': 'Username and password required'}, status=400)

    if verify_password(username, password, credentials_file):
        token = create_session_token(username, credentials_file)
        response = web.json_response({'ok': True, 'username': username})
        response.set_cookie(
            'pycraft_session',
            token,
            httponly=True,
            samesite='Lax',
            max_age=SESSION_MAX_AGE,
        )
        return response

    return web.json_response({'error': 'Invalid username or password'}, status=401)


async def logout_handler(request):
    """POST /api/auth/logout — clear session cookie."""
    response = web.json_response({'ok': True})
    response.del_cookie('pycraft_session')
    return response


async def status_handler(request):
    """GET /api/auth/status — check authentication state."""
    credentials_file = request.app.get('credentials_file')
    token = request.cookies.get('pycraft_session')
    username = verify_session_token(token, credentials_file)

    return web.json_response({
        'authenticated': username is not None,
        'auth_required': True,
        'username': username,
    })


def add_user_interactive(credentials_file=None):
    """Interactive CLI flow to add a user. Returns True on success."""
    username = input('Username: ').strip()
    if not username:
        print('Username cannot be empty.')
        return False
    password = getpass.getpass('Password: ')
    if not password:
        print('Password cannot be empty.')
        return False
    confirm = getpass.getpass('Confirm password: ')
    if password != confirm:
        print('Passwords do not match.')
        return False
    add_user(username, password, credentials_file)
    path = pathlib.Path(credentials_file) if credentials_file else DEFAULT_CREDENTIALS_FILE
    print(f'User "{username}" added. Credentials saved to {path}')
    return True
