
print range(1, 11)

L = []
for i in range(1, 11):
   	L.append(i*i)

print L


a = [x * x for x in range(1, 11)]
print a


b = [ x*(x+1) for x in range(1, 101, 2) ]
print b


