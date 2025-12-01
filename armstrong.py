'''An Armstrong number is a number that is equal to the sum of its own digits
 raised to the power of the number of digits.'''

n=153
temp=n                                # store in temp 

# step 1 count digits
digits=0                              # store number of digit in digits
while temp>0:
    digits+=1
    temp=temp//10


#  step 2  armstrong logic

sum_digit=0
temp=n                    # store again in temp because in previous temp becomes 0 because of while loop so again we use temp
while temp>0:
    digit=temp%10                    # get last digit in digit
    sum_digit+=digit**digits          # use that last digit square with previous digits(code 10 line) and store in sum_digits
    temp//=10                             # remove last digit 

if sum_digit==n:

    print("ARMSTRONG")

else:
    print("Not armstrong")

