from math import sqrt as rt
print("This program will calculate the roots of quadratic equation of the form ax\u00b2+bx+c")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))


def root(a, b, c):
    r1 = (-b+rt((b**2)-(4*a*c)))/2*a
    r2 = (-b-rt((b**2)-(4*a*c)))/2*a

    return "{r1} and {r2}".format(r1=r1, r2=r2)


print("The required roots are {}".format(root(a, b, c)))
