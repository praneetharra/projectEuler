sums = 0
sqr = 0
for i in range(1,101):
	sums += i
	sqr += i*i
	
diff = sums*sums - sqr
print(diff)
