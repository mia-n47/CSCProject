import unittest
import builder
import data

class TestCases(unittest.TestCase):

    def test_units_combinations(self):
        user_classes = [data.Classes("CSC101", "TUETHU","8 am", "11am",4),
            data.Classes("PHYS143", "TUETHU", "1 pm", "3pm",4),
            data.Classes("MATH244", "MONTUETHUFRI", "7am", "8am",4)]
        expected = [[data.Classes("CSC101", "TUETHU","8 am", "11am",4),
            data.Classes("PHYS143", "TUETHU", "1 pm", "3pm",4),
            data.Classes("MATH244", "MONTUETHUFRI", "7am", "8am",4)]]
        result = builder.make_combinations_with_units(user_classes)
        self.assertEqual(expected,result)




if __name__ == '__main__':
    unittest.main()