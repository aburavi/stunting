#! /usr/bin/sh
set -e

if [ -f app/main.py ]; then
    DEFAULT_MODULE_NAME=app.main:app
fi
MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

# Start app for deployment
python app/main.py
