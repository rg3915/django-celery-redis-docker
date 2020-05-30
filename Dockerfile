FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1
RUN mkdir /app
WORKDIR /app
EXPOSE 8000

ADD requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY .env .
COPY manage.py .
COPY myproject ./myproject

RUN mkdir static & \
    python manage.py collectstatic --noinput
# python manage.py migrate
CMD gunicorn myproject.wsgi:application -b 0.0.0.0:8000
