import mesa
from mesa.space import MultiGrid
from datetime import datetime
from mesa.time import RandomActivation
from utilities import Util as util
import random
import cmath

class evalAgent(mesa.Agent):
  def __init__(self, id, model, new_util : util):
    super().__init__(id, model)
    self.customers = new_util.customers
    self.listTabou = []
    self.listRecuit = []
    self.listGenetic = []
    self.util = new_util
  
  def refeed(self, agentsTabou, agentsRecuit, agentsGenetic):
    pool = []
    for i in range(2):
      pool.append(self.listTabou[-1][i]["agent"])
      pool.append(self.listRecuit[-1][i]["agent"])
      pool.append(self.listGenetic[-1][i]["agent"])
    
    for agent in agentsTabou:
      agent.solution = pool[random.randint(0,5)]
    for agent in agentsRecuit:
      agent.s = pool[random.randint(0,5)]
      agent.s_best = agent.s
    for agent in agentsGenetic:
      agent.solutions[-6:] = pool

  def step(self, agentsTabou, agentsRecuit, agentsGenetic):
    aux_list = []
    for agent in agentsTabou:
      item = {"agent" : agent.eval(), "cost" : self.util.cost_function(agent.eval())}
      aux_list.append(item)
    aux_list = sorted(aux_list, key = lambda i: i['cost'])
    self.listTabou.append(aux_list)

    aux_list = []
    for agent in agentsRecuit:
      item = {"agent" : agent.eval(), "cost" : self.util.cost_function(agent.eval())}
      aux_list.append(item)
    aux_list = sorted(aux_list, key = lambda i: i['cost'])
    self.listRecuit.append(aux_list)

    aux_list = []
    for agent in agentsGenetic:
      item = {"agent" : agent.eval(), "cost" : self.util.cost_function(agent.eval())}
      aux_list.append(item)
    aux_list = sorted(aux_list, key = lambda i: i['cost'])
    self.listGenetic.append(aux_list)
  
    self.refeed(agentsTabou, agentsRecuit, agentsGenetic)
