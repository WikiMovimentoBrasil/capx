SECRET_KEY = '<YOUR VERY SECRET KEY>'
DEBUG = False
ALLOWED_HOSTS = ['<YOUR HOSTS>']

# Database configurations

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Use 'localhost' if the database is on the same machine
        'PORT': '',  # Default PostgreSQL port (5432)
    }
}
