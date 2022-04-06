import utilities as util
import random
import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation
from utilities import Util as util

class geneticAgent(mesa.Agent):
    def __init__(self, id, model, new_util : util, max_iter = 3, number_solutions = 20):
        super().__init__(id, model)
        self.customers = new_util.customers
        self.vehicle_capacity = new_util.vehicle_capacity
        self.distances = new_util.distances
        self.solutions = [new_util.generate_initial_solution() for i in range(number_solutions)]
        self.new_util = new_util
        self.max_iter = max_iter

    def selection (self, pop_before) :
        return pop_before[:int(len(pop_before)/2)]

    def pairing (self, len_pop) :
        pairs = []
        for index in range(len_pop - 1):
            pairs.append((index, index + 1))
        
        pairs.append((len_pop - 1, 0))
        
        return pairs

    def crossing_over(self, solution1, solution2, customers, vehicle_capacity=20):
        child1 = [i for i in solution1 if i != (0,0,0)]
        child2 = [i for i in solution2 if i != (0,0,0)]
        
        end_point = len(child1)-1
        start_point = random.randint(0, end_point-1)

        child1[start_point : end_point+1], child2[start_point : end_point+1] = child2[start_point : end_point+1], child1[start_point : end_point+1]

        outside = []
        for i in child1:
            if not i in child2:
                outside.append(i)
        for i in range(len(child2)-1):
            if child2[i] in child2[i+1:]:
                child2[i] = outside.pop()
        
        current_capacity = vehicle_capacity
        child = []
        for gene in child2:
            if current_capacity - customers[gene[2]].vol < 0:
                current_capacity = vehicle_capacity
                child.append((0,0,0))    

            child.append(gene)
            current_capacity -= customers[gene[2]].vol
        
        return child

    def step(self):
        pop_before = []
        pop = []
        pop_after = []
        pairs = []

        for solution in self.solutions :
            pop_before.append({"individual":solution, "fitness":self.new_util.cost_function(solution)})
                

        for index in range(self.max_iter) :

            pop_before  = sorted(pop_before, key = lambda i: i['fitness'])
            pop = self.selection(pop_before).copy()

            pairs = self.pairing(len(pop))

            for pair in (pairs) :
                individual = self.crossing_over(pop[pair[0]]["individual"], pop[pair[1]]["individual"], self.customers, self.vehicle_capacity)
                pop.append({"individual":individual, "fitness":self.new_util.cost_function(individual)})
            
            pop_after.clear()
            for individual in pop :
                aux_individual = self.new_util.generate_neighborhood(individual["individual"], numberNeighbors=1, switchNodes=5)[0]
                pop_after.append({"individual":aux_individual, "fitness":self.new_util.cost_function(aux_individual)})

            pop_before = pop_after

        pop_before  = sorted(pop_before, key = lambda i: i['fitness'])
        
        self.solutions = [i["individual"] for i in pop_before]

    def eval(self):
        return self.solutions[0]


# def genetic (solutions, distances, customers, max_iterations = 20, vehicle_capacity = 20) :

#     pop_before = []
#     pop = []
#     pop_after = []
#     pairs = []
#     graph = []

#     for solution in solutions :
#             pop_before.append({"individual":solution, "fitness":util.cost_function(solution, distances)})
            

#     for index in range(max_iterations) :

#         pop_before  = sorted(pop_before, key = lambda i: i['fitness'])
#         pop = selection(pop_before).copy()

#         pairs = pairing(len(pop))

#         for pair in (pairs) :
#             individual = crossing_over(pop[pair[0]]["individual"], pop[pair[1]]["individual"], customers, vehicle_capacity)
#             pop.append({"individual":individual, "fitness":util.cost_function(individual, distances)})

#             graph.append(util.cost_function(pop[pair[0]]["individual"], distances))
        
#         pop_after.clear()
#         for individual in pop :
#             aux_individual = util.generate_neighborhood(individual["individual"], customers, vehicle_capacity, 1, 5)[0]
#             pop_after.append({"individual":aux_individual, "fitness":util.cost_function(aux_individual, distances)})

#         pop_before = pop_after

#     pop_before  = sorted(pop_before, key = lambda i: i['fitness'])
    
#     return pop_before[0]["individual"], graph






        


    
