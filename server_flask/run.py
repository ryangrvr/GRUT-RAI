#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5001))
    print(f"[GRUT Flask] Starting on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=True)
