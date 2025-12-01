n=5
isprime=True
if n<=1: # 1 and less than 1 is not a prime number 1 is unique number and less than 1 is negative number
    isprime=False   
else:
    i=2
    while i*i<=n:  # Loop from i = 2 up to sqrt(n)
        if n%i==0:    # If n is divisible by i then not a prime 
            isprime=False
            break    # exit the condition 
        i+=1         # and moves to next number
if (isprime):
    print(n,"is a prime")
else:
    print(n,"is a not prime")