
def log(f):
	def fn(*args, **kw):
		print 'call '+ f.__name__ + '()' 
		return f(*args, **kw)
	return fn

@log
def factorial(n):
	return reduce(lambda x,y:x*y, range(1, n+1))

@log
def add(x, y):
	return x+y

print factorial(10)
print add(1, 2)

