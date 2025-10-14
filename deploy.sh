#!/bin/bash

# Exit on error
set -e

# Create necessary directories
mkdir -p nginx certbot/{conf,www,scripts} postgres/backups

# Set proper permissions
chmod -R 755 nginx certbot postgres

# Copy environment file if it doesn't exist
if [ ! -f .env.prod ]; then
    echo "Creating .env.prod from example file"
    cp .env.prod.example .env.prod
    echo "Please edit .env.prod with your configuration"
    exit 1
fi

# Load environment variables
set -a
source .env.prod
set +a

# Build and start containers
echo "Building and starting containers..."
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

echo "Waiting for database to be ready..."
# Wait for PostgreSQL to be ready
until docker-compose exec db pg_isready -U $POSTGRES_USER -d $POSTGRES_DB; do
    echo "Waiting for PostgreSQL..."
    sleep 2
done

# Run database migrations
echo "Running database migrations..."
docker-compose exec web python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
docker-compose exec web python manage.py collectstatic --noinput

# Create superuser if needed
# Uncomment and modify if you need to create a superuser
# docker-compose exec web python manage.py createsuperuser

echo "Deployment completed successfully!"
echo "Your application is running at https://$ALLOWED_HOSTS"
