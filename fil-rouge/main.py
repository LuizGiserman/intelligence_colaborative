from node import node
import numpy as np
import utilities as util


a = node(1, 1, 0, 1, 50.6063978, 3.1360337)
b = node (1, 1, 1, 0, 50.61696744944052, 3.131022834587549)

graph_nodes = [a, b]

distances = []

for i, node1 in enumerate(graph_nodes):
    aux = []
    for node2 in graph_nodes[i:]:
        aux.append(util.distance(node1.lat, node2.lat, node1.long, node2.long))
    distances.append(aux)


print (distances)


