import sys

if len(sys.argv) == 6:
    print("USAGE python p1.py <sub1> <sub2> <sub3> <sub4> <sub5>")

    script_name=sys.argv[0]
    sub1=sys.argv[1]
    sub2=sys.argv[2]
    sub3=sys.argv[3]
    sub4=sys.argv[4]
    sub5=sys.argv[5]
    print("user marks")
    else :
        script_name=sys.argv[0]
        sub1="40"
        sub2="70"
        sub3="40"
        sub4="60"
        sub5="10"
        print("no input given default values are given")
        total=sub1+sub2+sub3+sub4+sub5
        average=total/5

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
print("Subject 1:",sub1)
print("Subject 2:",sub2)
print("Subject 3:",sub3)
print("Subject 4:",sub4)
print("Subject 5:",sub5)
print("Total Marks:",total)
print("Average Marks:", average)
print("Grade:", grade)
