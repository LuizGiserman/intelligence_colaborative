from distutils.sysconfig import customize_compiler
from node import node
import numpy as np
import utilities as util
import pandas as pd


customers_xls = pd.ExcelFile(r"bd/2_detail_table_customers.xls") #use r before absolute file path 
customers_parsed = customers_xls.parse(0) 



# a = node(1, 1, 0, 1, 50.6063978, 3.1360337)
# b = node (1, 1, 1, 0, 50.61696744944052, 3.131022834587549)

# graph_nodes = [a, b]

customers = []
customers_parsed.reset_index()
for index, customer in customers_parsed.iterrows():
    customers.append(node(customer['CUSTOMER_NUMBER'], customer['CUSTOMER_CODE'],
    customer['TOTAL_WEIGHT_KG'], customer['TOTAL_VOLUME_M3'], customer['CUSTOMER_TIME_WINDOW_FROM_MIN'],
    customer['CUSTOMER_TIME_WINDOW_TO_MIN'], customer['CUSTOMER_LATITUDE'], customer['CUSTOMER_LONGITUDE']))


#customers are starting in 0 in this list
## although the customer number starts in 1
distances = []

# creates a triangular matrix to save the distances
## saves half of it in order to optimize the utilized space
for i, node1 in enumerate(customers):
    aux = []
    for node2 in customers[i:]:
        aux.append(util.distance(node1.lat, node2.lat, node1.long, node2.long))
    distances.append(aux)


print(customers[3-1].get_distance(1, distances))

