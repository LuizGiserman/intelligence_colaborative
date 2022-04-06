import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation
from recuit import recuitAgent
from utilities import Utilities as util

new_util = util()

class GlobalMASModel(mesa.Model):
  def __init__(self, agents):
    self.schedule = RandomActivation(self)
    self.schedule.add(recuitAgent(0, new_util, t=150, max_iter=30, a=0.95, model=self))
    # self.schedule.add(Johnson2Agent(1,M,self))
    # self.evaluator = EvalAgent(0,M, self, self.schedule.agents)
  def step(self):
    self.schedule.step()
    print(util.cost_function (self.schedule.agents[0].eval()))
    # return self.evaluator.step([agent.eval() for agent in self.schedule.agents]).copy()

model = GlobalMASModel([])
for i in range(5):
    model.step()
