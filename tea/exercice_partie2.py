from cmath import inf


taches = [(6, 1, 5), (3, 5, 8), (10, 4, 1), (14, 6, 3), (5, 10, 6), (9, 6, 10), (7, 9, 12), (11, 8, 9), (2, 6, 6), (3, 1, 7)]
num_tasks = len(taches)

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

def get_c_max (sequence):
    m1, m2, m3 = 0, 0, 0
    temps_total = 0

    tache = sequence.pop()
    temps_total = tache[0]
    m2 = tache[1]
    while sequence:
        tache_ = sequence[0]
        if m1 == 0:
            sequence.pop()
            m1 = tache_[0]
        
johnson_2(taches)