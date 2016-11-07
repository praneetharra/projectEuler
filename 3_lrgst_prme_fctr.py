import math
def isPrimme(a):
	for i in range(2,int(math.sqrt(a))):
		if a%i == 0:
			return False
	return True
	
primes = []
n = 600851475143
if not isPrimme(n):
	for i in range(1,int(math.sqrt(n))):
		if n%i == 0:
			if isPrimme(i):
				primes.append(i)
			if isPrimme(int(n/i)):
				primes.append(int(n/i))
				
	print(max(primes))
	
else:
	print(n)
