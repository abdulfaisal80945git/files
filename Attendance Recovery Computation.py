total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
threshold = float(input("Enter eligibility percentage: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = attended / total * 100
    print("Current Attendance:", round(percentage, 2), "%")

    if percentage >= threshold:
        print("You are already eligible.")
    else:
        needed = 0
        while (attended + needed) / (total + needed) * 100 < threshold:
            needed += 1

        print("Consecutive classes to attend:", needed)

    print("\nFuture Attendance Scenarios:")
    for future in [5, 10, 20]:
        new_percentage = (attended + future) / (total + future) * 100
        print(f"After attending {future} classes: "
              f"{new_percentage:.2f}%")
