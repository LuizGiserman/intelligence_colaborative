from math import radians, cos, sin, asin, sqrt
from re import X
from node import node
import pandas as pd

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
    customers.append(node(0, 0, 0, 0, 0, 0, 0, 43,37391833, 17,60171712))
    return customers