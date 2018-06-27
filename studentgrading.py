def gradingStudents(grades):
    print(grades)
    for i, value in enumerate(grades):
        if (value < 38):
            grades[i] = value
        elif ((int(value / 10) * 10 + 10) - value) < 3 and ((int(value / 10) * 10 + 10) - value) > 0:
            grades[i] = int(value / 10) * 10 + 10
        elif ((int(value / 10) * 10 + 5) - value) < 3 and ((int(value / 10) * 10 + 5) - value) > 0:
            grades[i] = int(value / 10) * 10 + 5
    return grades


if __name__ == '__main__':
    n = int(raw_input())
    grades = []
    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)
