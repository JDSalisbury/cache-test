# cache-test

run Redis

```
redis-server
```

run celery worker

```
celery worker -A django_cache --loglevel=info
```

run admin Celery Beat Tasks

```
celery -A django_cache beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

run flower to view tasks doing things

```
celery flower -A django_cache --broker=redis://localhost:6379//
```

Added coverage .py

```
coverage erase
coverage run manage.py test
coverage report -m
coverage html

```

Enter Docker

```
docker ps # lists running containers
docker exec -it <container name> /bin/bash

```

[Celery-Beat](https://www.merixstudio.com/blog/django-celery-beat/)

[Redis-Celery](https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/)

[Check to see if tasks are running](https://www.vinta.com.br/blog/2017/how-make-sure-celery-beat-tasks-are-working/)

[Coverage](https://coverage.readthedocs.io/en/v4.5.x/index.html)

Allegedly this is the best way to test Tasks.
[Test Celery Tasks](https://www.distributedpython.com/2018/05/01/unit-testing-celery-tasks/)
