import unittest
from builder import user_data
import data

class TestCases(unittest.TestCase):
    def test_task1_first(self):
        d = [data.Classes("CSC101", "TUETHU","8 am", "11am",4),
            data.Classes("PHYS143", "TUETHU", "1 pm", "3pm",4),
            data.Classes("MATH244", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("COMS101", "TUETHU","12pm", "2pm",4),
            data.Classes("ENGL145", "WEDFRI", "11am", "1pm",4)]
        expected = ["CSC101","PHYS143", "MATH244", "COMS101", "ENGL145"]
        result = user_data(d)
        self.assertEqual(expected,result)




if __name__ == '__main__':
    unittest.main()