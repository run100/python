
A = ['admin','zzw','cc','dd']
B = range(1, 10)
for index,name in enumerate(B):
   print index,name


for index,name in zip(range(1, len(A)+1),A):
   print index,',',name

