import random as rnd
import csv, itertools
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

"""
------------------------------------------- Assignment 1.1-1.6 + 1.9 -----------------------------------------
"""

"""
1. Create 3 classes: Student, DataSheet and Course
2. A student has a data_sheet and a data_sheet has multiple courses in particular order
3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
4. In Student create init() so that a Student can be initiated with name, gender, data_sheet 
    and image_url
5. In DataSheet create a method to get_grades_as_list()
6. In student create a method: get_avg_grade()
"""
class Student:

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        grade_sum = 0
        no_of_grades = 0
        for grade in grades:
            if grade is not None:
                no_of_grades += 1
                grade_sum += grade
        return grade_sum/no_of_grades
    
    def get_progression(self):
        """
        Make a method on Student class that can show progression of the study in % 
        (add up ECTS from all passed courses divided by total of 150 total points (equivalent 
        to 5 semesters))
        """
        no_ects = 0
        for course in self.data_sheet.courses:
            if course.grade is not None and course.grade > 0:
                no_ects += course.ECTS
        
        return (no_ects/150)*100
    
    def get_course_list(self):
        return self.data_sheet.courses


class DataSheet:
    
    def __init__(self, courses=None):
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)
    
    def get_grades_as_list(self):
        res = []
        for course in self.courses:
            res.append(course.grade)
        return res

