import networkx as nx
import matplotlib.pyplot as plt
import shelve
import itertools
import xmlrpclib

s = shelve.open('storage')
data = s['data']
data2 = s['data2']
s.close()
#g = nx.Graph()
server = xmlrpclib.Server('http://localhost:20738/RPC2')
G = server.ubigraph

id = 1
for contributors in data2:
	#print contributors
	print id
	for c in itertools.combinations(contributors, 2):
		G.new_vertex_w_id(c[0])
		G.new_vertex_w_id(c[1])
		#G.new_edge(G.new_vertex_w_id(c[0]), G.new_vertex_w_id(c[1]))
		G.new_edge(c[0], c[1])
	id += 1
		#True
#		g.add_edge(c[0], c[1])
#g.add_edge('spam',2)
#g.add_edge('spam',2)

#nx.draw(g)
#plt.show()

