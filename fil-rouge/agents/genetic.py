import random
import mesa
from auxiliar.utilities import Util as util

class geneticAgent(mesa.Agent):
    def __init__(self, id, model, utility : util, max_iter = 3, number_solutions = 20):
        super().__init__(id, model)
        self.solutions = [utility.generate_initial_solution() for i in range(number_solutions)]
        self.pairs = [(i % int(len(self.solutions)/2), (i+1) % int(len(self.solutions)/2)) for i in range(int(len(self.solutions)/2))]
        self.utility = utility
        self.max_iter = max_iter

        # Stores the initial cost
        self.utility.newAction()
        holdSolutions = self.solutions.copy()
        self.step()
        self.initialCost = utility.cost_function(self.eval())
        self.solutions = holdSolutions.copy()

    # Function that retuns the first half of a solutions list
    def selection (self, pop_before) :
        return pop_before[:int(len(pop_before)/2)]

    # Function that does the crossing over between two different solutions
    def crossing_over(self, solution1, solution2):
        # Deletes all deposits from solutions
        child1 = [i for i in solution1 if i != (0,0,0)]
        child2 = [i for i in solution2 if i != (0,0,0)]
        
        # Gets a random cutting point
        end_point = len(child1)-1
        start_point = random.randint(0, end_point-1)

        # Crossing over
        child1[start_point : end_point+1], child2[start_point : end_point+1] = child2[start_point : end_point+1], child1[start_point : end_point+1]

        # Solves duplication problems
        outside = []
        for i in child1:
            if not i in child2:
                outside.append(i)
        if len(outside):
            for i in range(len(child2)-1):
                if child2[i] in child2[i+1:]:
                    child2[i] = outside.pop()
        
        # Adds the deposits when necessary so the final solution becomes possible
        current_capacity = self.utility.vehicle_capacity
        child = []
        for gene in child2:
            if current_capacity - self.utility.customers[gene[2]].vol < 0:
                current_capacity = self.utility.vehicle_capacity
                child.append((0,0,0))    

            child.append(gene)
            current_capacity -= self.utility.customers[gene[2]].vol
        
        return child

    # Function that applies the algorithm
    def step(self):
        population_before = []
        population = []
        population_after = []
        
        # Stores all solutions and their fitness
        for solution in self.solutions :
            population_before.append({"individual":solution, "fitness":self.utility.cost_function(solution)})

        for index in range(self.max_iter):
            # Sorts the population by their fitness
            population_before  = sorted(population_before, key = lambda i: i['fitness'])
            # Stores the top 50% solutions
            population = self.selection(population_before).copy()

            for pair in self.pairs:
                # Avoids changing the number of solutions
                if len(population) >= len(self.solutions):
                    break
                # Does the crossing over between the top 50% solutions
                individual = self.crossing_over(population[pair[0]]["individual"], population[pair[1]]["individual"])
                # Replaces the other solutions by the crossing over results
                population.append({"individual":individual, "fitness":self.utility.cost_function(individual)})
            
            population_after.clear()
            for individual in population:
                # Gets a neighbor for each solution
                aux_individual = self.utility.generate_neighborhood(individual["individual"], numberNeighbors=1, repeat=1)[0]
                population_after.append({"individual":aux_individual, "fitness":self.utility.cost_function(aux_individual)})

            population_before = population_after

        population_before  = sorted(population_before, key = lambda i: i['fitness'])

        # Stores all solutions
        self.solutions = [i["individual"] for i in population_before]

    # Returns the best solution
    def eval(self):
        return self.solutions[0]





        


    
