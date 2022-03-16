from distutils.sysconfig import customize_compiler
from node import node
import numpy as np
import utilities as util
import pandas as pd



customers = util.load_customers()

#customers are starting in 0 in this list
## although the customer number starts in 1
distances = []

# creates a triangular matrix to save the distances
## saves half of it in order to optimize the utilized space
for i, node1 in enumerate(customers):
    aux = []
    for node2 in customers[i:]:
        aux.append(util.distance(node1.lat, node2.lat, node1.long, node2.long))
    distances.append(aux)

print(distances[50])

print(customers[50].get_distance(1158, distances))

