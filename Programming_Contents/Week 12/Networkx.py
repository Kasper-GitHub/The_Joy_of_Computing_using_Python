import networkx as nx
import matplotlib.pyplot as plt

G = nx.barbell_graph(4,2)
plt.figure(1)
nx.draw(G)
plt.show()

G = nx.complete_graph(4)
plt.figure(2)
nx.draw(G)
plt.show()

G = nx.cycle_graph(5)
plt.figure(3)
nx.draw(G)
plt.show()

G = nx.ladder_graph(5)
plt.figure(4)
nx.draw(G)
plt.show()

G = nx.path_graph(6)
plt.figure(5)
nx.draw(G)
plt.show()

G = nx.star_graph(5)
plt.figure(6)
nx.draw(G)
plt.show()

G = nx.wheel_graph(4)
plt.figure(7)
nx.draw(G)
plt.show()

G = nx.gnp_random_graph(5,0.5)
plt.figure(8)
nx.draw(G)
plt.show()
