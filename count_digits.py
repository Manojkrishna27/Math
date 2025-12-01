count=0
n=140
while n>0:
    count+=1
    n=n//10 # this is floor division we use 10 for removing last digits
print(count)