import Tree
#from gp import D
import random
import multiprocessing as mp
import itertools


def elitism(parents, offspring, popsize):
    newgen = sorted(parents + offspring, key=lambda x: x.fit) #rmse
    #newgen = sorted(parents + offspring, key=lambda x: x.fit, reverse=True)
    return newgen[:popsize]

def select(parents, tournament_type, popsize, tournament_size ):
    pool = mp.Pool(processes=5)
    pop_per_process = int(popsize/5)
    chosen =  pool.starmap(tournament, ((parents, pop_per_process, tournament_size), (parents, pop_per_process, tournament_size),
        (parents, pop_per_process, tournament_size), (parents, pop_per_process, tournament_size),
        (parents, pop_per_process, tournament_size)))
    chosen = list(itertools.chain.from_iterable(chosen))

    if tournament_type is "doubletournament":
        chosen =  pool.starmap(double_tournament, ((chosen, pop_per_process), (chosen, pop_per_process),
                                                   (chosen,pop_per_process), (chosen,pop_per_process), (chosen,pop_per_process)))
        chosen = list(itertools.chain.from_iterable(chosen))
        
    pool.close()
    pool.join()
    #print("--- %s seconds1 ---" % (time.time() - start_time))
    chosen = sorted(chosen, key=lambda x: x[1])
   
    return chosen


def tournament(parents, popsize, tsize):
    chosen = []
    append = chosen.append
    while len(chosen) < popsize:
        r = [random.randint(0,popsize-1) for x in range(0,tsize)]
        append(parents[min(r)])
    chosen = sorted(chosen, key=lambda x: x.fit) #emse
    #chosen = sorted(chosen, key=lambda x: x.fit, reverse=True)
    return chosen


def double_tournament(parents, popsize):
    chosen = []
    append = chosen.append
    parents = sorted(parents, key=lambda x: x.size)
    while len(chosen) < popsize:
        r = [random.randint(0, popsize - 1) for x in range(0, 2)]
        if random.random() < 0.7:
            append(parents[min(r)])
        else:
            append(parents[max(r)])
    chosen = sorted(chosen, key=lambda x: x.fit) #rmse
    #chosen = sorted(chosen, key=lambda x: x.fit, reverse=True)
    return chosen

