#this file will create the forest
from Node import *
import math

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



def generatepop(popsize):
    treeList = []
    for i in range(0, popsize):
        t = Node()
        t.full(0) if rand.randint(0, 1) == 0 else t.growth(0)
        treeList.append((t, t.fitness(), t.number_of_nodes(), t.accuracy(), t.testAccuracy()))
    treeList = sorted(treeList, key=lambda x: x[1])
    return treeList