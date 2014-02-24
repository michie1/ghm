import shelve

s = shelve.open('storage', 'n')
s['rep_last_id'] = 0
s['data'] = []
s['data2'] = []
s.close()
