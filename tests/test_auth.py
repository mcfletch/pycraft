"""Tests for the dashboard authentication module"""

import json
import os
import time
from unittest import mock

import pytest

from pycraft.dashboard.auth import (
    _hash_password,
    add_user,
    verify_password,
    load_credentials,
    save_credentials,
    create_session_token,
    verify_session_token,
    auth_required,
    SESSION_MAX_AGE,
)


@pytest.fixture
def creds_file(tmp_path):
    return str(tmp_path / 'test-creds.json')


class TestPasswordHashing:
    def test_hash_produces_different_output_from_input(self):
        pw_hash, salt = _hash_password('testpass')
        assert pw_hash != 'testpass'
        assert len(salt) == 64  # 32 bytes hex

    def test_same_salt_produces_same_hash(self):
        pw_hash1, salt = _hash_password('testpass')
        pw_hash2, _ = _hash_password('testpass', salt=salt)
        assert pw_hash1 == pw_hash2

    def test_different_passwords_produce_different_hashes(self):
        pw_hash1, salt = _hash_password('password1')
        pw_hash2, _ = _hash_password('password2', salt=salt)
        assert pw_hash1 != pw_hash2


class TestCredentialStorage:
    def test_load_nonexistent_file_returns_empty(self, creds_file):
        assert load_credentials(creds_file) == {}

    def test_add_and_load_user(self, creds_file):
        add_user('alice', 'secret123', creds_file)
        creds = load_credentials(creds_file)
        assert 'alice' in creds
        assert 'hash' in creds['alice']
        assert 'salt' in creds['alice']

    def test_add_user_creates_signing_secret(self, creds_file):
        add_user('alice', 'secret123', creds_file)
        creds = load_credentials(creds_file)
        assert '_secret' in creds
        assert len(creds['_secret']) == 64  # 32 bytes hex

    def test_file_permissions_restricted(self, creds_file):
        add_user('alice', 'secret123', creds_file)
        mode = os.stat(creds_file).st_mode & 0o777
        assert mode == 0o600

    def test_add_multiple_users(self, creds_file):
        add_user('alice', 'pass1', creds_file)
        add_user('bob', 'pass2', creds_file)
        creds = load_credentials(creds_file)
        assert 'alice' in creds
        assert 'bob' in creds

    def test_update_existing_user(self, creds_file):
        add_user('alice', 'oldpass', creds_file)
        old_hash = load_credentials(creds_file)['alice']['hash']
        add_user('alice', 'newpass', creds_file)
        new_hash = load_credentials(creds_file)['alice']['hash']
        assert old_hash != new_hash

    def test_signing_secret_preserved_across_updates(self, creds_file):
        add_user('alice', 'pass1', creds_file)
        secret1 = load_credentials(creds_file)['_secret']
        add_user('bob', 'pass2', creds_file)
        secret2 = load_credentials(creds_file)['_secret']
        assert secret1 == secret2


class TestPasswordVerification:
    def test_correct_password(self, creds_file):
        add_user('alice', 'correct-horse', creds_file)
        assert verify_password('alice', 'correct-horse', creds_file) is True

    def test_wrong_password(self, creds_file):
        add_user('alice', 'correct-horse', creds_file)
        assert verify_password('alice', 'wrong-horse', creds_file) is False

    def test_nonexistent_user(self, creds_file):
        assert verify_password('nobody', 'anything', creds_file) is False


class TestSessionTokens:
    def test_create_and_verify_token(self, creds_file):
        add_user('alice', 'pass', creds_file)
        token = create_session_token('alice', creds_file)
        assert verify_session_token(token, creds_file) == 'alice'

    def test_invalid_token_returns_none(self, creds_file):
        add_user('alice', 'pass', creds_file)
        assert verify_session_token('garbage', creds_file) is None

    def test_empty_token_returns_none(self, creds_file):
        assert verify_session_token('', creds_file) is None

    def test_none_token_returns_none(self, creds_file):
        assert verify_session_token(None, creds_file) is None

    def test_tampered_username_rejected(self, creds_file):
        add_user('alice', 'pass', creds_file)
        add_user('bob', 'pass', creds_file)
        token = create_session_token('alice', creds_file)
        # Replace alice with bob in the token
        tampered = token.replace('alice:', 'bob:', 1)
        assert verify_session_token(tampered, creds_file) is None

    def test_expired_token_rejected(self, creds_file):
        add_user('alice', 'pass', creds_file)
        token = create_session_token('alice', creds_file)
        # Fast-forward past expiry
        with mock.patch('pycraft.dashboard.auth.time') as mock_time:
            mock_time.time.return_value = time.time() + SESSION_MAX_AGE + 1
            assert verify_session_token(token, creds_file) is None

    def test_token_survives_simulated_restart(self, creds_file):
        """Token created before 'restart' is still valid after (key is on disk)."""
        add_user('alice', 'pass', creds_file)
        token = create_session_token('alice', creds_file)
        # Verify with a fresh call (simulates new process reading from disk)
        assert verify_session_token(token, creds_file) == 'alice'

    def test_deleted_user_token_rejected(self, creds_file):
        add_user('alice', 'pass', creds_file)
        token = create_session_token('alice', creds_file)
        # Remove user from credentials
        creds = load_credentials(creds_file)
        del creds['alice']
        save_credentials(creds, creds_file)
        assert verify_session_token(token, creds_file) is None


class TestAuthRequired:
    def test_no_users_means_not_required(self, creds_file):
        assert auth_required(creds_file) is False

    def test_with_users_means_required(self, creds_file):
        add_user('alice', 'pass', creds_file)
        assert auth_required(creds_file) is True

    def test_secret_key_alone_not_counted_as_user(self, creds_file):
        """_secret is internal metadata, not a user."""
        save_credentials({'_secret': 'abc123'}, creds_file)
        assert auth_required(creds_file) is False
