'''
WAP that has following menu:

- Enter 1 to find the area of Rectangle
- Enter 2 to find the area of Circle

Values for length and width of a rectangle and value of a radius of circle will be entered through keyboard.
'''

choice = int(input("Enter 1 to find the area of Rectangle\nEnter 2 to find the area of Circle\n\nPlease enter your choice: "))

if choice == 1:
    l = float(input("\nPlease enter the length (in meters): "))
    w = float(input("Please enter the width (in meters): "))
    print("\n The Area of Rectangle is: ", l*w)
elif choice == 2:
    r = float(input("\nPlease enter the radius: "))
    print("\nThe Area of Circle is: ", 3.14*r*r) 
else:
    print("Invalid choice")
