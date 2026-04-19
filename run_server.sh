#!/bin/bash
# GRUT-RAI server launcher
# Finds a compatible Python (3.10-3.13) and starts the Flask dev server on :5000

set -e
cd "$(dirname "$0")"

# Prefer explicit 3.13, then 3.12, then 3.11, then 3.10, then fallback python3
for CANDIDATE in python3.13 python3.12 python3.11 python3.10 python3; do
    if command -v "$CANDIDATE" >/dev/null 2>&1; then
        # Confirm it's in the supported range (10..14-exclusive)
        VER=$("$CANDIDATE" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "0.0")
        MAJOR=${VER%.*}
        MINOR=${VER#*.}
        if [ "$MAJOR" = "3" ] && [ "$MINOR" -ge 10 ] && [ "$MINOR" -le 13 ]; then
            PYTHON="$CANDIDATE"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo "ERROR: No compatible Python found."
    echo "GRUT-RAI requires Python 3.10, 3.11, 3.12, or 3.13."
    echo "Python 3.14+ is not yet supported (numpy compatibility)."
    echo ""
    echo "Install with:  brew install python@3.13  (macOS)"
    echo "         or:  apt install python3.13     (Ubuntu/Debian)"
    exit 1
fi

echo "Using: $PYTHON ($VER)"

# Check required packages are present; if not, hint at installation
if ! "$PYTHON" -c "import numpy, scipy, flask" 2>/dev/null; then
    echo ""
    echo "Missing dependencies. Install with:"
    echo "  $PYTHON -m pip install -r requirements.txt"
    exit 1
fi

# Start the server
exec "$PYTHON" -m flask --app ui.app run --port 5000
