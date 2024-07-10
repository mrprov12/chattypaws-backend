#!/bin/bash

# Load environment variables from .env file
set -a
source .env
set +a

# Drop the database
echo "Dropping the database $DB_DATABASE_NAME..."
docker exec -it $DB_CONTAINER_NAME psql -U $DB_USERNAME -d postgres -c "DROP DATABASE IF EXISTS $DB_DATABASE_NAME;"

# Recreate the database
echo "Recreating the database $DB_DATABASE_NAME..."
docker exec -it $DB_CONTAINER_NAME psql -U $DB_USERNAME -d postgres -c "CREATE DATABASE $DB_DATABASE_NAME;"

# Reimport the schema
echo "Reimporting the schema to $DB_DATABASE_NAME..."
cat $SCHEMA_FILE | docker exec -i $DB_CONTAINER_NAME psql -U $DB_USERNAME -d $DB_DATABASE_NAME

echo "Database reset complete."
