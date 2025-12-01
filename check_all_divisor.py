""" learn about class and object then you can clearly understand"""

class Solution:
    def divisor(self,n):
        result=[] # empty list 
        for i in range(1,n+1):
            if n%i==0:
                result.append(i) # append will add all divisor to that empty list 
        return result

ans=Solution()
print(ans.divisor(10))  