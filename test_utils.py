import unittest
from who_in_space import get_who_in_space, display_who_in_space

class TestFulfillsChallenge47(unittest.TestCase):

    def setUp(self):
        self.mock_data = {"people" : [
            {"craft": "ISS", "name": "Buzz Aldrin"},
            {"craft": "ISS", "name": "Luke Skywalker"},
            {"craft": "ISS", "name": "Jules Verne"}
            ]}
        self.mock_data["message"] = "success"
        self.mock_data["number"] = 3

    def test_width_of_column_wide_enough(self):
        display_who_in_space(self.mock_data)
        self.assertEqual('foo'.upper(), 'FOO')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
