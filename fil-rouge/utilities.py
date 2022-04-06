from locale import currency
from math import radians, cos, sin, asin, sqrt
from node import node
import pandas as pd
import random

class Util():
    def __init__(self):
        self.vehicle_capacity = 20

        self.customers = self.load_customers().copy()

        #customers are starting in 0 in this list
        ## although the customer number starts in 1
        self.distances = {}

        # creates a dictionary (node1, node2) to save the distances from node 1 to node 2
        ## saves half of it in order to optimize the utilized space
        for i, node1 in enumerate(self.customers):
            for node2 in self.customers:
                self.distances[(node1.code, node2.code)] = self.distance(node1.lat, node2.lat, node1.long, node2.long)


    # Get the cost of a solution
    def cost_function(self, solution, numberVehicles = 1, omega = 0):
        total_distance = 0
        for i in range(len(solution)-1):
            total_distance += self.distances[(solution[i][1], solution[i+1][1])]
        return omega*numberVehicles + total_distance

    #
    ## Get distance from lat and long values.
    def distance(self, lat1, lat2, lon1, lon2):
        
        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
        c = 2 * asin(sqrt(a))
        
        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371
        
        # calculate the result
        return(c * r)


    def load_customers(self):
        customers = []
        customers_xls = pd.ExcelFile(r"bd/2_detail_table_customers.xls")
        customers_parsed = customers_xls.parse(0) 
        for index, customer in customers_parsed.iterrows():
            customers.append(node(customer['CUSTOMER_NUMBER'], customer['CUSTOMER_CODE'],
            customer['TOTAL_WEIGHT_KG'], customer['TOTAL_VOLUME_M3'], customer['CUSTOMER_TIME_WINDOW_FROM_MIN'],
            customer['CUSTOMER_TIME_WINDOW_TO_MIN'], customer['CUSTOMER_LATITUDE'], customer['CUSTOMER_LONGITUDE']))
        customers.append(node(0, 0, 0, 0, 0, 0, 43.37391833, 17.60171712))
        return customers

    def generate_neighborhood(self, solution, numberNeighbors = 5, switchNodes = 5):
        neighborhood = []

        for neighbor in range(numberNeighbors):
            is_possible_solution = False
            while not is_possible_solution:
                new_solution = solution.copy()
                is_possible_solution = True
                current_capacity = self.vehicle_capacity
                for node in range(switchNodes):
                    node1, node2 = random.randint(0, len(new_solution)-1), random.randint(0, len(new_solution)-1)

                    while node1 == node2:
                        node1, node2 = random.randint(0, len(new_solution)-1), random.randint(0, len(new_solution)-1)
                    new_solution[node1], new_solution[node2] = new_solution[node2], new_solution[node1]

                for customer in new_solution:
                    if customer == (0, 0, 0):
                        current_capacity = self.vehicle_capacity
                    else:
                        current_capacity -= self.customers[customer[2]].vol
                    if current_capacity < 0:
                        is_possible_solution = False

            neighborhood.append(new_solution)
        
        return neighborhood

    def generate_initial_solution(self):
        customers_clone = self.customers.copy()

        solution = [(0,0,0)]
        current_capacity = self.vehicle_capacity

        while len(customers_clone) > 0:
            node_elt = customers_clone.pop(random.randint(0,len(customers_clone)-1))

            if current_capacity - node_elt.vol < 0:
                current_capacity = self.vehicle_capacity
                solution.append((0,0,0))    

            solution.append((node_elt.number, node_elt.code, self.customers.index(node_elt)))
            current_capacity -= node_elt.vol
        return solution

    # visited = {}
    # solution = []
    # current_capacity = capacity
    # n_customers = len(customers)
    # for customer in customers:
    #     visited[(customer.number, customer.code, )] = 0
    
    # solution.append((0, 0, 0))
    # visited[(0, 0, 0)] = 1

    # for i in range(n_customers):
    #     new = random.randint(0, n_customers-1)
    #     while (visited[(customers[new].number, customers[new].code, new)] == 1):
    #         new = random.randint(0, n_customers-1)
        
    #     if (customers[new].vol > current_capacity):
    #         solution.append((0, 0, 0))
    #         current_capacity = capacity
       
    #     solution.append((customers[new].number, customers[new].code, new))
    #     current_capacity -= customers[new].vol

    # return solution
        
    
