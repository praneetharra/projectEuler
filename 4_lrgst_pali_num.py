def isPalidrome(s):
	if len(s)<=1:
		return True
	else:
		if s[0] == s[len(s)-1]:
			return isPalidrome(s[1:len(s)-1])
		else:
			return False
			
i = 999
j = 999

def func(i,j):
	maxi = 0
	while(i>0):
		j = 999
		while(j>0):
			if isPalidrome(str(i*j)):
				if i*j > maxi:
					maxi = i*j
			j = j-1
		i = i-1
	return maxi
print(func(i,j))
