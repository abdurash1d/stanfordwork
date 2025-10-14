import os
import getpass
from pathlib import Path

def setup_env():
    env_path = Path('.env')
    
    if env_path.exists():
        print("\n⚠️  .env file already exists. I'll back it up first.")
        backup_path = Path('.env.backup')
        if backup_path.exists():
            backup_path.unlink()
        env_path.rename(backup_path)
        print(f"✅ Created backup at {backup_path}")
    
    print("\n🛠️  Configuring environment variables...")
    
    # Default values
    config = {
        'DEBUG': 'True',
        'SECRET_KEY': 'django-insecure-' + os.urandom(32).hex(),
        'ALLOWED_HOSTS': 'localhost,127.0.0.1,0.0.0.1',
        'DATABASE_URL': 'sqlite:///db.sqlite3',
        'EMAIL_HOST': 'smtp.gmail.com',
        'EMAIL_PORT': '587',
        'EMAIL_USE_TLS': 'True',
        'EMAIL_HOST_USER': input('\n📧 Enter your email (for sending emails): ') or 'your-email@example.com',
        'REDIS_URL': 'redis://localhost:6379/0',
        'SENTRY_DSN': '',
        'CELERY_BROKER_URL': 'redis://localhost:6379/0',
        'CELERY_RESULT_BACKEND': 'redis://localhost:6379/0',
        'DJANGO_LOG_LEVEL': 'INFO'
    }
    
    # Ask for email password securely
    email_pwd = getpass.getpass('🔑 Enter your email password (input hidden): ')
    config['EMAIL_HOST_PASSWORD'] = email_pwd
    config['DEFAULT_FROM_EMAIL'] = config['EMAIL_HOST_USER']
    
    # Generate .env content
    env_content = """# Django Settings
DEBUG={DEBUG}
SECRET_KEY={SECRET_KEY}
ALLOWED_HOSTS={ALLOWED_HOSTS}

# Database
DATABASE_URL={DATABASE_URL}

# Email Configuration
EMAIL_HOST={EMAIL_HOST}
EMAIL_PORT={EMAIL_PORT}
EMAIL_USE_TLS={EMAIL_USE_TLS}
EMAIL_HOST_USER={EMAIL_HOST_USER}
EMAIL_HOST_PASSWORD={EMAIL_HOST_PASSWORD}
DEFAULT_FROM_EMAIL={DEFAULT_FROM_EMAIL}

# Redis
REDIS_URL={REDIS_URL}

# Sentry
SENTRY_DSN={SENTRY_DSN}

# Celery
CELERY_BROKER_URL={CELERY_BROKER_URL}
CELERY_RESULT_BACKEND={CELERY_RESULT_BACKEND}

# Logging
DJANGO_LOG_LEVEL={DJANGO_LOG_LEVEL}
""".format(**config)
    
    # Write to .env file
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n✅ .env file created successfully!")
    print("\n🔒 Please ensure this file is in your .gitignore and not committed to version control.")

if __name__ == "__main__":
    try:
        setup_env()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nPlease make sure you have the necessary permissions to create/modify files in this directory.")
        exit(1)
