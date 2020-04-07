import matplotlib.pyplot as plt
import ex1
import numpy as np


def show_pie_chart(students):
    """
    Create a function that can take a list of students and 
    show a pie chart of how students are distributed in ECTS percentage categories (10%, 20%, ...)
    """
    pr = {
        "0-10%": 0,
        "11-20%": 0,
        "21-30%": 0,
        "31-40%": 0,
        "41-50%": 0,
        "51-60%": 0,
        "61-70%": 0,
        "71-80%": 0,
        "81-90%": 0,
        "91-100%": 0,
    }

    for s in students:
        p = s.get_progression()
        if p <= 10:
            pr["0-10%"] += 1
        elif p > 10 and p <= 20:
            pr["11-20%"] += 1
        elif p > 20 and p <= 30:
            pr["21-30%"] += 1
        elif p > 30 and p <= 40:
            pr["31-40%"] += 1
        elif p > 40 and p <= 50:
            pr["41-50%"] += 1
        elif p > 50 and p <= 60:
            pr["51-60%"] += 1
        elif p > 60 and p <= 70:
            pr["61-70%"] += 1
        elif p > 70 and p <= 80:
            pr["71-80%"] += 1
        elif p > 80 and p <= 90:
            pr["81-90%"] += 1
        elif p > 90 and p <= 100:
            pr["91-100%"] += 1

    res = {}
    for key in pr:
        if pr.get(key) != 0:
            res[key] = pr.get(key)

    plt.pie(res.values(), labels=res.keys(), autopct="%1.1f%%")
    plt.axis("equal")
    plt.show()


def bar_chart_courses(students):
    """
    create a function that can take a list of students and show how many students have taken each 
    course (bar chart)
    a) create a method on student that can return a list of courses
    """
    courses = {
        "Python": 0,
        "Security": 0,
        "Adv. Programming": 0,
        "Unity": 0,
        "JavaScript": 0,
    }

    for s in students:
        print(s.get_progression())
        s_courses = s.get_course_list()

        for course in s_courses:
            courses[course.name] += 1

    plt.figure()
    plt.bar(
        list(courses.keys()), list(courses.values()), align="edge", edgecolor="black"
    )
    plt.xticks(horizontalalignment="left", rotation=45)
    plt.show()


def course_chart_gender(students):
    """
    make the figure show males and females in different colors for each course (display 2 datasets in same figure)
    """
    females = {
        "Python": 0,
        "Security": 0,
        "Adv. Programming": 0,
        "Unity": 0,
        "JavaScript": 0,
    }

    males = {
        "Python": 0,
        "Security": 0,
        "Adv. Programming": 0,
        "Unity": 0,
        "JavaScript": 0,
    }

    for s in students:
        s_courses = s.get_course_list()
        for course in s_courses:
            if s.gender == "Female":
                females[course.name] += 1
            else:
                males[course.name] += 1

    print(males)
    print(females)

    xpos = np.arange(len(males.values()))
    plt.figure()
    plt.xticks(xpos, males.keys())
    plt.bar(
        xpos - 0.2, list(females.values()), width=0.4, color="pink", edgecolor="red"
    )
    plt.bar(
        xpos + 0.2, list(males.values()), width=0.4, color="blue", edgecolor="black"
    )
    plt.xticks(horizontalalignment="left", rotation=-45)
    plt.show()


course_chart_gender(ex1.read_student_data())

# show_pie_chart(ex1.read_student_data())
# bar_chart_courses(ex1.read_student_data())

