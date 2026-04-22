#!/bin/bash
# Launch GRUT-RAI server for Claude Preview (preview_start).
#
# Finds any Python in [3.10, 3.13] that has the required deps installed.
# Python 3.14+ is rejected because numpy doesn't yet ship wheels for it.
# Honors $GRUT_PYTHON if set (e.g. GRUT_PYTHON=/path/to/python3.13 preview_start).

set -e
cd "$(dirname "$0")/.."

PYTHON="${GRUT_PYTHON:-}"
if [ -z "$PYTHON" ]; then
    for CANDIDATE in python3.13 python3.12 python3.11 python3.10 \
                      /opt/local/bin/python3.13 /opt/local/bin/python3.12 \
                      /usr/local/bin/python3.13 /usr/local/bin/python3.12 \
                      /opt/homebrew/bin/python3.13 /opt/homebrew/bin/python3.12 \
                      python3; do
        if command -v "$CANDIDATE" >/dev/null 2>&1; then
            VER=$("$CANDIDATE" -c 'import sys;print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "0.0")
            MAJOR=${VER%.*}; MINOR=${VER#*.}
            if [ "$MAJOR" = "3" ] && [ "$MINOR" -ge 10 ] && [ "$MINOR" -le 13 ]; then
                # Confirm numpy/flask importable before accepting
                if "$CANDIDATE" -c 'import numpy, flask' 2>/dev/null; then
                    PYTHON="$CANDIDATE"
                    break
                fi
            fi
        fi
    done
fi

if [ -z "$PYTHON" ]; then
    echo "ERROR: No Python 3.10-3.13 with numpy+flask found." >&2
    echo "Install deps:  pip install -r requirements.txt" >&2
    echo "Or set:        export GRUT_PYTHON=/full/path/to/python3.13" >&2
    exit 1
fi

echo "GRUT-RAI preview using $PYTHON ($("$PYTHON" --version 2>&1))" >&2
exec "$PYTHON" -m flask --app ui.app run --host 127.0.0.1 --port 5000
