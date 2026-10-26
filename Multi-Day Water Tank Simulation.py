
capacity = float(input("Enter tank capacity: "))
level = float(input("Enter initial water level: "))
threshold = float(input("Enter target water level: "))
n = int(input("Enter number of intervals: "))

if capacity <= 0 or level < 0 or level > capacity:
    print("Invalid tank capacity or initial level.")

elif threshold < 0 or threshold > capacity or n <= 0:
    print("Invalid threshold or number of intervals.")

else:
    reached = False

    for i in range(1, n + 1):
        inflow = float(input("Enter inflow: "))
        outflow = float(input("Enter outflow: "))

        if inflow < 0 or outflow < 0:
            print("Invalid quantities. Enter positive values.")
            continue

        level = level + inflow - outflow

        if level > capacity:
            print("Interval", i, ": Overflow detected!")
            level = capacity

        elif level < 0:
            print("Interval", i, ": Water shortage detected!")
            level = 0

        print("Water level:", level)

        if not reached and level >= threshold:
            print("Threshold first reached at interval:", i)
            reached = True

    if not reached:
        print("Threshold was not reached.")

    print("Final water level:", level)
