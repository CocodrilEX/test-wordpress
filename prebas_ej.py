import unittest
from example import my_function

class TestExample(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(my_function(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
