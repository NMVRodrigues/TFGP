import Node
#from gp import D
import random
import multiprocessing as mp
import itertools


def Elitism(parents, offspring, popsize):
    newgen = sorted(parents + offspring, key=lambda x: x[1])
    return newgen[:popsize]

def select(parents, tournament_type, popsize, tournament_size ):
    pool = mp.Pool(processes=5)
    pop_per_process = int(popsize/5)
    chosen =  pool.starmap(tournament, ((parents, pop_per_process, tournament_size), (parents, pop_per_process, tournament_size),
        (parents, pop_per_process, tournament_size), (parents, pop_per_process, tournament_size),
        (parents, pop_per_process, tournament_size)))
    chosen = list(itertools.chain.from_iterable(chosen))

    if tournament_type is "doubletournament":
        chosen =  pool.starmap(doubleTournament, ((chosen,pop_per_process), (chosen,pop_per_process),
                        (chosen,pop_per_process), (chosen,pop_per_process),(chosen,pop_per_process)))
        chosen = list(itertools.chain.from_iterable(chosen))
        
    pool.close()
    pool.join()
    #print("--- %s seconds1 ---" % (time.time() - start_time))
    chosen = sorted(chosen, key=lambda x: x[1])
   
    return chosen

def tournament(parents, popsize, tsize):
    chosen = []
    while(len(chosen) < popsize):
        r = [random.randint(0,popsize-1) for x in range(0,tsize)]
        chosen.append(parents[min(r)])
    return chosen


def doubleTournament(parents, popsize):
    chosen = []
    parents = sorted(parents, key=lambda x: x[3])
    while (len(chosen) < popsize):
        r = [random.randint(0, popsize - 1) for x in range(0, 2)]
        if random.random() < 0.7:
            chosen.append(parents[min(r)])
        else:
            chosen.append(parents[max(r)])
    chosen = sorted(chosen, key=lambda x: x[1])
    return chosen

