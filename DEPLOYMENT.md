# StanfordWork Deployment Guide

This guide provides instructions for deploying the StanfordWork project to a production server.

## Prerequisites

- Docker and Docker Compose installed on the server
- Domain name pointed to your server's IP address
- SSH access to the server

## Server Setup

1. **Update system packages**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Docker and Docker Compose**
   ```bash
   sudo apt install -y docker.io docker-compose
   sudo systemctl enable --now docker
   sudo usermod -aG docker $USER
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stanfordwork.git
   cd stanfordwork
   ```

## Configuration

1. **Create environment file**
   ```bash
   cp .env.prod.example .env.prod
   nano .env.prod  # Update with your configuration
   ```

2. **Set up SSL certificates** (first time only)
   ```bash
   mkdir -p certbot/{conf,www,scripts}
   # Update nginx/nginx.conf with your domain name
   # Run the initial certificate setup
   docker-compose run --rm certbot certonly --webroot -w /var/www/certbot/ -d yourdomain.com
   ```

## Deployment

1. **Start the application**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. **Verify the deployment**
   ```bash
   docker-compose ps  # Check if all services are running
   curl https://yourdomain.com/health/  # Check health status
   ```

## Maintenance

### Backups

To create a backup:
```bash
chmod +x backup.sh
./backup.sh
```

### Updating the Application

1. Pull the latest changes:
   ```bash
   git pull origin main
   ```

2. Rebuild and restart the containers:
   ```bash
   docker-compose up -d --build
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py collectstatic --noinput
   ```

### Monitoring

Check container logs:
```bash
docker-compose logs -f  # Follow logs
docker-compose logs web  # Web container logs
docker-compose logs db   # Database logs
```

## Troubleshooting

- **502 Bad Gateway**: Check if the web service is running with `docker-compose ps`
- **Database connection issues**: Verify the database credentials in `.env.prod`
- **SSL certificate renewal**: Certbot will automatically renew certificates, but you can force renewal with:
  ```bash
  docker-compose run --rm certbot renew --force-renewal
  docker-compose restart nginx
  ```

## Security Considerations

- Keep your `.env.prod` file secure and never commit it to version control
- Regularly update your server and dependencies
- Monitor your server logs for suspicious activity
- Use strong passwords for all accounts
- Enable firewall and only allow necessary ports (80, 443, SSH)

## Support

For any issues, please create an issue in the GitHub repository or contact support@yourdomain.com.
