#!/bin/bash
./stop_all.sh
echo "Try to run api..."
DB_USER=dev-user DB_PASSWORD=Hesoyam25$ HOST_NAME=localhost DB_NAME=Estore_db python3   -m backend.api.api
