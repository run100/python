# -*- coding:utf-8 -*-

sum = 0
x = 1
while True:
	sum = sum + x
	x = x +1
	if x >= 100 :
		break

print sum


sum1 = 0
x = 1
n  = 0
while True:
	if n > 20:
		break

	sum1 = sum1 + x*n
	n = n + 1
	x = x * 2


print sum1
