import sys

if len(sys.argv) == 6:
    print("User provided marks through command line:")

    marks = [
        float(sys.argv[1]),
        float(sys.argv[2]),
        float(sys.argv[3]),
        float(sys.argv[4]),
        float(sys.argv[5])
    ]
else:
    print("No input given - using default marks:")

    marks = [85, 78, 92, 74, 88]

average = sum(marks) / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Print results
print("\n--- Student Result ---")
print("Marks:", marks)
print("Average Marks:", average)
print("Grade:", grade)
