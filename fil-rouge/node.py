class node:

    def __init__(self, number, code, kg, vol, start, end, lat, long):
        self.number = number
        self.code = code
        self.kg = kg
        self.vol = vol
        self.start = start
        self.end = end
        self.lat = lat
        self.long = long

    ## Get distance in the triangular matrix that only stores half of itself
    def get_distance(self, destination_number, distance_matrix):
        if (destination_number > self.number):
            return distance_matrix[self.number-1][(destination_number-1)-(self.number-1)]
        else:
            return distance_matrix[destination_number-1][(self.number-1)-(destination_number-1)]
    