sum = 0
for i in range(1, 8):
    sum = sum+i
    print("{prev} + {i} = {sum}".format(prev=sum-i, i=i, sum=sum))
