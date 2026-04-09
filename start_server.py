#!/usr/bin/env python3
"""Start the GRUT-RAI API server directly (bypasses sandbox issues)."""
import os, sys

PROJECT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT)
os.chdir(PROJECT)

# Pre-import h11 to prevent sandbox path-scanning errors
import h11

from api.main import app
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info",
            loop="asyncio", http="h11")
