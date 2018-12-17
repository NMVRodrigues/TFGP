#this file will create the forest
from Node import *
import math
import threading


def Generate_forest(popsize, forest_type):
    pass


def RampedForest(popsize):
    full_size = math.ceil(popsize/2)
    grow_size = popsize - full_size
    full = []
    grow = []
    for i in range(0, full_size):
        t = Node().full(0)
        full.append(t, t.number_of_nodes, t.calculate())
    for i in range(0, grow_size):
        t = Node().grow(0)
        grow.append(t, t.number_of_nodes, t.calculate())    
    treeList = sorted(full + grow, key=lambda x: x[1])



