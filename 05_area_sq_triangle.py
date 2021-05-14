loop = 0
while loop == 0:
    shape = str(input("Enter 't' for triangle and 's' for square: "))
    if shape == "t":
        print("triangle")
        print("You have selected triangle.")
        b = int(input("Enter the Base of the triangle: "))
        h = int(input("Enter the Height of the triangle: "))
        area = 0.5*b*h
        print("The area of the triangle is ", area)
        loop = 1
    elif shape == "s":
        print("You have selected square")
        side = int(input("Side of square: "))
        print("The area of the square is", side**2, "sq units")
        loop = 1
    else:
        print("Invalid input please try again (s/t)")
        pass
