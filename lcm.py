# lcm of 2 number
x=2
y=7
lcm=max(x,y) # need max for checking
while True:
    if lcm % x==0 and lcm % y==0: # checking that max
        break
    lcm+=1 # until we found lcm we have to +=1 the lcm
print(lcm)
