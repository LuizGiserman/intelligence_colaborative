from locale import currency
from math import radians, cos, sin, asin, sqrt
from node import node
import pandas as pd
import random

# Get the cost of a solution
def cost_function(solution, distances, numberVehicles = 1, omega = 0):
    total_distance = 0
    for i in range(len(solution)-1):
        total_distance += distances[(solution[i][1], solution[i+1][1])]
    return omega*numberVehicles + total_distance

#
## Get distance from lat and long values.
def distance(lat1, lat2, lon1, lon2):
     
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


def load_customers():
    customers = []
    customers_xls = pd.ExcelFile(r"bd/2_detail_table_customers.xls")
    customers_parsed = customers_xls.parse(0) 
    for index, customer in customers_parsed.iterrows():
        customers.append(node(customer['CUSTOMER_NUMBER'], customer['CUSTOMER_CODE'],
        customer['TOTAL_WEIGHT_KG'], customer['TOTAL_VOLUME_M3'], customer['CUSTOMER_TIME_WINDOW_FROM_MIN'],
        customer['CUSTOMER_TIME_WINDOW_TO_MIN'], customer['CUSTOMER_LATITUDE'], customer['CUSTOMER_LONGITUDE']))
    customers.append(node(0, 0, 0, 0, 0, 0, 43.37391833, 17.60171712))
    return customers

def crossing_over(solution1, solution2, customers, vehicle_capacity=20):
    child1 = [i for i in solution1 if i != (0,0,0)]
    child2 = [i for i in solution2 if i != (0,0,0)]
    
    end_point = len(child1)-1
    start_point = random.randint(0, end_point-1)

    child1[start_point : end_point+1], child2[start_point : end_point+1] = child2[start_point : end_point+1], child1[start_point : end_point+1]

    outside = []
    for i in child1:
        if not i in child2:
            outside.append(i)
    for i in range(len(child2)-1):
        if child2[i] in child2[i+1:]:
            child2[i] = outside.pop()
    
    current_capacity = vehicle_capacity
    child = []
    for gene in child2:
        if current_capacity - customers[gene[2]].vol < 0:
            current_capacity = vehicle_capacity
            child.append((0,0,0))    

        child.append(gene)
        current_capacity -= customers[gene[2]].vol
    
    return child

def generate_neighborhood(solution, customers, vehicleCapacity, numberNeighbors = 5, switchNodes = 5):
    neighborhood = []

    for neighbor in range(numberNeighbors):
        is_possible_solution = False
        while not is_possible_solution:
            new_solution = solution.copy()
            is_possible_solution = True
            current_capacity = vehicleCapacity
            for node in range(switchNodes):
                node1, node2 = random.randint(0, len(new_solution)-1), random.randint(0, len(new_solution)-1)

                while node1 == node2:
                    node1, node2 = random.randint(0, len(new_solution)-1), random.randint(0, len(new_solution)-1)
                new_solution[node1], new_solution[node2] = new_solution[node2], new_solution[node1]

            for customer in new_solution:
                if customer == (0, 0, 0):
                    current_capacity = vehicleCapacity
                else:
                    current_capacity -= customers[customer[2]].vol
                if current_capacity < 0:
                    is_possible_solution = False

        neighborhood.append(new_solution)
    
    return neighborhood

def generate_initial_solution(capacity, customers):
    customers_clone = customers.copy()

    solution = [(0,0,0)]
    current_capacity = capacity

    while len(customers_clone) > 0:
        node_elt = customers_clone.pop(random.randint(0,len(customers_clone)-1))

        if current_capacity - node_elt.vol < 0:
            current_capacity = capacity
            solution.append((0,0,0))    

        solution.append((node_elt.number, node_elt.code, customers.index(node_elt)))
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
        
    
