import math
import time
def isPrimme(a):
	for j in range(2,int(math.sqrt(a))+1):
		if a%j == 0:
			return False
	return True

def primes(n):
	for i in range(2,n):
		if isPrimme(i):
			yield i
			
sums = 0
n = 2000000
for num in primes(n):
	sums += num

start = time.time()
print(sums)
print(time.time()-start)
