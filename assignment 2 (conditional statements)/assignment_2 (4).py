'''
WAP that has following menu:

- Enter 1 to find out whether the entered number is even or odd
- Enter 2 to find out whether the entered number is positive or negative
'''

choice = int(input("Enter 1 to find out whether the entered number is even or odd\nEnter 2 to find out whether the entered number is positive or negative\n\nPlease enter your choice: "))

if choice == 1:
    num = int(input("\nPlease enter the number: "))
    if num % 2 == 0:
        print("\nThe number is even")
    else:
        print("\nThe number is odd")

if choice == 2:
    num = int(input("\nPlease enter the number: "))
    if num >= 0:
        print("\nThe number is positive")
    else:
        print("\nThe number is negative")


