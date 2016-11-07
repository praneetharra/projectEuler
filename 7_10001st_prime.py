import math
def isPrimme(a):
	for j in range(2,int(math.sqrt(a))+1):
		if a%j == 0:
			return False
	return True
	
counter = 10001
num = 2
while counter>0:
	if isPrimme(num):
		counter -= 1
	if counter == 0:
		print(num)
	num += 1
