from node import node
import numpy as np
import utilities as util
import pandas as pd
import tabou
import matplotlib.pyplot as plt

vehicle_capacity = 20

customers = util.load_customers()

#customers are starting in 0 in this list
## although the customer number starts in 1
distances = {}

# creates a dictionary (node1, node2) to save the distances from node 1 to node 2
## saves half of it in order to optimize the utilized space
for i, node1 in enumerate(customers):
    for node2 in customers:
        distances[(node1.code, node2.code)] = util.distance(node1.lat, node2.lat, node1.long, node2.long)

solution = util.generate_initial_solution(vehicle_capacity, customers)

solution_tabou, graph = tabou.tabou(solution, customers, vehicle_capacity, distances, max_iterations=10, number_neighbors=2)

plt.plot(graph)
plt.grid(True)
plt.show()

# def recuilt(max_iter):
#     s = get_initial_solution()
#     n_iter = 0
#     new_cycle = True