class Course:
    
    def __init__(self, name, classroom, teacher, ECTS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade

    def __repr__(self):
        return 'Course(%r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ECTS, self.grade)


"""
------------------------------------------- Assignment 1.7 -----------------------------------------
"""

def create_random_students():
    """
    Create a function that can generate n number of students with random: name, 
    gender, courses (from a fixed list of course names), grades, img_url
    """
    students = []
    female_names = ['Annika', 'Anina', 'Josefine', 'Linda', 'Shafa']
    male_names = ['Martin', 'Peter', 'Mathias', 'Kasper', 'Jonas']
    first_names = female_names + male_names
    sur_names = ['Hansen', 'Sørensen', 'Jensen', 'Jakobsen']
    genders = ['Male', 'Female']

    pictures = ['https://www.pexels.com/photo/woman-sitting-and-smiling-1858175/',
                'https://www.pexels.com/photo/adult-beard-boy-casual-220453/',
                'https://www.pexels.com/photo/women-s-white-and-black-button-up-collared-shirt-774909/',
                'https://www.pexels.com/photo/man-wearing-black-zip-up-jacket-near-beach-smiling-at-the-photo-736716/',
                'https://www.pexels.com/photo/woman-wearing-black-eyeglasses-1239291/',
                'https://www.pexels.com/photo/photography-of-person-walking-on-road-1236701/',
                'https://www.pexels.com/photo/afterglow-backlit-beautiful-crescent-moon-556666/',
                'https://www.pexels.com/photo/photography-of-a-guy-wearing-green-shirt-1222271/', 
                'https://www.pexels.com/photo/man-young-happy-smiling-91227/',
                'https://www.pexels.com/photo/landscape-nature-africa-boy-103123/']

    courses = create_courses()

    for name in first_names:
        sur_name = rnd.choice(sur_names)

        if name in female_names:
            gender = genders[1]
        else:
            gender = genders[0]

        # Make sure not to reuse picture
        pic = rnd.choice(pictures)
        pictures.remove(pic)

        # Set course
        tmp_courses = courses.copy()
        c = []

        # Used for randomly giving out grades
        grades = [-3, 0, 2, 4, 7, 10, 12, None]
        for i in range(3):
            course = rnd.choice(tmp_courses)
            tmp_courses.remove(course)
            grade = rnd.choice(grades)
            c.append(Course(*course, grade))
        
        data_sheet = DataSheet(c)
        students.append(Student(name + ' ' + sur_name, gender, data_sheet, pic))

    # Write to file
    write_students_to_file(students)   

def write_students_to_file(students):
    """
    Let the function write the result to a csv file with format stud_name, 
    course_name, teacher, ects, classroom, grade, img_url
    """
    with open('Students.csv', 'w', newline='', encoding='UTF-8') as stud_file:
        output_writer = csv.writer(stud_file)
        output_writer.writerow(['Student_name', 'Gender', 'Course', 'Teacher', 'ECTS', 'Classroom', 'Grade', 'image'])
        for s in students:
            for c in s.data_sheet.courses:
                output_writer.writerow([s.name, s.gender, c.name, c.teacher, c.ECTS, c.classroom, c.grade, s.image_url])


def create_courses():
    
    courses = []

    course_names = ['Python', 'Security', 'Adv. Programming', 'Unity', 'JavaScript']
    ects = [5, 10, 15, 20, 25, 30]
    class_rooms = ['101', '102', '103', '104', '105']
    teachers = ['Hans', 'Jens', 'Lars', 'Klausbjerke']


    for name in course_names:
        class_room = rnd.choice(class_rooms)
        teacher = rnd.choice(teachers)
        e = rnd.choice(ects)

        courses.append([name, class_room, teacher, e])

    print(courses)
    return courses

"""
------------------------------------------- Assignment 1.8 -----------------------------------------
"""

def read_student_data():
    """
    Read student data into list of Students from a csv file
    Print students with name, img_url and avg_grade
    Sort the list
    """
    with open('Students.csv', 'r', newline='', encoding='UTF-8') as stud_file:
        students = []
        
        reader = csv.reader(stud_file)
        next(reader) # Header
        for row in reader:
            name, gender, course_name, teacher, ects, classroom, grade, image = row
            if grade != '':
                grade = int(grade)
            else:
                grade = None

            course = Course(course_name, classroom, teacher, int(ects), grade)

            if students and students[-1].name == name:
                students[-1].data_sheet.courses.append(course)
            else:
                data = DataSheet([course])
                student = Student(name, gender, data, image)
                students.append(student)
    
    students.sort(key=lambda x: x.get_avg_grade())
    
    #for s in student:
    #    student_avg = {s.name, s.get_avg_grade()}
    
    return students

def chart_avg_grades():
    """
    Create bar chart wight student_name on x-axis and avg_grade on y-axis
    """
    students = read_student_data()
    avg_grade_map = {}
    for s in students:
        avg_grade_map[s.name] = s.get_avg_grade()
    plt.figure()
    plt.bar(list(avg_grade_map.keys()), list(avg_grade_map.values()), align='center',edgecolor='black')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.show()


"""
------------------------------------------- Assignment 1.10 -----------------------------------------
"""
def chart_progression():
    """
    Show a bar chart of distribution of study progression on x-axis and number of 
    students in each category on y-axis. (e.g. make 10 categories from 0-100%)
    """
    students = read_student_data()
    pr = {
        '0-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0,
        '51-60': 0,
        '61-70': 0,
        '71-80': 0,
        '81-90': 0,
        '91-100': 0
    }

    for s in students:
        p = s.get_progression()
        if p <= 10:
            pr['0-10'] += 1
        elif p > 10 and p <= 20:
            pr['11-20'] += 1
        elif p > 20 and p <= 30:
            pr['21-30'] += 1
        elif p > 30 and p <= 40:
            pr['31-40'] += 1
        elif p > 40 and p <= 50:
            pr['41-50'] += 1
        elif p > 50 and p <= 60:
            pr['51-60'] += 1
        elif p > 60 and p <= 70:
            pr['61-70'] += 1
        elif p > 70 and p <= 80:
            pr['71-80'] += 1
        elif p > 80 and p <= 90:
            pr['81-90'] += 1
        elif p > 90 and p <= 100:
            pr['91-100'] += 1

    print(pr)
    plt.figure()
    plt.bar(list(pr.keys()), list(pr.values()), align='edge', edgecolor='black')
    plt.xticks(horizontalalignment='left', rotation=45)
    plt.yticks(range(1,6,1))
    plt.xlabel('Completion in %')
    plt.ylabel('Number of students')

    plt.show()

chart_progression()