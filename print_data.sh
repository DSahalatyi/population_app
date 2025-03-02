#!/bin/sh

set -e

until nc -z -v -w30 db 5432
do
  echo "Waiting for database connection..."
  sleep 1
done
  echo "Database connection established"

echo "Reading and printing data from DB:"
python print_data.py

if [ $? -ne 0 ]; then
    echo "An error occurred while reading or printing data."
    exit 1
fi