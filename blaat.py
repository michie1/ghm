import shelve

s = shelve.open('storage')
#print s
for el in s['data2']:
	print len(el)


"""
if False:
	s = shelve.open('storage')
	s['i'] = 0
	s['data'] = []

	s.close()


s = shelve.open('storage')
#a = s['a']
print s['i']
#print type(s['data'])
s.close()
#print a
"""
