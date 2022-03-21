from generator import generate
import unittest


class MyTestCase(unittest.TestCase):
    def test_generator(self):
        password_one = generate(16)
        password_two = generate(16)

        print(f'First password={password_one}')
        print(f'First password={password_two}')

        self.assertNotEqual(password_one, password_two)  # should always return a random password


if __name__ == '__main__':
    unittest.main()
