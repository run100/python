import math


def fact(n):
   	if n == 1:
		return 1;
	return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)


def move(x, y, step, angle):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

print move(100, 100, 60, math.pi / 6)
   	

def my_abs(x):
   	if x >= 0:
		return x
	else:
	   	return -x


print my_abs(-999)


def square_of_sum(arr):
   	sum = 0.0
	for num in arr:
	   	sum = sum + (num * num)
	
	return sum


A = [1,234,2,2342]

print square_of_sum(A)






