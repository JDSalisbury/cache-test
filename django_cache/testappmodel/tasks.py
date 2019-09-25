from celery import shared_task, task
from .models import Blog
from faker import Faker
from django.core.mail import send_mail


@shared_task
def data_dump(num):
    for x in range(num):
        fake = Faker()
        Blog.objects.create(
            name=fake.name(), slug=fake.slug(), body=fake.text())


@task(name='summary')
def send_import_summary(test):
    Blog.objects.filter(name__startswith='T').delete()
    print(test)
    print('this is a summary!!')


@shared_task
def send_notification():
    print('We Did it!!')


@shared_task
def send_email_task():
    send_mail("Celery Task email!", "This was an email send by django view celery task.",
              'jsalisbury@everesttech.com', ['salisbury.jeffery@gmail.com'])
    return None
