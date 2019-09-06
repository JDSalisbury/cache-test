# cache-test

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
