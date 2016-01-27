import sys

nums = map(int, raw_input().split())
x = nums[0]
y = nums[1]
z = nums[2]
n = x + y + z
four_counts = [ 0 for t in range(n)]
five_counts = [ 0 for t in range(n)]
six_counts = [ 0 for t in range(n)]

P = 1000000007

def cumulativeAdd(array, num, end):
    for l in range(end):
        array[l] += num

def moduloPower(a, x, p):
    # computes a^x (mod p)
    ans = 1
    prod = a
    exp = x
    while (exp > 0):
        if exp&1:
            ans = (ans*prod)%p
        
        exp = exp>>1
        prod = (prod*prod)%p
    return ans

multiset_perms_eff = [[[ 0 for t in range(z+1)] for t in range (y+1)] for t in range(x+1)]

for i in range(x + 1):
    multiset_perms_eff[i][0][0] = 1
for i in range(y + 1):
    multiset_perms_eff[0][i][0] = 1
for i in range(z + 1):
    multiset_perms_eff[0][0][i] = 1

for i in range(1, x + 1):
    for j in range(1, y + 1 ):
        multiset_perms_eff[i][j][0] += (multiset_perms_eff[i-1][j][0] + multiset_perms_eff[i][j-1][0] )%P

for j in range(1, y + 1):
    for k in range(1, z + 1 ):
        multiset_perms_eff[0][j][k] += (multiset_perms_eff[0][j][k-1] + multiset_perms_eff[0][j-1][k] )%P


for i in range(1, x + 1):
    for k in range(1, z + 1 ):
        multiset_perms_eff[i][0][k] += (multiset_perms_eff[i][0][k-1] + multiset_perms_eff[i-1][0][k] )%P 




for i in range(1, x + 1):
    for j in range(1, y + 1):
        for k in range(1, z + 1):
            multiset_perms_eff[i][j][k] += (multiset_perms_eff[i-1][j][k] + multiset_perms_eff[i][j-1][k] + multiset_perms_eff[i][j][k-1])%P


## Accumulate digit occurances 

for i in range(1,x + 1): 
    for j in range(y + 1): 
        for k in range(z + 1): 
            cumulativeAdd(four_counts, multiset_perms_eff[i-1][j][k], i + j + k)

for i in range(x + 1): 
    for j in range(1,y + 1): 
        for k in range(z + 1):
             cumulativeAdd(five_counts, multiset_perms_eff[i][j-1][k], i + j + k)

for i in range(x + 1): 
    for j in range(y + 1):
        for k in range(1, z + 1):
             cumulativeAdd(six_counts, multiset_perms_eff[i][j][k-1], i + j + k)


totals = [ 0 for t in range(n)]
for i in range(n):
     totals[i] = (4*four_counts[i] + 5*five_counts[i] + 6*six_counts[i])%P



sum = 0  
for i in range(n):
    sum += totals[i]*moduloPower(10,i,P)
sum = sum%P
sys.stdout.write(str(sum))

