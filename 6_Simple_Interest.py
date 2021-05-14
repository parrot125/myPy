p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years): "))

intrst = p*r*t/100

print("The simple interest is", intrst, "units",
      "and amount is", p+intrst, "units")
