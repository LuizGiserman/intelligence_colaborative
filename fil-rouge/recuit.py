import utilities as util
import random
import math
import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation

def recuit(customers, distances, vehicle_capacity=20, t=150, max_iter=30, a=0.95):
    s_best = util.generate_initial_solution(15.5, customers)
    s = s_best
    n_iter = 0
    new_cycle = True
    graph = []
    while (new_cycle == True):
        n_iter = 0
        new_cycle = False
        while(n_iter < max_iter):
            n_iter += 1
            new_s = util.generate_neighborhood(s, customers, vehicle_capacity)[random.randint(0,4)] #util.generate_initial_solution(15.5, customers)
            diff = util.cost_function(new_s, distances) - util.cost_function(s, distances)
            graph.append(util.cost_function(new_s, distances))
            if (diff < 0):
                s = new_s
                new_cycle = True
            else:
                prob = math.exp(-util.cost_function(s, distances)/t)
                q = random.uniform(0,1)
                if (q < prob):
                    s = new_s
                    new_cycle = True
            if (util.cost_function(s, distances) < util.cost_function(s_best, distances)):
                s_best = s
        t = a*t
    
    return s_best, graph


class recuitAgent(mesa.Agent):
      def __init__(self, id, M, model):
        
