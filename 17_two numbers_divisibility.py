def rem(n1, n2):
    if n1 % n2 == 0:
        return "are"
    else:
        return "are not"


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("The two numbers", rem(x, y), "divisible with each other.")
