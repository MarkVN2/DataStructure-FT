# We can use data to optimize recursions like this one

# not optimized
def fibun(n):
    if n <= 2 : return 1
    return fibun(n-1) + fibun(n-2)

# print(fibun(100)) 
# this will take a long time to give any response

#optimized with dictionary
d = {}
def fib(n):
    if n <=2: return 1
    if n not in d:
        d[n] = fib(n-1) + fib(n-2)
    return d[n]

print(fib(100)) #354224848179261915075 
# this one gives a insta response

# by using the dictionary to save already done equations 
# we avoid doing repeated equations making the function faster


# optimized with the functools library
from functools import lru_cache

@lru_cache(maxsize=None)
def fiblru(n):
    if n <= 2 : return 1
    return fiblru(n-1) + fiblru(n-2)

print(fiblru(200)) #280571172992510140037611932413038677189525
# this also gives an instantaneous response
# this method gives the function a cache that keeps data for a while to be reused