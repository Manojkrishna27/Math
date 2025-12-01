# method 1 logic 
num=13
rev=0
while num>0:
    digits=num%10 # this % is storing num's last digits
    rev=rev*10+digits
    num=num//10 # this floor division is remove the last digits
print(rev)

# method 2 slicing 
n=input() # input() string data type 
rev=int(n[::-1]) # so that we  used explict type conversion  and reversing it
print(rev)