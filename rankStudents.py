'''
Read names and marks of at least 3 students
Rank top 3 students with highest marks
Give cash reward $500 for first rank, $300 for second rank, $100 for third rank. Value cannot be modified
Appreciate students who scored 950 marks and above
'''

import operator

def readStudentDetails():
    print()
    print("Enter the number of student: ")
    numberOfStudents = int(input())
    print()
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        name = input()
        print("Enter the marks of the student: ")
        marks = int(input())
        studentRecord[name] = marks
        print()
    return studentRecord

def rankStudents(studentRecord):
    try:
        print()
        sortedStudentRecord = sorted(studentRecord.items(), key=operator.itemgetter(1), reverse=True)  # convert dictionary to list in order to sort
        print(sortedStudentRecord)
        print()
        print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()

def rewardStudents(sortedStudentRecord, reward):
    print()
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    print()

def appreciateStudent(sortedStudentRecord):
    print()
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break
    print()

studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudent(sortedStudentRecord)
