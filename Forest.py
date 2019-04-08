#this file will create the forest
import Tree as t
import math
import multiprocessing as mp
import random
import time
import itertools
import sys



# def Generate_forest(popsize, forest_type):
#     start_time = time.time()
#     pool = mp.Pool(processes=5)
#     pop_per_process = int(popsize/5)
#     if forest_type == 'ramped_forest':
#         treeList =  pool.starmap(ramped_forest, ((pop_per_process, []), (pop_per_process, []),
#                                                  (pop_per_process, []), (pop_per_process, []), (pop_per_process, [])))
#         #treeList = pool.starmap(test, ((5, []), (5, []),(5, []), (5, []),(5, [])))
#     elif forest_type == 'full_forest':
#         treeList =  pool.starmap(full_forest, ((pop_per_process, []), (pop_per_process, []),
#                                                (pop_per_process, []), (pop_per_process, []), (pop_per_process, [])))
#     elif forest_type == 'grow_forest':
#         treeList =  pool.starmap(grow_forest, ((pop_per_process, []), (pop_per_process, []),
#                                                (pop_per_process, []), (pop_per_process, []), (pop_per_process, [])))
#     else:
#         print("Invalid initialization, quiting...")
#         exit(0)
#     #start_time = time.time()
#     tree_lst = list(itertools.chain.from_iterable(treeList))
#     print("--- %s seconds1 ---" % (time.time() - start_time))
#     #start_time = time.time()
#     #tree_lst = [x for x in itertools.chain.from_iterable(treeList)]
#     #print("--- %s seconds2 ---" % (time.time() - start_time))
#     #start_time = time.time()
#     #lst_iter = iter(treeList)
#     #tree_lst = next(lst_iter)
#     #for inner in lst_iter:
#     #    tree_lst += inner
#     #print("--- %s seconds3 ---" % (time.time() - start_time))
#     tree_lst = sorted(tree_lst, key=lambda x: x[3])
#     return tree_lst


def ramped_forest(popsize):
    full_size = int(math.ceil(popsize/2))
    grow_size = popsize - full_size
    full = full_forest(full_size, [])
    grow = grow_forest(grow_size, [])
    tree_lst = sorted(full+grow, key=lambda x: x.fit) #rmse
    #tree_lst = sorted(full + grow, key=lambda x: x.fit, reverse=True)
    return tree_lst


def full_forest(popsize, tree_lst):
    append = tree_lst.append
    for _ in range(popsize):
        tree = t.Tree()
        sub_tree = t.Node().full(0)
        tree.size = sub_tree.number_of_nodes()
        calculated = sub_tree.calculate(0, False)
        print(calculated, '\n')
        print(calculated.numpy())
        sys.exit()
        tree.globalvalue = calculated
        tree.fit = sub_tree.fitness(calculated)
        tree.root = sub_tree
        append(tree)
    return tree_lst


def grow_forest(popsize, tree_lst):
    append = tree_lst.append
    for _ in range(popsize):
        tree = t.Tree()
        sub_tree = t.Node().grow(0)
        tree.size = sub_tree.number_of_nodes()
        calculated = sub_tree.calculate(0, False)
        tree.globalvalue = calculated
        tree.fit = sub_tree.fitness(calculated)
        tree.root = sub_tree
        append(tree)
    return tree_lst






