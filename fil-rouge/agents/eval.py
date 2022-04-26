import mesa
from auxiliar.utilities import Util as util
import random

class evalAgent(mesa.Agent):
  def __init__(self, id, model, utility : util):
    super().__init__(id, model)
    self.listTabou = []
    self.listRecuit = []
    self.listGenetic = []
    self.util = utility
  
  # Function that creates a pool with the most recent solutions and "refeed" the agents
  def refeed(self, agentsTabou, agentsRecuit, agentsGenetic):
    pool = []
    # Adds the most reacent solutions to pool
    for i in range(2):
      pool.append(self.listTabou[-1][i]["agent"])
      pool.append(self.listRecuit[-1][i]["agent"])
      pool.append(self.listGenetic[-1][i]["agent"])
    
    # Refeed the agents with a random solution from pool
    for agent in agentsTabou:
      agent.solution = pool[random.randint(0,5)]
    for agent in agentsRecuit:
      agent.s = pool[random.randint(0,5)]
      agent.s_best = agent.s
    for agent in agentsGenetic:
      agent.solutions[-6:] = pool

  # Function that records all solutions for all agents at each step and applies the Q-Learning for the neighborhood generation
  def step(self, agentsTabou, agentsRecuit, agentsGenetic):
    aux_list = []
    for agent in agentsTabou:
      cost = self.util.cost_function(agent.eval())
      agent.utility.Q_learning(agent.initialCost, cost)
      item = {"agent" : agent.eval(), "cost" : cost}
      aux_list.append(item)
    aux_list = sorted(aux_list, key = lambda i: i['cost'])
    self.listTabou.append(aux_list)

    aux_list = []
    for agent in agentsRecuit:
      cost = self.util.cost_function(agent.eval())
      agent.utility.Q_learning(agent.initialCost, cost)
      item = {"agent" : agent.eval(), "cost" : cost}
      aux_list.append(item)
    aux_list = sorted(aux_list, key = lambda i: i['cost'])
    self.listRecuit.append(aux_list)

    aux_list = []
    for agent in agentsGenetic:
      cost = self.util.cost_function(agent.eval())
      agent.utility.Q_learning(agent.initialCost, cost)
      item = {"agent" : agent.eval(), "cost" : cost}
      aux_list.append(item)
    aux_list = sorted(aux_list, key = lambda i: i['cost'])
    self.listGenetic.append(aux_list)
  
    self.refeed(agentsTabou, agentsRecuit, agentsGenetic)