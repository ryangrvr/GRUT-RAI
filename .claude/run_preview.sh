#!/bin/bash
# Launch GRUT-RAI server using working Python 3.13
cd "$(dirname "$0")/.."
exec /opt/local/bin/python3.13 -m flask --app ui.app run --host 127.0.0.1 --port 5000
