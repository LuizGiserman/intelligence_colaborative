from asyncio.windows_events import NULL
import utilities as util
import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation

class tabouAgent(mesa.Agent):
  def __init__(self, id, model, customers, vehicle_capacity, distances, number_neighbors = 5):
    super().__init__(id, model)
    self.customers = customers
    self.vehicle_capacity = vehicle_capacity
    self.distances = distances
    self.number_neighbors = number_neighbors
    self.solution = NULL
    self.visited_solutions = []
  def step(self, solution):
    best_solution = solution.copy()
    current_solution = solution.copy()

    neighborhood = util.generate_neighborhood(current_solution, self.customers, self.vehicle_capacity, switchNodes=self.number_neighbors)

    best_neighbor = neighborhood[0]
    for neighbor in neighborhood[1:]:
        if not (neighbor in self.visited_solutions):
            if util.cost_function(neighbor, self.distances) < util.cost_function(best_neighbor, self.distances):
                best_neighbor = neighbor
    
    self.visited_solutions.append(best_neighbor)

    current_solution = best_neighbor.copy()

    if util.cost_function(current_solution, self.distances) < util.cost_function(best_solution, self.distances):
        best_solution = current_solution.copy()

    self.solution = best_solution

    def eval(self):
        return self.solution


'''def tabou(solution, customers, vehicle_capacity, distances, max_iterations = 20, number_neighbors = 5):
    best_solution = solution.copy()
    current_solution = solution.copy()

    iteration = 0
    visited_solutions = []
    best_solution_index = 0

    graph = []

    while iteration - best_solution_index < max_iterations :
        neighborhood = util.generate_neighborhood(current_solution, customers, vehicle_capacity, switchNodes=number_neighbors)

        best_neighbor = neighborhood[0]
        for neighbor in neighborhood[1:]:
            if not (neighbor in visited_solutions):
                if util.cost_function(neighbor, distances) < util.cost_function(best_neighbor, distances):
                    best_neighbor = neighbor
        
        visited_solutions.append(best_neighbor)

        current_solution = best_neighbor.copy()

        if util.cost_function(current_solution, distances) < util.cost_function(best_solution, distances):
            best_solution = current_solution.copy()
            best_solution_index = iteration

        graph.append(util.cost_function(current_solution, distances))
        iteration += 1

    return best_solution, graph'''