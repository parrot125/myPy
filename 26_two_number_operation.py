a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = str(input("Enter the arithmetic operator: "))

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "/":
    print(round(a/b, 2))
elif c == "*":
    print(a*b)
else:
    print("Invalid mathematical operation")
