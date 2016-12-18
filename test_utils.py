import unittest
from who_in_space import get_who_in_space, display_who_in_space

class TestFulfillsChallenge47(unittest.TestCase):

    def setUp(self):
        self.mock_data = {"people" : [
            {"craft": "Millenium Falcon", "name": "Han Solo"},
            {"craft": "Apollo", "name": "Buzz Aldrin"},
            {"craft": "Millenium Falcon", "name": "Luke Skywalker"}
            ]}
        self.mock_data["message"] = "success"
        self.mock_data["number"] = 3

    def test_sorting_astronauts_alphabetically(self):
        result = display_who_in_space(self.mock_data)
 
        expected_result = """The number of people currently in space is : 3
They are :
Name          |Craft
--------------|------------------
Buzz Aldrin   |Apollo
Han Solo      |Millenium Falcon
Luke Skywalker|Millenium Falcon
"""
        self.assertEqual(result, expected_result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
