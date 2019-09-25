from django.test import TestCase
from testappmodel.tasks import send_notification, data_dump, send_import_summary, send_email_task
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
