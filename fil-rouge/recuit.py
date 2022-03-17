import utilities as util
import math
import random 
import matplotlib.pyplot as plt


def recuit(customers, distances, t=300, max_iter=100, a=0.65):
    costs_to_plot = []
    s_best = util.generate_initial_solution(15.5, customers)
    s = s_best
    n_iter = 0
    new_cycle = True
    while (new_cycle == True):
        n_iter = 0
        new_cycle = False
        while(n_iter < max_iter):
            n_iter += 1
            new_s = util.generate_initial_solution(15.5, customers)
            diff = util.cost_function(new_s, distances) - util.cost_function(s, distances)
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
            costs_to_plot.append(util.cost_function(s, distances))
        t = a*t
    
    return s_best, costs_to_plot