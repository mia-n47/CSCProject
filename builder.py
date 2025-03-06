import data
from itertools import combinations
from datetime import datetime

database = [data.Classes("CSC101", "TUETHU","8 am", "11am",4),
            data.Classes("PHYS143", "TUETHU", "1 pm", "3pm",4),
            data.Classes("MATH244", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("COMS101", "TUETHU","12pm", "2pm",4),
            data.Classes("ENGL145", "WEDFRI", "11am", "1pm",4),
            data.Classes("CHEM124", "MONWED", "6pm", "9pm",4),
            data.Classes("EE111", "FRI", "9am", "10am",1),
            data.Classes("ENGL134", "MONWEDFRI", "4pm", "6pm",4),
            data.Classes("EE151", "TUE", "8 am", "11 am",1),
            data.Classes("PHYS141", "MONTUETHUFRI", "5pm", "6pm",4),
            data.Classes("MATH241", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("MATH142", "MONTUETHUFRI", "9am", "10am",4),
            data.Classes("MATH141", "MONTUETHUFRI", "7am", "8am",4),
            data.Classes("ES256", "TUETHU", "8am", "10am",4),
            data.Classes("PHYS142", "WEDFRI", "2pm","4pm",4),
            data.Classes("AERO220", "TUE", "3pm", "6pm",4),
            data.Classes("AERO299", "MONWEDFRI", "12pm", "1pm",4),
            data.Classes("AG413", "TUE", "11am", "12pm",2),
            data.Classes("AG581", "THU", "2pm", "3pm",2),
            data.Classes("ARCE315", "MONWED", "10am", "12pm",4),
            data.Classes("ARCE354", "TUE","8am", "11am",2),
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

def make_combinations_with_units(user_classes: list[data.Classes]) -> list[list[data.Classes]]:
    unit_verified_classes = []
    for r in range(1, len(user_classes)+1):
        for combo in combinations(user_classes,r):
            #r is the number of elements in the lists, therefore this function goes through a variety of list lengths
            #user_classes is the list it is pulling from
            total_units = sum(course.units for course in combo)
            if 12<=total_units<=22:
                unit_verified_classes.append(list(combo))
    return unit_verified_classes

# converts a time string into a datetime object for easier comparison
def analyze_time(time_str: str) -> datetime:
    return datetime.strptime(time_str.replace(" ", ""), "%I%p") # tells python hour in 12 hr format and AM/PM

# sorts classes by their start time to help with organization
def sort_classes_by_time(classes: list[data.Classes]) -> list[data.Classes]:
    # Create a list of start times and their corresponding classes
    class_times = []
    for c in classes:
        start_time = analyze_time(c.start_time)
        class_times.append((start_time, c))  # Store the start time with the class
    class_times.sort(key=get_start_time)
    sorted_classes = []
    for _, c in class_times:
        sorted_classes.append(c)

    return sorted_classes

def get_start_time(class_tuple):
    # This function returns the start time from a tuple (start_time, class)
    return class_tuple[0]


# checks if two classes overlap based on their days and times
def classes_overlap(class1: data.Classes, class2: data.Classes) -> bool:
    days_overlap = any(day in class2.days for day in class1.days)
    if not days_overlap:
        return False
    start1, end1 = analyze_time(class1.start_time), analyze_time(class1.end_time)
    start2, end2 = analyze_time(class2.start_time), analyze_time(class2.end_time)
    return max(start1, start2) < min(end1, end2)

# filters out class combinations that have scheduling conflict
def verify_combinations(unit_verified_combinations: list[list[data.Classes]]) -> list[list[data.Classes]]:
    possible_combos = []
    for combo in unit_verified_combinations:
        if all(not classes_overlap(c1, c2) for i, c1 in enumerate(combo) for c2 in combo[i+1:]):
            possible_combos.append(combo) # only adds valid schedules
    return possible_combos


def main():
    print("Here are the classes available:", user_data(database))
    user_input = input("Enter classes you would like to take with a space in between each:")
    user_classes_str = user_input.split()
    user_classes = convert_to_data(user_classes_str)
    sorted_classes = sort_classes_by_time(user_classes)
    unit_verified_classes = make_combinations_with_units(sorted_classes)
    possible_combos = verify_combinations(unit_verified_classes)
    print("Here are possible combinations of classes you can take:", possible_combos)

main()