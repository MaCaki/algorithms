import sys
data = sys.stdin.readlines()
          
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def reduce_fraction(numerator, denominator):
    p = gcd(numerator, denominator)
    return numerator/p , denominator/p

for line in data:
    r = [int(x) for x in line.split()]
    if len(r) < 3: continue
    A,B,C  = min(r[0],r[1]), max(r[1],r[0]), r[2]
    
    denom = 2 * A * B
    #cases 
    if C < 0: 
        print("0/1")
        continue
    
    if C >= A + B:
        print("1/1")
        continue
        
    if C <= A: 
        num = C**2
    elif A < C <= B:
        num = (2 * A * (C - A)) + A**2    
    else:
        num = 2 * A * B - (A + B - C)**2
  
    num, denom = reduce_fraction(num, denom)
    print('%d/%d' % (num, denom))