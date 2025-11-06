#! /usr/bin/sh
set -e

docker build -t fastapi-app .
docker run -p 8080:8000 fastapi-app