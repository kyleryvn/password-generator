from generator import generate
import unittest


class MyTestCase(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
