#!/bin/bash
cd "$(dirname "$0")"
/usr/bin/python3 -m flask --app ui.app run --port 5000
