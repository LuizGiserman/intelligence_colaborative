import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation

class GlobalMASModel(mesa.Model):
  def __init__(self, agents):
    self.schedule = RandomActivation(self)
    # self.schedule.add(ListAgent(0,M,self))
    # self.schedule.add(Johnson2Agent(1,M,self))
    # self.evaluator = EvalAgent(0,M, self, self.schedule.agents)
  def step(self):
    self.schedule.step()
    return self.evaluator.step([agent.eval() for agent in self.schedule.agents]).copy()