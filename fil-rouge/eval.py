import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation
import utilities as util
import cmath

class EvalAgent(mesa.Agent):
  def __init__(self, id, customers, model, agents):
    super().__init__(id, model)
    self.customers = customers
    self.best = [cmath.inf for agent in agents]
  def step(self, agents):
    cmax = []
    for i, tasks in enumerate(agents):
      atual = util.cost_function([u+1 for u in tasks], self.M, 3)
      cmax.append(atual)
      if self.best[i] > atual:
        self.best[i] = atual 
    return self.best