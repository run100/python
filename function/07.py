
def calc_prod(lst):
   def lazy_prod():
	  def f(x, y):
		 return x*y;
	  return reduce(f, lst, 1)
   return lazy_prod


f = calc_prod([1, 2, 3])

print f()
