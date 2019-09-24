from django.test import TestCase
from testappmodel.actions.maths import adding, multiplying, subtracting
from testappmodel.tasks import send_notification, data_dump, send_import_summary


class ActionTests(TestCase):

    def test_adding(self):
        """ Test Adding """
        added = adding(1, 2)
        print('Running test adding...')
        self.assertEquals(added, 3)

    def test_multiply(self):
        """ Test Multiplying """
        multiplied = multiplying(2, 2)
        print('Running test multiplying...')
        self.assertEquals(multiplied, 4)

    def test_subtracting(self):
        """ Test Subtraction """
        subtracted = subtracting(4, 2)
        print('Running test subtracting...')
        self.assertEquals(subtracted, 2)

    def test_task_notification(self):
        task = send_notification.s().apply()
        result = task.get()
        self.assertEqual(task.status, "SUCCESS")

    def test_task_data_dump(self):
        task = data_dump.s(2).apply()
        result = task.get()
        self.assertEqual(task.status, "SUCCESS")

    def test_task_import_summary(self):
        task = send_import_summary.s("Testing s").apply()
        result = task.get()
        self.assertEqual(task.status, "SUCCESS")
