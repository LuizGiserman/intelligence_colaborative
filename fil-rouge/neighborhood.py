
class intraRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class interRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class intraRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class interRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class twoIntraRouteSwap():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class twoIntraRouteShift():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class elimSmallest():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class elimRandom():
    def __init__(self):
        pass
    
    def execute(self, solution):
        return solution

class functionHandler():
    def __init__(self):
        self.functions = [intraRouteSwap(), interRouteSwap(), intraRouteShift(), interRouteShift(), twoIntraRouteSwap(), twoIntraRouteShift(), elimSmallest(), elimRandom()]

    def execute(self, id, solution):
        return self.functions[id].execute(solution)