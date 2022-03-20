from generator import generate
import unittest


class MyTestCase(unittest.TestCase):
    def test_generator(self):
        password_one = generate()
        password_two = generate()
        self.assertNotEqual(password_one, password_two)  # should always return a random password


if __name__ == '__main__':
    unittest.main()
