import networkx as nx
import matplotlib.pyplot as plt

'''Reference = https://networkx.org/documentation/stable/reference/index.html'''

'''Scale free Graph (Preferential Graph)'''
G = nx.barabasi_albert_graph(50,2)
nx.draw(G)
plt.show()

nx.write_gexf(G, "Analysis_1.gexf")