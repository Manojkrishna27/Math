""" Why?
First digit → 1 to 9 → 9 choices
Remaining (K-1) digits → 0 to 9 → 10 choices each"""
k=3
count=9*(10**(k-1)) # direct formula
print(count)