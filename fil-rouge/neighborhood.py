import random
from collections import deque

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

def assembleSolution(solutionList):
    solution = []
    for solution_node in solutionList:
        for node in solution_node:
            solution.append(node)
        solution.append((0, 0, 0))
    return solution[:-1]

class intraRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        index_1, index_2 = random.sample(range(len(solutionList[route_index])), k=2)
        solutionList[route_index][index_1], solutionList[route_index][index_2] = solutionList[route_index][index_2], solutionList[route_index][index_1]
        return assembleSolution(solutionList)

class interRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        route1_index, route2_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=2)
        index_1 = random.sample(range(len(solutionList[route1_index])), k=1)[0]
        index_2 = random.sample(range(len(solutionList[route2_index])), k=1)[0]
        solutionList[route1_index][index_1], solutionList[route2_index][index_2] = solutionList[route2_index][index_2], solutionList[route1_index][index_1]
        return assembleSolution(solutionList)

class intraRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        route_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=1)[0]
        index_1, index_2 = random.sample(range(len(solutionList[route_index])), k=2)
        
        sub_route = deque((solutionList[route_index][min(index_1,index_2):max(index_1,index_2)+1]))
        sign = 1 if index_1 > index_2 else -1
        sub_route.rotate(sign)
        solutionList[route_index][min(index_1,index_2):max(index_1,index_2)+1] = list(sub_route)

        return assembleSolution(solutionList)

class interRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        route1_index, route2_index = random.choices(range(len(solutionList)), weights=[len(i) for i in solutionList], k=2)
        index_1 = random.sample(range(len(solutionList[route1_index])), k=1)[0]
        index_2 = random.sample(range(len(solutionList[route2_index])), k=1)[0]

        element = solutionList[route1_index][index_1]
        solutionList[route2_index].insert(index_2, element)
        del solutionList[route1_index][index_1]
        
        return assembleSolution(solutionList)

class twoIntraRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        return assembleSolution(solutionList)

class twoIntraRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        return assembleSolution(solutionList)

class elimSmallest():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        return assembleSolution(solutionList)

class elimRandom():
    def __init__(self):
        pass
    
    def execute(self, solutionList):
        return assembleSolution(solutionList)

class functionHandler():
    def __init__(self):
        self.functions = [intraRouteSwap(), interRouteSwap(), intraRouteShift(), interRouteShift(), twoIntraRouteSwap(), twoIntraRouteShift(), elimSmallest(), elimRandom()]

    def execute(self, id, solution):
        solutionList = splitSolution(solution)
        return self.functions[id].execute(solutionList)