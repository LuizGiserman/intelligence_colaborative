import random
from collections import deque

# Splits a solution into a table of routes
def splitSolution(solution):
    solutionList = []
    route = []
    for node in solution:
        if not node == (0, 0, 0):
            route.append(node)
        else:
            solutionList.append(route)
            route = []
    if len(route) > 0:
        solutionList.append(route)
    return solutionList

# Assembles a table of routes into a solution
def assembleSolution(solutionList):
    solution = []
    for solution_node in solutionList:
        for node in solution_node:
            solution.append(node)
        solution.append((0, 0, 0))
    return solution[:-1]

#---[NEIGHBORHOOD FUNCTIONS]---#
class intraRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        if [len(i)>=2 for i in solutionList].count(True) < 1:
            return assembleSolution(solutionList)
        route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        while len(solutionList[route_index]) <= 1:
            route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        #-----#
        index_1, index_2 = random.sample(range(len(solutionList[route_index])), k=2)
        solutionList[route_index][index_1], solutionList[route_index][index_2] = solutionList[route_index][index_2], solutionList[route_index][index_1]
        return assembleSolution(solutionList)

class interRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        if [len(i)>0 for i in solutionList].count(True) < 2:
            return assembleSolution(solutionList)
        route1_index, route2_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=2)
        while len(solutionList[route1_index]) < 1 or len(solutionList[route2_index]) < 1 :
            route1_index, route2_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=2)
        #-----#
        index_1 = random.sample(range(len(solutionList[route1_index])), k=1)[0]
        index_2 = random.sample(range(len(solutionList[route2_index])), k=1)[0]
        solutionList[route1_index][index_1], solutionList[route2_index][index_2] = solutionList[route2_index][index_2], solutionList[route1_index][index_1]
        return assembleSolution(solutionList)

class intraRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        if [len(i)>=2 for i in solutionList].count(True) < 1:
            return assembleSolution(solutionList)
        route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        while len(solutionList[route_index]) < 2:
            route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        indexes = random.sample(range(len(solutionList[route_index])), k=2)
        index_1 = min(indexes)
        index_2 = max(indexes)
        #-----#
        sub_route = deque((solutionList[route_index][index_1:index_2+1]))
        sub_route.rotate(-1)
        solutionList[route_index][index_1:index_2+1] = list(sub_route)
        return assembleSolution(solutionList)

class interRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        if [len(i)>0 for i in solutionList].count(True) < 2:
            return assembleSolution(solutionList)
        route1_index, route2_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=2)
        while len(solutionList[route1_index]) < 1 or len(solutionList[route2_index]) < 1 :
            route1_index, route2_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=2)
        index_1 = random.sample(range(len(solutionList[route1_index])), k=1)[0]
        index_2 = random.sample(range(len(solutionList[route2_index])), k=1)[0]
        #-----#
        element = solutionList[route1_index][index_1]
        solutionList[route2_index].insert(index_2, element)
        del solutionList[route1_index][index_1]
        return assembleSolution(solutionList)

class twoIntraRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        if [len(i)>=4 for i in solutionList].count(True) < 1:
            return assembleSolution(solutionList)
        route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        while len(solutionList[route_index]) < 4:
            route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        index_1 = random.randint(0,len(solutionList[route_index])-2)
        index_2 = random.randint(0,len(solutionList[route_index])-2)
        while abs(index_2-index_1) <= 1:
            index_2 = random.randint(0,len(solutionList[route_index])-2)
        #-----#
        solutionList[route_index][index_1], solutionList[route_index][index_2] = solutionList[route_index][index_2], solutionList[route_index][index_1]
        solutionList[route_index][index_1+1], solutionList[route_index][index_2+1] = solutionList[route_index][index_2+1], solutionList[route_index][index_1+1]
        return assembleSolution(solutionList)

class twoIntraRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        if [len(i)>=3 for i in solutionList].count(True) < 1:
            return assembleSolution(solutionList)
        route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        while len(solutionList[route_index]) < 3:
            route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        indexes = random.sample(range(len(solutionList[route_index])), k=2)
        index_1 = min(indexes)
        index_2 = max(indexes)
        #-----#
        sub_route = deque(solutionList[route_index][index_1:index_2+1])
        sub_route.rotate(-2)
        solutionList[route_index][index_1:index_2+1] = list(sub_route)

        return assembleSolution(solutionList)

class elimSmallest():
    def __init__(self):
        pass

    def notNull(self, x):
        return x != 0
    
    def execute(self, solutionList):
        if len(solutionList) < 2 or [len(i)>0 for i in solutionList].count(True) < 1:
            return assembleSolution(solutionList)
        sizes = [len(i) for i in solutionList]
        route_index = sizes.index(min(filter(self.notNull,sizes)))
        break_index = random.randint(0, len(solutionList[route_index]))
        #-----#
        sub_route_1 = solutionList[route_index][:break_index].copy()
        sub_route_2 = solutionList[route_index][break_index:].copy()

        route1_index = random.randint(0, len(solutionList)-1)
        while route1_index == route_index:
            route1_index = random.randint(0, len(solutionList)-1)
        
        route2_index = random.randint(0, len(solutionList)-1)
        while route2_index == route_index:
            route2_index = random.randint(0, len(solutionList)-1)

        if sub_route_1.reverse():
            sub_route_1 = sub_route_1.reverse()

        for node in sub_route_1:
            solutionList[route1_index].insert(0, node)
        
        for node in sub_route_2:
            solutionList[route2_index].append(node)
        
        del solutionList[route_index]

        return assembleSolution(solutionList)

class elimRandom():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        if len(solutionList) < 2 or [len(i)>0 for i in solutionList].count(True) < 1:
            return assembleSolution(solutionList)
        route_index = random.randint(0, len(solutionList)-1)
        while len(solutionList[route_index]) < 1:
            route_index = random.randint(0, len(solutionList)-1)
        break_index = random.randint(0, len(solutionList[route_index]))
        #-----#
        sub_route_1 = solutionList[route_index][:break_index].copy()
        sub_route_2 = solutionList[route_index][break_index:].copy()

        route1_index = random.randint(0, len(solutionList)-1)
        while route1_index == route_index:
            route1_index = random.randint(0, len(solutionList)-1)
        
        route2_index = random.randint(0, len(solutionList)-1)
        while route2_index == route_index:
            route2_index = random.randint(0, len(solutionList)-1)

        if sub_route_1.reverse():
            sub_route_1 = sub_route_1.reverse()

        for node in sub_route_1:
            solutionList[route1_index].insert(0, node)
        
        for node in sub_route_2:
            solutionList[route2_index].append(node)
        
        del solutionList[route_index]

        return assembleSolution(solutionList)
#------------------------------#

class functionHandler():
    def __init__(self):
        self.functions = [intraRouteSwap(), interRouteSwap(), intraRouteShift(), interRouteShift(), twoIntraRouteSwap(), twoIntraRouteShift(), elimSmallest(), elimRandom()]

    def execute(self, id, solution):
        solutionList = splitSolution(solution)
        return self.functions[id].execute(solutionList)