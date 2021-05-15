n = int(input("Enter a number: "))
pd = 1
for i in range(1, n+1):
    pd = pd*i
print("{0}! = {1}".format(n, pd))
