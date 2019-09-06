from celery import shared_task
from .models import Blog
from faker import Faker


@shared_task
def data_dump(num):
    for x in range(num):
        fake = Faker()
        Blog.objects.create(
            name=fake.name(), slug=fake.slug(), body=fake.text())
