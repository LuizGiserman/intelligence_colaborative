import random
import math
import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation
from utilities import Util as util

class tabouAgent(mesa.Agent):
    def __init__(self, id, model, new_util : util, max_iter = 10, number_neighbors = 5):
        super().__init__(id, model)
        self.customers = new_util.customers
        self.vehicle_capacity = new_util.vehicle_capacity
        self.distances = new_util.distances
        self.max_iter = max_iter
        self.number_neighbors = number_neighbors
        self.solution = new_util.generate_initial_solution()
        self.visited_solutions = []
        self.new_util = new_util

        self.new_util.newAction()
        holdSolution = self.solution
        self.step()
        self.initialCost = new_util.cost_function(self.eval())
        self.solution = holdSolution
        
    def step(self):
        best_solution = self.solution.copy()
        current_solution = self.solution.copy()
        
        for i in range(self.max_iter):
            neighborhood = self.new_util.generate_neighborhood(current_solution, numberNeighbors=self.number_neighbors)
            
            best_neighbor = neighborhood[0]
            for neighbor in neighborhood[1:]:
                if not (neighbor in self.visited_solutions):
                    if self.new_util.cost_function(neighbor) < self.new_util.cost_function(best_neighbor):
                        best_neighbor = neighbor

            self.visited_solutions.append(best_neighbor)

            current_solution = best_neighbor.copy()

            if self.new_util.cost_function(current_solution) < self.new_util.cost_function(best_solution):
                best_solution = current_solution.copy()

        self.solution = best_solution

    def eval(self):
        return self.solution

# def tabou(solution, customers, vehicle_capacity, distances, max_iterations = 20, number_neighbors = 5):
#     best_solution = solution.copy()
#     current_solution = solution.copy()

#     iteration = 0
#     visited_solutions = []
#     best_solution_index = 0

#     graph = []

#     while iteration - best_solution_index < max_iterations :
#         neighborhood = util.generate_neighborhood(current_solution, customers, vehicle_capacity, switchNodes=number_neighbors)

#         best_neighbor = neighborhood[0]
#         for neighbor in neighborhood[1:]:
#             if not (neighbor in visited_solutions):
#                 if util.cost_function(neighbor, distances) < util.cost_function(best_neighbor, distances):
#                     best_neighbor = neighbor
        
#         visited_solutions.append(best_neighbor)

#         current_solution = best_neighbor.copy()

#         if util.cost_function(current_solution, distances) < util.cost_function(best_solution, distances):
#             best_solution = current_solution.copy()
#             best_solution_index = iteration

#         graph.append(util.cost_function(current_solution, distances))
#         iteration += 1

#     return best_solution, graph
