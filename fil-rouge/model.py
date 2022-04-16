import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation
from tabou import tabouAgent
from recuit import recuitAgent
from genetic import geneticAgent
from utilities import Util as util
from eval import evalAgent
import matplotlib.pyplot as plt
import neighborhood as nh

new_util = util()

numberTabou = 3
numberRecuit = 3
numberGenetic = 3

class GlobalMASModel(mesa.Model):
  def __init__(self):
    self.schedule = RandomActivation(self)
    self.listTabou = [tabouAgent(id=i,model=self,new_util=new_util,max_iter=10) for i in range(numberTabou)]
    self.listRecuit = [recuitAgent(id=i,model=self,new_util=new_util,t=150, max_iter=10, a=0.95) for i in range(numberTabou,numberTabou+numberRecuit)]
    self.listGenetic = [geneticAgent(id=i,model=self,new_util=new_util,max_iter=3) for i in range(numberTabou+numberRecuit,numberTabou+numberRecuit+numberGenetic)]

    for agent in self.listTabou:
      self.schedule.add(agent)
    for agent in self.listRecuit:
      self.schedule.add(agent)
    for agent in self.listGenetic:
      self.schedule.add(agent)

    self.evaluator = evalAgent(numberTabou+numberRecuit+numberGenetic,self,new_util)
  def step(self):
    self.schedule.step()
    self.evaluator.step(self.listTabou, self.listRecuit, self.listGenetic)

model = GlobalMASModel()
for i in range(10):
  print(i)
  model.step()

graphTabou = [i[0]["cost"] for i in model.evaluator.listTabou]
graphRecuit = [i[0]["cost"] for i in model.evaluator.listRecuit]
graphGenetic = [i[0]["cost"] for i in model.evaluator.listGenetic]

plt.plot(list(range(len(graphTabou))),graphTabou)
plt.plot(list(range(len(graphRecuit))),graphRecuit)
plt.plot(list(range(len(graphGenetic))),graphGenetic)
plt.legend(['Tabou', 'Recuit', 'Genetic'])
plt.title('Cost Function x Steps')
plt.xlabel('Steps')
plt.ylabel('Cost [Km]')
plt.grid(True)
plt.show()