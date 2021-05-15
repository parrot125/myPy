num = int(input("Enter a number: "))
a = "{} is a Prime number".format(num)
for i in range(2, num):
    if (num % i) == 0:
        a = "{} is not a Prime Number".format(num)
        break
    else:
        pass
print(a)
