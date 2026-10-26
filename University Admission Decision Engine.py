
n = int(input("Enter number of candidates: "))

candidates = []

for i in range(n):
    print("\nCandidate", i + 1)

    name = input("Enter candidate name: ")
    math = float(input("Enter Mathematics marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))

    aggregate = (math + physics + chemistry) / 3

    # Course-specific eligibility
    course = input("Enter course (CSE or ECE): ").upper()

    if course == "CSE":
        eligible = math >= 60 and physics >= 50 and aggregate >= 70
    elif course == "ECE":
        eligible = math >= 50 and physics >= 50 and aggregate >= 60
    else:
        eligible = False

    if eligible:
        candidates.append([
            name, course, aggregate, math, physics, chemistry
        ])

# Rank by aggregate, then Mathematics, then Physics
candidates.sort(
    key=lambda x: (x[2], x[3], x[4]),
    reverse=True
)

print("\n----- RANKED ELIGIBLE CANDIDATES -----")

if len(candidates) == 0:
    print("No eligible candidates found.")
else:
    for rank, candidate in enumerate(candidates, start=1):
        print("\nRank:", rank)
        print("Name:", candidate[0])
        print("Course:", candidate[1])
        print("Aggregate:", round(candidate[2], 2))
        print("Mathematics:", candidate[3])
        print("Physics:", candidate[4])
        print("Chemistry:", candidate[5])
