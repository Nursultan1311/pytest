import unittest

class TestAddition(unittest.TestCase):

    def test_addition(self):
        result = 2 + 3
        expected = 5
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

