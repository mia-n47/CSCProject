import unittest
from builder import user_data, analyze_time, convert_to_data, sort_classes_by_time, make_combinations_with_units, get_start_time, classes_overlap,verify_combinations
import data
import datetime

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
    def test_task1_second(self):
        d = [data.Classes("EE111", "FRI", "9am", "10am",1),
            data.Classes("ENGL134", "MONWEDFRI", "4pm", "6pm",4),
            data.Classes("EE151", "TUE", "8 am", "11 am",1)]
        expected = ["EE111","ENGL134", "EE151"]
        result = user_data(d)
        self.assertEqual(expected,result)

    def test_task2_first(self):
        user_classes_str = ["COMS101"]
        expected = [data.Classes("COMS101", "TUETHU","12pm", "2pm",4)]
        result = convert_to_data(user_classes_str)
        self.assertEqual(expected,result)
    def test_task2_second(self):
        user_classes_str = ["EE111"]
        expected = [data.Classes("EE111", "FRI", "9am", "10am",1)]
        results = convert_to_data(user_classes_str)
        self.assertEqual(expected,results)

    def test_task3_first(self):
        time_str = "11am"
        expected = datetime.datetime(1900, 1, 1, 11, 0)
        result = analyze_time(time_str)
        self.assertEqual(expected,result)
    def test_task3_second(self):
        time_str = "6pm"
        expected = datetime.datetime(1900,1,1,18,0)
        result = analyze_time(time_str)
        self.assertEqual(expected,result)

    def test_task4_first(self):
        classes = [ data.Classes("COMS101", "TUETHU","12pm", "2pm",4),
            data.Classes("ENGL145", "WEDFRI", "11am", "1pm",4),
            data.Classes("CHEM124", "MONWED", "6pm", "9pm",4)]
        expected = [data.Classes("ENGL145", "WEDFRI", "11am", "1pm",4),data.Classes("COMS101", "TUETHU","12pm", "2pm",4),data.Classes("CHEM124", "MONWED", "6pm", "9pm",4)]
        result = sort_classes_by_time(classes)
        self.assertEqual(expected,result)
    def test_task4_second(self):
        classes = [data.Classes("ENGL134", "MONWEDFRI", "4pm", "6pm",4),
            data.Classes("EE151", "TUE", "8 am", "11 am",1)]
        expected = [data.Classes("EE151", "TUE", "8 am", "11 am",1),data.Classes("ENGL134", "MONWEDFRI", "4pm", "6pm",4)]
        result = sort_classes_by_time(classes)
        self.assertEqual(expected,result)

    def test_task5_first(self):
        user_classes = [data.Classes("CHEM124", "MONWED", "6pm", "9pm",4),
            data.Classes("EE111", "FRI", "9am", "10am",1),
            data.Classes("ENGL134", "MONWEDFRI", "4pm", "6pm",4),
            data.Classes("EE151", "TUE", "8 am", "11 am",1),
            data.Classes("PHYS141", "MONTUETHUFRI", "5pm", "6pm",4)]
        expected = []
        result = make_combinations_with_units(user_classes)
        self.assertEqual(expected,result)
    def test_task5_second(self):
        user_classes = [data.Classes("PHYS141", "MONTUETHUFRI", "5pm", "6pm",4),
            data.Classes("MATH241", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("MATH142", "MONTUETHUFRI", "9am", "10am",4),
            data.Classes("MATH141", "MONTUETHUFRI", "7am", "8am",4)]
        expected = [[data.Classes("PHYS141", "MONTUETHUFRI", "5pm", "6pm",4),
            data.Classes("MATH241", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("MATH142", "MONTUETHUFRI", "9am", "10am",4),
            data.Classes("MATH141", "MONTUETHUFRI", "7am", "8am",4)]]
        result = make_combinations_with_units(user_classes)
        self.assertEqual(expected,result)

    def test_task6_first(self):
        class_tuple = (analyze_time("8am"), data.Classes("EE151", "TUE", "8 am", "11 am",1))
        expected = datetime.datetime(1900, 1, 1, 8, 0)
        result = get_start_time(class_tuple)
        self.assertEqual(expected,result)
    def test_task6_second(self):
        class_tuple = (analyze_time("10am"),data.Classes("ARCE315", "MONWED", "10am", "12pm",4))
        expected = datetime.datetime(1900,1,1,10,0)
        result = get_start_time(class_tuple)
        self.assertEqual(expected,result)

    def test_task7_first(self):
        c1 = data.Classes("MATH241", "MONTUETHUFRI", "7am", "8am",4)
        c2 = data.Classes("MATH141", "MONTUETHUFRI", "7am", "8am",4)
        expected = True
        result = classes_overlap(c1,c2)
        self.assertEqual(expected,result)
    def test_task7_second(self):
        c1 = data.Classes("MATH141", "MONTUETHUFRI", "7am", "8am",4)
        c2 = data.Classes("AERO220", "TUE", "3pm", "6pm",4)
        expected = False
        result = classes_overlap(c1,c2)
        self.assertEqual(expected,result)

    def test_task8_first(self):
        unit_verified_combinations = [[data.Classes("COMS101", "TUETHU","12pm", "2pm",4),
            data.Classes("ENGL145", "WEDFRI", "11am", "1pm",4),
            data.Classes("CHEM124", "MONWED", "6pm", "9pm",4),
            data.Classes("EE111", "FRI", "9am", "10am",1)]]
        expected = []
        result = verify_combinations(unit_verified_combinations)
        self.assertEqual(expected,result)
    def test_task8_second(self):
        unit_verified_combinations = [[data.Classes("CHEM124", "MONWED", "6pm", "9pm",4),
                                       data.Classes("COMS101", "TUETHU","12pm", "2pm",4),

                                       ]]
        expected = []
        result = verify_combinations(unit_verified_combinations)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()