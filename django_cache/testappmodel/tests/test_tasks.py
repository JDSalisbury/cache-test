from django.test import TestCase
from testappmodel.tasks import *
from django.test import tag


class TaskTests(TestCase):

    @tag('task')
    def test_task_notification(self):
        """ Send Notification Task test """
        task = send_notification.s().apply()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_task_data_dump(self):
        """ Data Dump Task test """
        task = data_dump.s(2).apply()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_task_import_summary(self):
        """ Send Import Summary Task Test """
        task = send_import_summary.s("Testing s").apply()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_email_task(self):
        """ Sending an Email via celery """
        task = send_email_task.s().apply()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_delete_trash_task(self):
        """ Delete Trash Contents Task Test """
        task = delete_trash_task.s().apply()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_create_txt_file(self):
        """ Task That creates A file """
        task = create_txt_file_task.s().apply()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_delete_txt_folder_task(self):
        """ Deleting folder contents based on number of files inside """
        task = delete_txt_folder_task.s(0).apply()
        self.assertEqual(task.status, "SUCCESS")
