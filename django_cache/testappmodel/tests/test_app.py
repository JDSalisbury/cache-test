from django.test import TestCase
from testappmodel.actions.maths import adding, multiplying, subtracting


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
