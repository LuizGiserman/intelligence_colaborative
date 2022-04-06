import random
import math
import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation
from utilities import Util as util



class recuitAgent(mesa.Agent):
    def __init__(self, id, model, new_util, t, max_iter, a):
        super().__init__(id, model)
        self.id = id
        self.customers = new_util.customers
        self.distances = new_util.distances
        self.vehicle_capacity = new_util.vehicle_capacity
        self.t = t
        self.max_iter = max_iter
        self.a = a
        self.model = model
        self.new_cycle = True
        self.s_best = new_util.generate_initial_solution()
        self.s = self.s_best
        self.n_iter = 0
        self.new_util = new_util
        
    def step(self):
        if self.new_cycle == True:
            self.n_iter = 0
            self.new_cycle = False
            while(self.n_iter < self.max_iter):
                self.n_iter += 1
                new_s = self.new_util.generate_neighborhood(self.s)[random.randint(0,4)] #util.generate_initial_solution(15.5, customers)
                diff = self.new_util.cost_function(new_s) - self.new_util.cost_function(self.s)
                if (diff < 0):
                    self.s = new_s
                    self.new_cycle = True
                else:
                    prob = math.exp(-self.new_util.cost_function(self.s)/self.t)
                    q = random.uniform(0,1)
                    if (q < prob):
                        self.s = new_s
                        self.new_cycle = True
                if (self.new_util.cost_function(self.s) < self.new_util.cost_function(self.s_best)):
                    self.s_best = self.s
            self.t = self.a * self.t
    
    def eval(self):
        self.new_cycle = True
        return self.s_best.copy()


# def recuit(customers, distances, vehicle_capacity=20, t=150, max_iter=30, a=0.95):
#     s_best = util.generate_initial_solution(15.5, customers)
#     s = s_best
#     n_iter = 0
#     new_cycle = True
#     graph = []
#     while (new_cycle == True):
#         n_iter = 0
#         new_cycle = False
#         while(n_iter < max_iter):
#             n_iter += 1
#             new_s = util.generate_neighborhood(s, customers, vehicle_capacity)[random.randint(0,4)] #util.generate_initial_solution(15.5, customers)
#             diff = util.cost_function(new_s, distances) - util.cost_function(s, distances)
#             graph.append(util.cost_function(new_s, distances))
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
    
#     return s_best, graph