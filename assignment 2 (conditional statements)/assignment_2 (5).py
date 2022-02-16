'''
WAP that implements the simple calculator that has following menu:

- Enter 1 to find the addition of two numbers
- Enter 2 to find the substraction of two numbers
- Enter 3 to find the multiplication of two numbers
- Enter 4 to find the division of two numbers
- Enter 5 to find the inverse of a number
- Enter 6 to find the square of a number
- Enter 7 to find the cube of a number
'''

choice = int(input("Enter 1 to find the addition of two numbers\nEnter 2 to find the substraction of two numbers\nEnter 3 to find the multiplication of two numbers\nEnter 4 to find the division of two numbers\nEnter 5 to find the inverse of a number\nEnter 6 to find the square of a number\nEnter 7 to find the cube of a number\n\nPlease enter your choice: "))

if choice == 1 or choice == 2 or choice == 3 or choice == 4:
    num1 = float(input("\nPlease enter num 1: "))
    num2 = float(input("Please enter num 2: "))
    print("\n")
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)

if choice == 5 or choice == 6 or choice == 7:
    num = int(input("\nPlease enter the number: "))
    print("\n")
    if choice == 5:
        print("1/",num, " = ", 1/num)
    elif choice == 6:
        print(num ** 2)
    elif choice == 7:
        print(num ** 3)
