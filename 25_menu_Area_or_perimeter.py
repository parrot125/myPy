menu = str(input("Please enter A for AREA and P for PERIMETER: "))
if menu == "A":
    r = int(input("Enter the radius of the circle: "))
    print("The area of the circle is {area} unit\ub002.".format(
        area=round(3.14*r*r, 2)))
elif menu == "P":
    r = int(input("Enter the radius of the circle: "))
    print("The perimeter of the circle is {perimeter} units.".format(
        perimeter=round(2*3.14*r, 2)))
else:
    print("Invalid input, please run the program again.")
