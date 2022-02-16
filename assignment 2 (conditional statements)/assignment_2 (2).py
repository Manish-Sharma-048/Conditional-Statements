'''
Admission to professional course in a college according to following conditions:

- Marks in mathematics are greater than or equal to 60 and marks in Physics is greater than or equal to 50 and marks in Chemistry is greater than or equal to 40
OR
- Total marks in mathematics and physics are greater than or equal to 150
OR
- Total marks in mathematics, physics and chemistry is greater than or equal to 200
'''

maths = int(input("Please enter the marks obtained in Mathematics: "))
phy = int(input("Please enter the marks obtained in Physics: "))
chem = int(input("Please enter the marks obtained in Chemistry: "))

q = "\nCongratulation! you are qualified for the admission."

if maths >= 60 and phy >= 50 and chem >= 40:
    print(q)
elif (maths + phy >= 150):
    print(q)
elif (maths + phy + chem >= 200):
    print(q)    
else:
    print("\nThe details you have shared with us doesn't meet the required admission criterias.")
