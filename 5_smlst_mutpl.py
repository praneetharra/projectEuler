import math
def isPrimme(a):
	for j in range(2,int(math.sqrt(a))+1):
		if a%j == 0:
			return False
	return True

def largest_pow(p,x):
	req = 1
	c = x
	while c>0 and req<x:
		req = req*p
		c -= 1
	return int(req/p)
	
primes = []
n = 20
for i in range(2,n+1):
	if isPrimme(i):
		primes.append(i)

result = 1
for i in primes:
	result = result * largest_pow(i,n)
	
print(result)
