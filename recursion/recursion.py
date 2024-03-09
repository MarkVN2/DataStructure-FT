# recursion is a powerfull tool that we can use to optimize functions
# usually functions with recursion will look like this
# function x(A):
#   if "A too small" return resp
#   return function x with A decreased

def pot(a,n):
    if n <= 0 : return 1 
    return pot(a,n-1) * a 

def fat(a):
    if a == 0 : return 1
    return fat(a-1) * a 

def inv(s):
    if len(s) <= 1: return s
    return inv(s[1:]) + s[0]

def mdc(a,b):
    if a % b == 0: return b
    return mdc(b, a%b)

def dec2bin(n):
    if n == 0 : return ''
    return dec2bin(n//2) + str(n%2) 


# --testing

print(pot(2,5)) # 32 
print(dec2bin(16)) # 10000
print(fat(5)) # 120
print(mdc(3,12)) # 3
print(inv('inverted')) # detrevni