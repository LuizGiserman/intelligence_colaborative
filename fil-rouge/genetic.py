import utilities as util

def selection (pop_before) :
    return pop_before[:int(len(pop_before)/2)]

def pairing (len_pop) :
    pairs = []
    for index in range(int(len_pop / 2)):
        pairs.append((index, int(len_pop - index - 1)))
    
    return pairs

def genetic (solutions, distances, max_iterations = 40) :

    pop_before = []
    pop = []
    pairs = []

    for solution in solutions :
            pop_before.append({"individual":solution, "fitness":util.cost_function(solution, distances)})
            

    for index in range(max_iterations) :

        print(len(pop_before))
        pop_before  = sorted(pop_before, key = lambda i: i['fitness'])
        pop = selection(pop_before).copy()

        pairs = pairing(len(pop))

        break






        


    
