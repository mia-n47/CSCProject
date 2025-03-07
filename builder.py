import data
from itertools import combinations
from datetime import datetime
import courses


#This function takes the data from database, and converts it to a more readable variation to present to the user.
def user_data(d: list[data.Classes]) -> list[str]:
    user_friendly = []
    for clas in d:
        user_friendly.append(clas.subject)
    return user_friendly


#This function takes a list of strings and converts it to classes Objects.
def convert_to_data(user_classes_str: list[str]) -> list[data.Classes]:
    user_classes =[]
    for c in user_classes_str:
        for course in courses.database:
            if course.subject == c:
                user_classes.append(course)
    return user_classes

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


# This function verifies that the sum of the combinations is within a valid unit range.
def make_combinations_with_units(user_classes: list[data.Classes]) -> list[list[data.Classes]]:
    unit_verified_classes = []
    for r in range(1, len(user_classes)+1):
        for combo in combinations(user_classes,r):
            #r is the number of elements in the lists, therefore this function goes through a variety of
            #list lengths user_classes is the list it is pulling from
            total_units = sum(course.units for course in combo)
            if 15<=total_units<=20:
                unit_verified_classes.append(list(combo))
    return unit_verified_classes

# This function returns the start time from a tuple (start_time, class)
def get_start_time(class_tuple):
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


# Makes the final display of classes more user-friendly, by only presenting the subject of the classes.
def user_friendly_final(possible_combos: list[list[data.Classes]]) -> list[list[str]]:
    final_combos =[]
    for l in possible_combos:
        new_user_combo =[]
        for c in l:
            new_user_combo.append(c.subject)
        final_combos.append(new_user_combo)
    return final_combos

# this functions makes a dictionary to display information about the combination of classes the user has selected
def display_extra_info(course: data.Classes) -> dict:
    info_dict = {"Subject:":course.subject, "Days:":course.days, "Start Time:":course.start_time,
                 "End Time:":course.end_time, "Units:":course.units}
    return info_dict

def main():
    print("Here are the classes available:", user_data(courses.database))
    print()
    user_input = input("Enter classes you would like to take with a space in between each:")
    print()
    user_classes_str = user_input.split()
    user_classes = convert_to_data(user_classes_str)

    sorted_classes = sort_classes_by_time(user_classes)

    unit_verified_classes = make_combinations_with_units(sorted_classes)

    possible_combos = verify_combinations(unit_verified_classes)
    final_combos = user_friendly_final(possible_combos)
    if len(final_combos) == 0:
        print("There are no possible combinations that include those classes")
        print()
    else:
        print("Here are possible combinations of classes you can take:")
        for r in range(0,len(final_combos)-1):
            print(r,final_combos[r])
        print()

    idx = input("If you would like more information about a specific combination, enter the number to the left of it,"
                "if you would like to re-enter classes, type RESET")
    if idx != "RESET":
        idx = int(idx)
        combo_info = possible_combos[idx]
        for course in combo_info:
            print(display_extra_info(course))
    elif idx == "RESET":
        main()


main()