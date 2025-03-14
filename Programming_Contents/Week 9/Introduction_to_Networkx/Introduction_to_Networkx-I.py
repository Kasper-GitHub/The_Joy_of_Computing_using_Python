import networkx as nx
import matplotlib.pyplot as plt

'''Reference = https://networkx.org/documentation/stable/reference/index.html'''

'''Drawing Nodes & Edges'''
G = nx.Graph()

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

list = [1,2,3]
G.add_nodes_from(list)

G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# print(G.edges())

plt.figure(1)
nx.draw(G)
plt.show()

'''Drawing Complete Graph'''
H = nx.complete_graph(15)
plt.figure(2)
nx.draw(H)
plt.show()

'''Drawing Random Graph'''
K = nx.gnp_random_graph(10,0.5)
print(nx.is_connected(K))
plt.figure(3)
nx.draw(K)
plt.show()