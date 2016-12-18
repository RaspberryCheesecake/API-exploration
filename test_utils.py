import unittest
from who_in_space import get_who_in_space, display_who_in_space

class TestFulfillsChallenge47(unittest.TestCase):

    def setUp(self):
        self.mock_data = {"people" : [
            {"craft": "Apollo", "name": "Buzz Aldrin"},
            {"craft": "Millenium Falcon", "name": "Luke Skywalker"},
            {"craft": "Millenium Falcon", "name": "Han Solo"}
            ]}
        self.mock_data["message"] = "success"
        self.mock_data["number"] = 3

    def test_width_of_column_wide_enough(self):
        result = display_who_in_space(self.mock_data)
 
        expected_result = """The number of people currently in space is : 3
They are :
Name          |Craft
--------------|------------------
Buzz Aldrin   |Apollo
Luke Skywalker|Millenium Falcon
Han Solo      |Millenium Falcon
"""
        self.assertEqual(result, expected_result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
