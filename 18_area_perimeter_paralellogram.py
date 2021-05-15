# Defining the functions for perimeter and area
def peri(base, width):
    return 2*(base+width)


def area(base, height):
    return base*height


# Taking input from user
b = int(input("Enter the base of the parallelogram: "))
h = int(input("Enter the height of the parallelogram: "))
w = int(input("Enter the width of the parallelogram: "))

# Printing the output
print("The area of the paralellogram is", area(b, h),
      "units\u00b2 and the perimeter is", peri(b, w), "units")
