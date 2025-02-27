import data

database = [data.Classes("CSC 101", "TUETHU","8 am", "11am",4),
            data.Classes("PHYS 143", "TUETHU", "1 pm", "3pm",4),
            data.Classes("MATH 244", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("COMS 101", "TUETHU","12pm", "2pm",4),
            data.Classes("ENGL 145", "WEDFRI", "11am", "1pm",4),
            data.Classes("CHEM 124", "MONWED", "6pm", "9pm",4),
            data.Classes("EE 111", "FRI", "9am", "10am",1),
            data.Classes("ENGL 134", "MONWEDFRI", "4pm", "6pm",4),
            data.Classes("EE 151", "TUE", "8 am", "11 am",1),
            data.Classes("PHYS 141", "MONTUETHUFRI", "5pm", "6pm",4),
            data.Classes("MATH 241", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("MATH 142", "MONTUETHUFRI", "9am", "10am",4),
            data.Classes("MATH 141", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("ES 256", "TUETHU", "8am", "10am",4),
            data.Classes("PHYS 142", "WEDFRI", "2pm","4pm",4),
            data.Classes("AERO 220", "TUE", "3pm", "6pm",4),
            data.Classes("AERO 299", "MONWEDFRI", "12pm", "1pm",4),
            data.Classes("AG 413", "TUE", "11am", "12pm",2),
            data.Classes("AG 581", "THU", "2pm", "3pm",2),
            data.Classes("ARCE 315", "MONWED", "10am", "12pm",4),
            data.Classes("ARCE 354", "TUE","8am", "11am",2),
            data.Classes("SPAN380","TUETHU", "2pm", "4pm",4)
            ]
def user_data(d: list[data.Classes]) -> list[str]:
    user_friendly = []
    for clas in d:
        user_friendly.append(clas.subject)
    return user_friendly

def convert_to_data(user_classes_str: list[str]) -> list[data.Classes]:
    user_classes =[]
    for c in user_classes_str:
        for course in database:
            if course.subject == c:
                user_classes.append(course)
    return user_classes

#def make_combinations_with_units(user_classes: list[data.Classes]): -> list[list[data.Classes]]:
    #unit_verified_classes = []
    #return unit_verified_classes
#def verify_combinations(unit_verified_combinations: list[list[data.Classes]]) -> list[list[data.Classes]:
    #possible_combos = []
    #return possible_combos



def main():
    print("Here are the classes available:", user_data(database))
    user_input = input("Enter classes you would like to take with a space in between each:")
    user_classes_str = user_input.split()
    user_classes = convert_to_data(user_classes_str)
    print(user_classes)
    #unit_verified_classes = make_combinations_with_units(user_classes)
   # possible_combos = verify_combinations(unit_verified_classes)
   # print("Here are the possible combinations of classes you can take:", possible_combos)

main()