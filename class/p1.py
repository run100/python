
class Person(object):
   	pass


p1 = Person()
p1.name = 'z'


p2 = Person()
p2.name = 'c'


p3 = Person()
p3.name = 'd'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1,p2:cmp(p1.name, p2.name))

print L1

for i in range(0, 3):
	print L2[i].name
