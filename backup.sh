#!/bin/bash

# Exit on error
set -e

# Load environment variables
set -a
source .env.prod
set +a

# Create backup directory with timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="./backups/$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

# Backup PostgreSQL database
echo "Backing up PostgreSQL database..."
docker-compose exec -T db pg_dump -U $POSTGRES_USER -d $POSTGRES_DB > "$BACKUP_DIR/db_backup.sql"

# Backup media files
echo "Backing up media files..."
docker cp "$(docker-compose ps -q web):/app/media/" "$BACKUP_DIR/"

# Create a compressed archive
echo "Creating backup archive..."
tar -czf "$BACKUP_DIR.tar.gz" -C "$BACKUP_DIR" .

# Clean up
echo "Cleaning up..."
rm -rf "$BACKUP_DIR"

echo "Backup completed: $BACKUP_DIR.tar.gz"
