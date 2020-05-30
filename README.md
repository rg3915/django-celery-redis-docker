# django-celery-redis-docker

Test Django and Celery on Docker with Redis

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-celery-redis-docker.git
cd django-celery-redis-docker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Rodando com Docker

```
docker-compose up --build
```

Entre no container e rode as migrações:

```
docker container exec -ti ID python manage.py migrate
docker container exec -ti ID python manage.py createsuperuser
```

Está rodando na porta `localhost:82`. Ou você pode digitar

```
docker container inspect ID
```

e pegar o `IPAddress`.

## Rodando o Celery

Abra outro terminal com o virtualenv ativado e digite

Dá pra fazer sem o `queue`.

```
# terminal 1
celery --app=myproject worker --loglevel=INFO
```

Mas o `queue` define uma fila.

```
# terminal 1
celery --app=myproject worker --loglevel=INFO --queue=fila1
```

## Experimentando o flower

O [flower](https://flower.readthedocs.io/en/latest/) serve pra monitorar o Celery em realtime.

Rode num outro terminal o comando

```
# terminal 2
celery -A myproject flower
```

Se for no Docker, pegue o ip do service flower

```
IP-ADDRESS:5555
```

Se quiser estressar o Celery e ver no monitor digite

```
for i in $(seq 10); do curl localhost:8000/task/print_numbers/; sleep 1; done
```

A url do monitor é http://localhost:5555/monitor


### Instalando e configurando django-celery-results

https://django-celery-results.readthedocs.io/en/latest/

```
python manage.py migrate django_celery_results
```

### Links

https://medium.com/@mdcg.dev/configurando-um-sistem-em-django-para-executar-tarefas-ass%C3%ADncronas-utilizando-celery-redis-e-53a30d0d2ec2

