import unittest
import builder
import data

class TestCases(unittest.TestCase):

    def test_units_combinations(self):
        user_classes = ["CSC101","PHYS143","MATH244","EE151","EE111","COMS101"]
        expected =
        result = builder.make_combinations_with_units(user_classes)
        self.assertEqual(expected,result)




if __name__ == '__main__':
    unittest.main()