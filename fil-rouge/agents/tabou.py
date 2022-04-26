import mesa
from auxiliar.utilities import Util as util

class tabouAgent(mesa.Agent):
    def __init__(self, id, model, utility : util, max_iter = 10, number_neighbors = 5):
        super().__init__(id, model)
        self.max_iter = max_iter
        self.number_neighbors = number_neighbors
        self.solution = utility.generate_initial_solution()
        self.visited_solutions = []
        self.utility = utility

        # Stores the initial cost
        self.utility.newAction()
        holdSolution = self.solution
        self.step()
        self.initialCost = utility.cost_function(self.eval())
        self.solution = holdSolution
    
    # Function that applies the algorithm
    def step(self):
        best_solution = self.solution.copy()
        current_solution = self.solution.copy()
        
        for i in range(self.max_iter):
            # Generates a neighborhood for the current solution
            neighborhood = self.utility.generate_neighborhood(current_solution, numberNeighbors=self.number_neighbors)
            
            # Chooses the best neighbor
            best_neighbor = neighborhood[0]
            for neighbor in neighborhood[1:]:
                if not (neighbor in self.visited_solutions):
                    if self.utility.cost_function(neighbor) < self.utility.cost_function(best_neighbor):
                        best_neighbor = neighbor

            # Adds the best neighbor to the visited solutions list
            self.visited_solutions.append(best_neighbor)

            # Updates the current solution
            current_solution = best_neighbor.copy()

            if self.utility.cost_function(current_solution) < self.utility.cost_function(best_solution):
                best_solution = current_solution.copy()

        # Updates the solution
        self.solution = best_solution

    # Returns the best solution
    def eval(self):
        return self.solution