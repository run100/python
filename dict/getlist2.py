
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

def get_str(name, score):
   return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [get_str(name, score) for name,score in d.iteritems() ]

print '\n'.join(tds)
