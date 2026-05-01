#1. Grade Checker
#Take a score as input and print the grade based on the following:
#90+ : "A"
#80-89 : "B"
#70-79 : "C"
#60-69 : "D"
#Below 60 : "F"
#here we used a basic if else statement to carry out marks and all.

score = float(input("enter score"))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")