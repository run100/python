i = int('a', 16)

print i


def power(x, n=2):
	s = 1 
	while n > 0:
		n = n -1
		s = s * x

	return s
		

print power(5)


def fn(*arg):
	print arg


print fn(1)
print fn(1,2)
print fn(1,2,3,4)
print fn(1,3,4,5,6)
