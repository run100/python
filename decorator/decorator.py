

ef new_fn(f):
	def fn( '__call__ ' + f.__name__ + '()' 
		return f(x)
	return fn


def f1(x):
   rieturn x*2


g1 = new_fn(f1)
print g1(5)
