loop = 0
while loop == 0:
    try:
        age = int(input("Enter the age of the candidate:"))
        loop = 1
    except:
        print("Invalid input")
        loop = 0

if age > 18:
    print("Eligible to vote.")
elif age < 0:
    print("Please enter a positive age.")
else:
    print("Not eligible to vote.")
