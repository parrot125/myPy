c = input("Enter a character: ")

if len(c) == 1:
    if c.isdigit():
        print("{} is a digit.".format(c))

    elif c.isupper():
        print("{} is an uppercase letter.".format(c))

    elif c.islower():
        print("{} is an lowercase letter.".format(c))

    elif c.isnumeric:
        print("{} is a mathematical operator.".format(c))
    else:
        pass
else:
    print("Please enter a Single character.")
