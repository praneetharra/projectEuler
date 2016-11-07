def mult_generator(a):
    for i in a:
        if i%3 == 0 or i%5 == 0:
            yield i
            
total = 0
for i in mult_generator(range(1,1000)):
    total += i
print(total)
