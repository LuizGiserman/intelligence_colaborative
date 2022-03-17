from node import node
import numpy as np
import utilities as util
import pandas as pd
import math
import random
import genetic
from recuit import recuit
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


new_s, costs = recuit(customers, distances)

iters = [i for i in range(len(costs))]

plt.plot(iters, costs)
plt.ylabel("Cout")
plt.xlabel("Iteration")
plt.title("Iteration du methode de recuit par cout de solution")
plt.show()



# solutions = []
# for i in range(20) :
#     solutions.append(util.generate_initial_solution(vehicle_capacity, customers))

# solution_tabou, graph = tabou.tabou(solutions[0], customers, vehicle_capacity, distances, max_iterations=50, number_neighbors=10)

# #solutions.append(solution_tabou)
# solution_genetic = genetic.genetic(solutions, distances, customers)

# print("resultat tabou: ", util.cost_function(solution_tabou, distances))
# print("resultat genetic: ", util.cost_function(solution_genetic, distances))
# plt.plot(graph)
# plt.grid(True)
# plt.show()