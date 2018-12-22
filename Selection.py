import Node
from Node import D
import random


def Elitism(parents, offspring, popsize):
    newgen = sorted(parents + offspring, key=lambda x: x[1])
    return newgen[:popsize]



def tournament(parents, popsize, tsize):
    chosen = []
    while(len(chosen) < popsize):
        r = [random.randint(0,popsize-1) for x in range(0,tsize)]
        chosen.append(parents[min(r)])
    return chosen


def doubleTournament(parents, popsize):
    chosen = []
    parents = sorted(parents, key=lambda x: x[2])
    while (len(chosen) < popsize):
        r = [random.randint(0, popsize - 1) for x in range(0, 2)]
        if random.random() < D:
            chosen.append(parents[min(r)])
        else:
            chosen.append(parents[max(r)])
    chosen = sorted(chosen, key=lambda x: x[1])
    return chosen

