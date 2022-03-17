from node import node
import numpy as np
import utilities as util
import pandas as pd
import math
import random
import tabou
import genetic
import recuilt
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

solutions = []
for i in range(20) :
    solutions.append(util.generate_initial_solution(vehicle_capacity, customers))

solution_tabou, graph = tabou.tabou(solutions[0], customers, vehicle_capacity, distances, max_iterations=50, number_neighbors=10)

#solutions.append(solution_tabou)
solution_genetic, graph_genetic = genetic.genetic(solutions, distances, customers)
plt.plot(graph_genetic)
plt.grid(True)
plt.show()

print("resultat tabou: ", util.cost_function(solution_tabou, distances))
print("resultat genetic: ", util.cost_function(solution_genetic, distances))


recuilt_best, graph_recuilt = recuilt.recuilt(customers, distances, vehicle_capacity)
print('resultat recuilt : ' + str(util.cost_function(recuilt_best, distances)))
# plt.plot(graph_recuilt)
# plt.grid(True)
# plt.show()

# def recuilt(t=150, max_iter=30, a=0.95):
#     s_best = util.generate_initial_solution(15.5, customers)
#     s = s_best
#     n_iter = 0
#     new_cycle = True
#     while (new_cycle == True):
#         n_iter = 0
#         new_cycle = False
#         while(n_iter < max_iter):
#             n_iter += 1
#             new_s = util.generate_initial_solution(15.5, customers)
#             diff = util.cost_function(new_s, distances) - util.cost_function(s, distances)
#             if (diff < 0):
#                 s = new_s
#                 new_cycle = True
#             else:
#                 prob = math.exp(-util.cost_function(s, distances)/t)
#                 q = random.uniform(0,1)
#                 if (q < prob):
#                     s = new_s
#                     new_cycle = True
#             if (util.cost_function(s, distances) < util.cost_function(s_best, distances)):
#                 s_best = s
#         t = a*t
    
#     return s_best
