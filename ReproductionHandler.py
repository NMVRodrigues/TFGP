from Tree import *
#from gp import MUTATIONPERCENT, CROSSOVERPERCENT
import random
from GeneticOperators import mutation, crossover
import copy
import multiprocessing as mp
import itertools

MUTATIONPERCENT = 0.05      # probabilidade de mutacao
CROSSOVERPERCENT = 0.95     # probabilidade de crossover



def Generate_Offsprings(parents, popsize):
    #start_time = time.time()
    pool = mp.Pool(processes=5)
    pop_per_process = int(popsize/5)
    offsprings =  pool.starmap(apply_operators, ((parents, pop_per_process, []), (parents, pop_per_process, []),
                                                 (parents,pop_per_process, []), (parents,pop_per_process, []), (parents,pop_per_process, [])))

    pool.close ()
    pool.join()
    offsprings = list(itertools.chain.from_iterable(offsprings))
    #print("--- %s seconds1 ---" % (time.time() - start_time))
    offsprings = sorted(offsprings, key=lambda x: x[1])
   
    return offsprings


def apply_operators(parents, popsize, offspring):
    appendof = offspring.append
    while len(offspring) < popsize:
        if len(parents) >= 2:
            if random.random() <= MUTATIONPERCENT:
                p = parents[random.randint(0, len(parents) - 1)]
                parent = copy.deepcopy(p)
                mutation(parent)
                appendof(p)
            else:
                p1 = parents[random.randint(0, len(parents) - 1)]
                parent1 = copy.deepcopy(p1)
                p2 = parents[random.randint(0, len(parents) - 1)]
                parent2 = copy.deepcopy(p2)
                crossover(parent1, parent2)
                appendof(parent1)
                appendof(parent2)
        else:
            p = parents[random.randint(0, len(parents) - 1)]
            parent = copy.deepcopy(p)
            mutation(parent)
            appendof(p)
    offspring = sorted(offspring, key=lambda x: x.fit) #rmse
    #offspring = sorted(offspring, key=lambda x: x.fit, reverse=True)
    return offspring
