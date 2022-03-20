from generator import generate
import unittest


class MyTestCase(unittest.TestCase):
    def test_generator(self):
        password = generate()
        self.assertEqual(True, password)  # should always return a random password


if __name__ == '__main__':
    unittest.main()
