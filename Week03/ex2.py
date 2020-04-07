"""
Ex 2 Exceptions
1. Create a function that can take a list of students and return the 3 students closest to completing their study.
2. If list is shorter than 3 raise your own custom exception (NotEnoughStudentsException)
3. Create another function that can create a csv file with 3 students closest to completion
 a) If an exception is raised write an appropriate message to the file
"""

import ex1
import csv

"""
------------------------------------------- Assignment 2.1 -----------------------------------------
"""


def students_closest_to_finishing(students):
    """
    Create a function that can take a list of students and return the 3 students closest to completing their study.
    Raise exception if list is shorter than 3
    """
    if len(students) < 3:
        raise NotEnoughStudentsException("Should be 3 or more students in list")

    # Creating temporary list so that I don't sort the input list
    tmp = sorted(students, key=lambda s: s.get_progression(), reverse=True)

    return tmp[:3]


"""
------------------------------------------- Assignment 2.2 -----------------------------------------
"""


class NotEnoughStudentsException(IndexError):
    def __init__(self, *args, **kwargs):
        IndexError.__init__(self, *args, **kwargs)


"""
------------------------------------------- Assignment 2.3 -----------------------------------------
"""


def write_to_file(students):
    """
    Create another function that can create a csv file with 3 students closest to completion
    If an exception is raised write an appropriate message to the file
    """
    with open(
        "students_closest_to_finishing.csv", "w", newline="", encoding="UTF-8"
    ) as stud_file:
        output_writer = csv.writer(stud_file)
        try:
            tmp = students_closest_to_finishing(students)
        except NotEnoughStudentsException as e:
            stud_file.write(str(e))
        else:
            output_writer.writerow(["Student_name", "Gender", "Progression", "image"])
            for s in tmp:
                output_writer.writerow(
                    [s.name, s.gender, s.get_progression(), s.image_url]
                )


write_to_file(ex1.read_student_data())
