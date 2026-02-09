n=310
total=0
while n>0:
    last=n%10
    total+=last
    n//=10
print(total)
