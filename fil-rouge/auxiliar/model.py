import mesa
from mesa.time import RandomActivation
#---[AGENTS]---#
from agents.tabou import tabouAgent
from agents.recuit import recuitAgent
from agents.genetic import geneticAgent
from agents.eval import evalAgent
#--------------#
from auxiliar.utilities import Util as util

utility = util()

numberTabou = 3
numberRecuit = 3
numberGenetic = 3

# General model that contains lists of agents
class GlobalMASModel(mesa.Model):
  def __init__(self):
    self.schedule = RandomActivation(self)
    self.listTabou = [tabouAgent(id=i,model=self,utility=utility,max_iter=10) for i in range(numberTabou)]
    self.listRecuit = [recuitAgent(id=i,model=self,utility=utility,t=150, max_iter=10, a=0.95) for i in range(numberRecuit,numberTabou+numberRecuit)]
    self.listGenetic = [geneticAgent(id=i,model=self,utility=utility,max_iter=3) for i in range(numberTabou+numberRecuit,numberTabou+numberRecuit+numberGenetic)]

    for agent in self.listTabou:
      self.schedule.add(agent)
    for agent in self.listRecuit:
      self.schedule.add(agent)
    for agent in self.listGenetic:
      self.schedule.add(agent)

    # Evaluator agent
    self.evaluator = evalAgent(numberTabou+numberRecuit+numberGenetic,self,utility)
  def step(self):
    self.schedule.step()
    self.evaluator.step(self.listTabou, self.listRecuit, self.listGenetic)