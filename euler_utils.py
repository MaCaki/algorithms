import timeit
import time
import numpy as np

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print( '%s function took %0.3f s' % (f.func_name, (time2-time1)))
        return ret
    return wrap


### an efficient algorithm for calculating a^x % p  

@timing
def moduloPowerOpt(a, x, p):
    ans = 1
    prod = a
    exp = x
    while (exp > 0):
        if exp&1:
            ans = (ans*prod)%p
        
        exp = exp>>1
        prod = (prod*prod)%p
    return ans
            
def powerEff(a,m):
    ans = 1
    prod = a
    exp = m
    while (exp > 0):
        if exp&1:
            ans *= prod
        
        exp = exp>>1
        print (exp)
        prod = prod*prod
    
    return ans

def primesLessThan(n):
    if n == 1: 
        yield None
        
    l = [True]*n
    l[0] = l[1] = False
    for (p, isPrime) in zip(range(n), l):
        if isPrime:
            yield int(p)
            for i in range(p*p,n,p):
                l[i] = False
        
