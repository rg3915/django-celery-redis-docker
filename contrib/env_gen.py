#!/usr/bin/env python

"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
password = 'abcdefghijklmnopqrstuvwxyz0123456789'

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost
DATABASE_NAME=django_celery_db
DATABASE_USER=myuser
DATABASE_PASSWORD=%s
DATABASE_HOST=localhost
APP_ID=xyz
KEY=xyz
SECRET=xyz
CLUSTER=xyz
""".strip() % (get_random_string(50, chars), get_random_string(32, password))

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
