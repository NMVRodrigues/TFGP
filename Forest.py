#this file will create the forest
import Node as n
import math
import multiprocessing as mp
import random
import time



def Generate_forest(popsize, forest_type):
    start_time = time.time()
    pool = mp.Pool(processes=5)
    pop_per_process = int(popsize/5)
    if forest_type == 'RampedForest':
        #treeList = [pool.apply(RampedForest, args=(popsize/5,[]))]
        #treeList = [pool.apply(test, args=(5,[]))]
        treeList = pool.starmap(test, ((5, []), (5, []),(5, []), (5, []),(5, [])))
    #elif forest_type == 'FullForest':
    #    pass
    #elif forest_type == 'GrowForest':
    #    pass
    #else:
    #    print("Invalid initialization, quiting...")
    print("--- %s seconds ---" % (time.time() - start_time))
    return treeList

def RampedForest(popsize, treeList):
    full_size = int(math.ceil(popsize/2))
    grow_size = int(popsize - full_size)
    full = []
    grow = []
    for i in range(0, full_size):
        t = n.Node().full(0)
        full.append((t, t.number_of_nodes(), t.calculate(0, False)))
    for i in range(0, grow_size):
        t = n.Node().growth(0)
        grow.append((t, t.number_of_nodes(), t.calculate(0, False)))    
    treeList = sorted(full + grow, key=lambda x: x[1])
    return treeList


def test(popsize, treelist):
    r = random.randint(0,5)
    for i in range(popsize):
        treelist.append(r)
    return treelist



