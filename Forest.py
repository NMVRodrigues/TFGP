#this file will create the forest
import Node as n
import math
import multiprocessing as mp
import random
import time
import itertools



def Generate_forest(popsize, forest_type):
    start_time = time.time()
    pool = mp.Pool(processes=5)
    pop_per_process = int(popsize/5)
    if forest_type == 'RampedForest':
        treeList =  pool.starmap(RampedForest, ((pop_per_process, []), (pop_per_process, []),
                    (pop_per_process, []), (pop_per_process, []),(pop_per_process, [])))
        #treeList = pool.starmap(test, ((5, []), (5, []),(5, []), (5, []),(5, [])))
    elif forest_type == 'FullForest':
        treeList =  pool.starmap(FullForest, ((pop_per_process, []), (pop_per_process, []),
                    (pop_per_process, []), (pop_per_process, []),(pop_per_process, [])))
    elif forest_type == 'GrowForest':
        treeList =  pool.starmap(GrowForest, ((pop_per_process, []), (pop_per_process, []),
                    (pop_per_process, []), (pop_per_process, []),(pop_per_process, [])))
    else:
        print("Invalid initialization, quiting...")
        exit(0)
    #start_time = time.time()
    tree_lst = list(itertools.chain.from_iterable(treeList))
    print("--- %s seconds1 ---" % (time.time() - start_time))
    #start_time = time.time()
    #tree_lst = [x for x in itertools.chain.from_iterable(treeList)]
    #print("--- %s seconds2 ---" % (time.time() - start_time))
    #start_time = time.time()
    #lst_iter = iter(treeList)
    #tree_lst = next(lst_iter)
    #for inner in lst_iter:
    #    tree_lst += inner
    #print("--- %s seconds3 ---" % (time.time() - start_time))
    tree_lst = sorted(tree_lst, key=lambda x: x[3])
    return tree_lst

def RampedForest(popsize, tree_lst):
    full_size = int(math.ceil(popsize/2))
    grow_size = popsize - full_size
    append = tree_lst.append
    for _ in range(full_size):
        t = n.Node().full(0)
        nn = t.number_of_nodes()
        c = t.calculate(0, False)
        f = t.fitness(c)
        append((t,f,c,nn))
    for _ in range(grow_size):
        t = n.Node().full(0)
        nn = t.number_of_nodes()
        c = t.calculate(0, False)
        f = t.fitness(c)
        append((t,f,c,nn))
    tree_lst = sorted(tree_lst, key=lambda x: x[1])
    return tree_lst

def FullForest(popsize, tree_lst):
    append = tree_lst.append
    for _ in range(popsize):
        t = n.Node().full(0)
        nn = t.number_of_nodes()
        c = t.calculate(0, False)
        f = t.fitness(c)
        append((t,nn,c,f))
    return tree_lst

def GrowForest(popsize, tree_lst):
    append = tree_lst.append
    for _ in range(popsize):
        t = n.Node().full(0)
        nn = t.number_of_nodes()
        c = t.calculate(0, False)
        f = t.fitness(c)
        append((t,nn,c,f))
    return tree_lst


#def test(popsize, treelist):
#    r = random.randint(0,5)
#    for i in range(popsize):
#        treelist.append(r)
#    return treelist



