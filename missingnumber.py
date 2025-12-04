arr=[1,2,4,5] # A array with missing value
n=5 # taking a max number in array
excepted=n*(n+1)//2        # math logic
total=0
for i in range(0,len(arr)):
    total+=arr[i]         # getting the sum of all values in array
missing=excepted-total    # excepted-total =missing
print(missing)