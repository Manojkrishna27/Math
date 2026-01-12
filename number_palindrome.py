''' palindorme is nothing but checking a datatype which is equal to its reverse 
if reverse == original it is known as palindrome '''

# method 1 using logic 
num=121
temp=num                 # store num in temp because after the while loop num becomes 0 so store the value in temp
rev=0

while num>0:
    digits=num%10        # we use modulus for getting last digits
    rev=rev*10+digits
    num//=10           # floor division is removing last digits

if temp==rev:             # check  the temp equal to rev 
    print("palindrome")
else:
    print("not")



# method 2 slicing
num=input()

temp=int(num)               # store num in temp because input() take input as a string so type conversion 

rev=int(num[::-1])            # here we slicing the num and convert to int 

if temp==rev:                 # checking equals
    print("palindrome")
else:
    print("not")