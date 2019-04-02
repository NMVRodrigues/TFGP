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
                (x, _, _) = parents[random.randint(0,len(parents)-1)]
                parent = copy.deepcopy(x)
                mutation(parent)
                n = parent.number_of_nodes()
                c = parent.calculate(0, False)
                f = parent.fitness(c)
                parent.size = n
                appendof((parent, c, f))
            else:
                (x1, _, _) = parents[random.randint(0, len(parents)-1)]
                parent1 = copy.deepcopy(x1)
                (x2, _, _) = parents[random.randint(0, len(parents)-1)]
                parent2 = copy.deepcopy(x2)
                crossover(parent1,parent2)
                n1 = parent1.number_of_nodes()
                c1 = parent1.calculate(0, False)
                f1 = parent1.fitness(c1)
                parent1.size = n1
                n2 = parent2.number_of_nodes()
                c2 = parent2.calculate(0, False)
                f2 = parent2.fitness(c2)
                parent2.size = n2
                appendof((parent1, c1, f1))
                appendof((parent2, c2, f2))
        else:
            (x, _, _) = parents[random.randint(0, len(parents)-1)]
            parent = copy.deepcopy(x)
            mutation(parent)
            n = parent.number_of_nodes()
            c = parent.calculate(0, False)
            f = parent.fitness(c)
            parent.size = n
            appendof((parent, c, f))
    offspring = sorted(offspring, key=lambda x: x[2])
    return offspring
