n = int(input("Enter number of subjects: "))
marks = []
grace = 5
maximum = 100

for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))

    if m < 0 or m > maximum:
        print("Invalid marks!")
        exit()

    if m < 35 and 35 - m <= grace:
        m = 35
        print("Grace marks applied")

    marks.append(m)

print("\nFinal Marks:", marks)

if all(m >= 35 for m in marks):
    total = sum(marks)
    percentage = total / n

    if percentage >= 75:
        result = "Distinction"
    elif percentage >= 60:
        result = "First Class"
    elif percentage >= 50:
        result = "Second Class"
    else:
        result = "Pass"

    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Classification:", result)
else:
    print("Classification: Fail")
