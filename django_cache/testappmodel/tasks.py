from celery import shared_task, task
from .models import Blog
from faker import Faker
from django.core.mail import send_mail
import os
import shutil

txt_folder = '/Users/jeffsalisbury/Documents/Code/Python_Code/cache-test/django_cache/testappmodel/weirdtxtfiles'
trash_folder = '/Users/jeffsalisbury/.Trash'
content_limit = 6


@shared_task(name='Blog Create')
def data_dump(num):
    for x in range(num):
        fake = Faker()
        Blog.objects.create(
            name=fake.name(), slug=fake.slug(), body=fake.text())


@task(name='Delete T authored Blogs')
def send_import_summary(test):
    Blog.objects.filter(name__startswith='T').delete()
    print(test)
    print('this is a summary!!')


@shared_task(name='Print Something')
def send_notification():
    print('We Did it!!')


@shared_task(name='Email')
def send_email_task():
    send_mail("Celery Task email!", "This was an email send by django view celery task.",
              'jsalisbury@everesttech.com', ['salisbury.jeffery@gmail.com'])
    return None


@shared_task(name='Delete Trash')
def delete_trash_task(folder=trash_folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


@shared_task(name='Delete Folder Contents when over 6 files')
def delete_txt_folder_task():
    list = os.listdir(txt_folder)
    number_files = len(list)
    if number_files >= content_limit:
        delete_trash_task(txt_folder)


@shared_task(name='Create File')
def create_txt_file_task():
    fake = Faker()
    file_name = fake.slug() + '.txt'

    completeName = os.path.join(txt_folder, file_name)

    f = open(completeName, 'w+')
    for i in range(10):
        f.write(fake.city() + ' This is line %d\r\n' % (i+1))
    f.close()
