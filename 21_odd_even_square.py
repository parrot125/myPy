from math import sqrt
no = int(input("Enter a number: "))


def oddeven(n):
    return n % 2


if oddeven(no) == 1:
    print(no**2)
else:
    print(sqrt(no))
