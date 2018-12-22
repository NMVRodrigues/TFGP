from Node import *
import random
from Genetic_Operators import mutation, crossover
import copy
import time
import multiprocessing as mp
import itertools



def Generate_Offsprings(parents, popsize):
    start_time = time.time()
    pool = mp.Pool(processes=5)
    pop_per_process = int(popsize/5)
    offsprings =  pool.starmap(Apply_ops, ((parents,pop_per_process, []), (parents,pop_per_process, []),
                (parents,pop_per_process, []), (parents,pop_per_process, []),(parents,pop_per_process, [])))
        
    offsprings = list(itertools.chain.from_iterable(offsprings))
    print("--- %s seconds1 ---" % (time.time() - start_time))
    offsprings = sorted(offsprings, key=lambda x: x[1])
   
    return offsprings



def Apply_ops(parents, popsize,offspring):
    appendof = offspring.append
    while(len(offspring) < popsize):
        if len(parents) >= 2:
            if random.random() <= MUTATIONPERCENT:
                (x, _, _, _, _ ) = parents[random.randint(0,len(parents)-1)]
                parent = copy.deepcopy(x)
                mutation(parent)
                appendof((parent,parent.fitness(), parent.number_of_nodes(),
                                  parent.accuracy(), parent.testAccuracy()))
            else:
                (x1, _, _, _, _) = parents[random.randint(0, len(parents)-1)]
                parent1 = copy.deepcopy(x1)
                (x2, _, _, _, _) = parents[random.randint(0, len(parents)-1)]
                parent2 = copy.deepcopy(x2)
                crossover(parent1,parent2)
                appendof((parent1, parent1.fitness(), parent1.number_of_nodes(),
                                  parent1.accuracy(), parent1.testAccuracy()))
                appendof((parent2, parent2.fitness(), parent2.number_of_nodes(),
                                  parent2.accuracy(), parent2.testAccuracy()))
        else:
            (x, _, _, _, _) = parents[random.randint(0, len(parents)-1)]
            parent = copy.deepcopy(x)
            mutation(parent)
            appendof((parent, parent.fitness(), parent.number_of_nodes(),
                              parent.accuracy(), parent.testAccuracy()))
    return offspring