#!/bin/bash
flask db migrate
flask db upgrade
# gunicorn -w 4 --log-level debug --access-logfile ./auth.log -b 0.0.0.0:5001 "auth:create_app()"
gunicorn -w 4 --log-level debug --access-logfile /dev/fd/1 -b 0.0.0.0:5001 "auth:create_app()"