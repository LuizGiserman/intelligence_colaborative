##############################
## Ecole Centrale de Lille   #  
## ICO - 2022                #
## FABIAO GISERMAN Luiz      #
## GONZAGA MONTEIRO Mario    #
### Copyright Luiz&MarioSA 📚#
##############################


from cmath import inf
import numpy as np
import random

taches = [(6, 1, 5), (3, 5, 8), (10, 4, 1), (14, 6, 3), (5, 10, 6), (9, 6, 10), (7, 9, 12), (11, 8, 9), (2, 6, 6), (3, 1, 7)]
num_tasks = len(taches)

def get_c_max (sequence, taches):

    sequence_process = list(np.zeros((10, 3)))

    sumMa = 0
    for i in range(num_tasks) :
        #get all of the times concerning the 1st machine.
        sumMa += taches[sequence[i]][0]
        sequence_process[i][0] = sumMa

    for n in range(3 - 1):
        for i in range(num_tasks):
            if (i > 0):
                t_init = max(sequence_process[i-1][1 + n], sequence_process[i][0 + n])
            else:
                t_init = sequence_process[i][0 + n]
        
            sequence_process[i][1 + n] = t_init + taches[sequence[i]][1 + n]

    print ("Sequence: ", sequence)
    print("C_max =", sequence_process[-1][-1])
    return sequence_process[-1][-1]

def get_priority(taches_):
    min_time = sum(list(taches_[0]))
    place = 0
    for i, times in enumerate(taches_):
        current = sum(list(times))
        if sum(list(times)) < min_time:
            min_time = current
            place = i

    return place



def liste(taches):

    copy_taches = taches.copy()
    num_inserted = 0
    pos = None
    U = []

    while num_inserted != num_tasks:
        pos = get_priority(copy_taches)
        copy_taches[pos] = (inf, inf, inf)
        U.append(pos)
        num_inserted += 1
    
    print (U)
    return U

def johnson_2(taches):
    u = []
    v = []
    for i, tache in enumerate(taches):
        if (tache[0] < (tache[1] + tache[2])):
            u.append((i, tache[0]))
        else:
            v.append((i, (tache[1] + tache[2])))
    
    u.sort(key=lambda tup: tup[1])
  
    v.sort(key=lambda tup: tup[1], reverse=True)

    total1 = [x[0] for x in u]
    total2 = [x[0] for x in v]
    total = total1 + total2
    
    print (total)
    return total


## Get 2 random positions to swap within the previous sequence of tasks.
###Calculate c_max for each sequence and keep the optimal value within the solutions
def voisinage(taches):
    seq_inicial = [x for x in range(num_tasks)]
    num_iters = 5
    index = 0
    best_cmax = get_c_max(seq_inicial, taches)
    best_seq = seq_inicial
    while index < num_iters:
        first, second = random.randint(0, num_tasks-1), random.randint(0, num_tasks-1)
        if (first != second):
            seq_inicial[first], seq_inicial[second] = seq_inicial[second], seq_inicial[first]
            index += 1
            new_seq_c = get_c_max(seq_inicial, taches)
            if (new_seq_c < best_cmax):
                print ("entrou")
                best_seq = seq_inicial.copy()
                best_cmax = new_seq_c
    
    print (best_seq)
    print (best_cmax)
    return best_seq
