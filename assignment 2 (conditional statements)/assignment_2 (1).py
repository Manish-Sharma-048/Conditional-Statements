
'''
The marks obtained by a student in 5 different subjects are input through keyboard. The student gets the division as per the following rules:

- Percentage above or equal to 60 - first division
- Percentage between 50 and 59 - second division
- Percentage between 40 and 49 - third division
- Percentage below 40 - fail.
'''

marks1 = int(input("Please enter marks obtained in subject 1: "))
marks2 = int(input("Please enter marks obtained in subject 2: "))
marks3 = int(input("Please enter marks obtained in subject 3: "))
marks4 = int(input("Please enter marks obtained in subject 4: "))
marks5 = int(input("Please enter marks obtained in subject 5: "))

per = float((marks1 + marks2 + marks3 + marks4 + marks5)/5)

if per >= 60:
    print("\nTotal Percentage: ", per,"(First Division)")
elif per > 50 and per < 59:
    print("\nTotal Percentage: ", per,"(Second Division)")
elif per > 40 and per < 49:
    print("\nTotal Percentage: ", per,"(Third Division)")
else:
    print("\nTotal Percentage: ", per,"(Fail)")
