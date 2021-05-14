loop = 0
while loop == 0:
    n = int(input("Enter the number: "))
    rem = n % 2
    if n < 0:
        print("Please enter a whole number.")
        pass
    elif rem == 0:
        print("The number is even.")
        loop = 1
    elif rem == 1:
        print("The number is odd.")
        loop = 1
