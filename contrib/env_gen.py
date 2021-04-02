import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"  # noqa E501
size = 50
secret_key = "".join(random.sample(chars, size))

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%_"
size = 32
password = "".join(random.sample(chars, size))

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost, 0.0.0.0
DATABASE_NAME=db
DATABASE_USER=myuser
POSTGRES_PASSWORD=%s
DATABASE_HOST=localhost
APP_ID=
KEY=
SECRET=
CLUSTER=
""".strip() % (secret_key, password)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')
