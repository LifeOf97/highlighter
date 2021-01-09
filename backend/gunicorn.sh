#!/usr/bin/bash

# Author: Kelvin Mayowa Ayeni.
# Copy (c): Aces & Coup inc.
# Purpose: Run a Gunicorn server.
# Date: Tuesday September 30 2020.
# Last editted: 

echo "GREEN UNICORN SERVER"
gunicorn --workers=2 --bind=0.0.0.0:8000 --reload --reload-engine='inotify' src.wsgi:application
