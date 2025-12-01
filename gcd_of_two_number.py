x=7
y=14
gcd=0
for i in range(1,min(x,y)+1): # we use min because GCD cannot be larger than the smallest number

    if x%i==0 and y%i==0:
        gcd=i  # if the condition satisfy i will be stored in gcd 

print(gcd)