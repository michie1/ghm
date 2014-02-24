import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edge('spam',2)
g.add_edge('spam',2)

nx.draw(g)
plt.show()
