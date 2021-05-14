n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
n3 = int(input("Enter the third integer: "))

if n1 > n2 and n1 > n3:
    print("The greatest number is", n1)
elif n2 > n3 and n2 > n1:
    print("The greatest number is", n2)
else:
    print("The greatest number is", n3)
