import random
import math
import mesa
from auxiliar.utilities import Util as util

class recuitAgent(mesa.Agent):
    def __init__(self, id, model, utility : util, t, max_iter, a):
        super().__init__(id, model)
        self.t = t
        self.max_iter = max_iter
        self.a = a
        self.new_cycle = True
        self.s_best = utility.generate_initial_solution()
        self.s = self.s_best
        self.n_iter = 0
        self.utility = utility

        # Stores the initial cost
        self.utility.newAction()
        holdS_best = self.s_best
        self.step()
        self.initialCost = utility.cost_function(self.eval())
        self.s = holdS_best
        self.s_best = holdS_best
    
    # Function that applies the algorithm
    def step(self):
        if self.new_cycle == True:
            self.n_iter = 0
            self.new_cycle = False
            while(self.n_iter < self.max_iter):
                self.n_iter += 1
                new_s = self.utility.generate_neighborhood(self.s)[random.randint(0,4)]
                diff = self.utility.cost_function(new_s) - self.utility.cost_function(self.s)
                if (diff < 0):
                    self.s = new_s
                    self.new_cycle = True
                else:
                    prob = math.exp(-self.utility.cost_function(self.s)/self.t)
                    q = random.uniform(0,1)
                    if (q < prob):
                        self.s = new_s
                        self.new_cycle = True
                if (self.utility.cost_function(self.s) < self.utility.cost_function(self.s_best)):
                    self.s_best = self.s
            self.t = self.a * self.t
    
    # Returns the best solution
    def eval(self):
        self.new_cycle = True
        return self.s_best.copy()