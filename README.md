# StanfordWork - HR and Job Portal

A comprehensive HR and job portal built with Django, Django REST Framework, and React, featuring job postings, applications, and employer dashboards.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Local Development Setup](#local-development-setup)
- [Backend Setup](#backend-setup)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Environment Variables](#environment-variables)
- [Database Schema](#database-schema)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features

### User Features
- User registration and authentication (JWT)
- Job search and filtering
- Job application system
- User profiles and resumes
- Multi-language support (EN, DE, UZ, RU)

### Employer Features
- Job posting management
- Application tracking
- Candidate search
- Company profile management

### Admin Features
- User management
- Content management
- Analytics dashboard
- System configuration

## Tech Stack

### Backend
- Python 3.12+
- Django 5.0+
- Django REST Framework
- PostgreSQL
- Redis
- Celery

### Frontend
- React.js
- Redux Toolkit
- Tailwind CSS
- Axios

### Infrastructure
- Docker
- Nginx
- Gunicorn
- AWS S3 (for file storage)

## Prerequisites

- Docker and Docker Compose
- Python 3.12+
- Node.js 18+
- PostgreSQL 15+
- Redis 7+

## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stanfordwork.git
   cd stanfordwork
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start development services**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

4. **Apply migrations**
   ```bash
   docker-compose -f docker-compose.dev.yml exec web python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
   ```

6. **Start the development server**
   - Backend: http://localhost:8000
   - Frontend: http://localhost:3000
   - Admin: http://localhost:8000/admin

## Backend Setup

### Project Structure
```
stanfordwork/
├── apps/
│   ├── company/         # Company and job related models/views
│   ├── dashboard/       # Dashboard and analytics
│   ├── users/           # User authentication and profiles
│   └── core/            # Core functionality and utilities
├── config/              # Project settings
├── static/              # Static files
├── media/               # User uploaded files
└── tests/               # Test files
```

### API Endpoints

#### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - Obtain JWT token
- `POST /api/auth/refresh/` - Refresh JWT token
- `POST /api/auth/logout/` - Invalidate refresh token

#### Jobs
- `GET /api/jobs/` - List all jobs
- `POST /api/jobs/` - Create new job (employer only)
- `GET /api/jobs/{id}/` - Get job details
- `PUT /api/jobs/{id}/` - Update job (owner/admin only)
- `DELETE /api/jobs/{id}/` - Delete job (owner/admin only)

#### Applications
- `GET /api/applications/` - List user's applications
- `POST /api/applications/` - Submit new application
- `GET /api/applications/{id}/` - Get application details
- `PATCH /api/applications/{id}/` - Update application status (employer only)

### Running Tests

```bash
# Run all tests
docker-compose -f docker-compose.dev.yml exec web pytest

# Run specific test file
docker-compose -f docker-compose.dev.yml exec web pytest apps/users/tests/test_views.py

# Run with coverage
docker-compose -f docker-compose.dev.yml exec web pytest --cov=.
```

## Deployment

For production deployment, refer to [DEPLOYMENT.md](DEPLOYMENT.md).

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Enable debug mode | `False` |
| `SECRET_KEY` | Django secret key | - |
| `DATABASE_URL` | Database connection URL | - |
| `REDIS_URL` | Redis connection URL | `redis://redis:6379/0` |
| `ALLOWED_HOSTS` | List of allowed hosts | `['*']` |
| `CORS_ALLOWED_ORIGINS` | Allowed CORS origins | `[]` |
| `EMAIL_BACKEND` | Email backend | `django.core.mail.backends.console.EmailBackend` |
| `DEFAULT_FROM_EMAIL` | Default sender email | `noreply@stanfordwork.com` |
| `AWS_ACCESS_KEY_ID` | AWS access key | - |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key | - |
| `AWS_STORAGE_BUCKET_NAME` | S3 bucket name | - |

## Database Schema

### Core Models
- **User**: Custom user model with role-based permissions
- **Profile**: Extended user information
- **Company**: Company details and settings

### Job Models
- **Job**: Job postings with details
- **Application**: Job applications
- **Skill**: Skills and qualifications
- **Category**: Job categories

## Troubleshooting

### Common Issues

#### Database Connection Issues
- Verify database credentials in `.env`
- Check if PostgreSQL is running
- Run migrations if schema changed

#### Email Not Sending
- Check email backend configuration
- Verify SMTP settings for production
- Check spam folder

#### Static Files Not Loading
- Run `collectstatic`
- Check `STATIC_URL` and `STATIC_ROOT` settings
- Verify file permissions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.