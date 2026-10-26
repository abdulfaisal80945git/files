
n = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")

    total1 = 0
    total2 = 0
    weak_count = 0

    for j in range(subjects):
        print("Subject", j + 1)
        exam1 = float(input("Enter Exam 1 marks: "))
        exam2 = float(input("Enter Exam 2 marks: "))

        total1 += exam1
        total2 += exam2

        change = exam2 - exam1

        if change > 0:
            print("Improvement:", change)
        elif change < 0:
            print("Decline:", abs(change))
        else:
            print("No change")

        if exam1 < 40 and exam2 < 40:
            weak_count += 1

    avg = total2 / subjects

    print("\nStudent Name:", name)
    print("Exam 1 Total:", total1)
    print("Exam 2 Total:", total2)
    print("Overall Improvement:", total2 - total1)
    print("Consistently Weak Subjects:", weak_count)

    if avg >= 75:
        print("Classification: Excellent")
    elif avg >= 60:
        print("Classification: Good")
    elif avg >= 40:
        print("Classification: Average")
    else:
        print("Classification: Poor")
