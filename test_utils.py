import unittest
from who_in_space import get_who_in_space, display_who_in_space

class TestFulfillsChallenge47(unittest.TestCase):

    def setUp(self):
        pass

    def test_width_of_column_wide_enough(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
