from django.test import TestCase
from testappmodel.tasks import send_notification, data_dump, send_import_summary
from django.test import tag


class TaskTests(TestCase):

    @tag('task')
    def test_task_notification(self):
        task = send_notification.s().apply()
        result = task.get()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_task_data_dump(self):
        task = data_dump.s(2).apply()
        result = task.get()
        self.assertEqual(task.status, "SUCCESS")

    @tag('task')
    def test_task_import_summary(self):
        task = send_import_summary.s("Testing s").apply()
        result = task.get()
        self.assertEqual(task.status, "SUCCESS")
