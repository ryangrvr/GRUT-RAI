#!/bin/bash
cd "$(dirname "$0")"
export PATH="/opt/local/bin:$PATH"
export PYTHONPATH="$(pwd)"
echo "Using python: $(which python3)" >&2
echo "Python version: $(/opt/local/bin/python3.13 --version)" >&2
exec /opt/local/bin/python3.13 -m flask --app ui.app run --port 5000 --host 0.0.0.0
