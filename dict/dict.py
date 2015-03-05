d = {
	'admin' : 95,
	'hello' : 80,
	'zzw'   : 70
}

print len(d)

if 'admin' in d:
	print d['admin']

print d.get('admin')

for key in d:
	print d[key]
	
