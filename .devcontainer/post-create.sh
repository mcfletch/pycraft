#!/usr/bin/env bash
set -euo pipefail

echo "==> Creating Python 3.14 virtualenv..."
python3.14 -m venv .venv

echo "==> Installing Python requirements..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "==> Installing pycraft in editable mode with all dependency groups..."
.venv/bin/pip install -e ".[all]"

echo "==> Installing frontend dependencies..."
cd pycraft/dashboard/frontend
pnpm install
cd ../../..

echo "==> Dev container setup complete."
