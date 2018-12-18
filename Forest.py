#this file will create the forest
from Node import *
import math
import multiprocessing as mp



def Generate_forest(popsize, forest_type):
    pool = mp.Pool(processes=5)
    pop_per_process = int(popsize/5)
    temp = []
    if forest_type == 'RampedForest':
        treeList = [pool.apply(RampedForest, args=(popsize/5,[]))]
    #elif forest_type == 'FullForest':
    #    pass
    #elif forest_type == 'GrowForest':
    #    pass
    #else:
    #    print("Invalid initialization, quiting...")
    return treeList

def RampedForest(popsize, treeList):
    full_size = math.ceil(popsize/2)
    grow_size = popsize - full_size
    full = []
    grow = []
    print("ok")
    for i in range(0, full_size):
        print("ok2")
        t = Node().full(0)
        print("ok3")
        full.append(t, t.number_of_nodes(), t.calculate(0, False))
    for i in range(0, grow_size):
        t = Node().growth(0)
        grow.append(t, t.number_of_nodes(), t.calculate(0, False))    
    treeList = sorted(full + grow, key=lambda x: x[1])



