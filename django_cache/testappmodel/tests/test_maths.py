from django.test import TestCase
from testappmodel.actions.maths import adding, multiplying, subtracting, dividing
from django.test import tag


class ActionTests(TestCase):

    @tag('action')
    def test_adding(self):
        """ Test Adding """
        added = adding(1, 2)
        print('Running test adding...')
        self.assertEquals(added, 3)

    @tag('action')
    def test_multiply(self):
        """ Test Multiplying """
        multiplied = multiplying(2, 2)
        print('Running test multiplying...')
        self.assertEquals(multiplied, 4)

    @tag('action')
    def test_subtracting(self):
        """ Test Subtraction """
        subtracted = subtracting(4, 2)
        print('Running test subtracting...')
        self.assertEquals(subtracted, 2)

    @tag('action')
    def test_dividing(self):
        """Testing Division"""
        divided = dividing(4, 2)
        print("Divided")
        self.assertEqual(divided, 2)
