#!/bin/sh

set -e

until nc -z -v -w30 db 5432
do
  echo "Waiting for database connection..."
  sleep 1
done
  echo "Database connection established"

apply_migrations_and_run() {
    echo "Applying DB migrations"
    alembic upgrade "$1"

    # Check if alembic command was successful
    if [ $? -eq 0 ]; then
        echo "Migrations applied successfully."
        python get_data.py

        # Check if Python script ran successfully
        if [ $? -eq 0 ]; then
            echo "Data has been parsed and saved to the database successfully."
        else
            echo "An error occurred while parsing data."
        fi
    else
        echo "Migration failed. Skipping data parsing."
    fi
}

if [ "$DATA_ORIGIN" = "wikipedia" ]; then
    echo "Parsing from Wikipedia..."
    apply_migrations_and_run "$WIKI_MIGRATION_ID"

elif [ "$DATA_ORIGIN" = "statisticstimes" ]; then
    echo "Parsing from Statistics Times..."
    apply_migrations_and_run "$STATS_TIMES_MIGRATION_ID"

else
    echo "DATA_ORIGIN is not set or is invalid. Skipping migrations."
fi