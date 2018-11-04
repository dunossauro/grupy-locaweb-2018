from unittest import TestCase
from app import head

class TestHead(TestCase):
    def test_head(self):
        self.assertEqual(head([1,2,3]), 1)
