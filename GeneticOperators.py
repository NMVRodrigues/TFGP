from Tree import *
import copy
import random


# performs the mutation operator
def mutation(parent):
    chosen = random.randint(0, parent.size-1)
    parent.root.mutate(chosen)

    parent.size = parent.root.number_of_nodes()

    calculated = parent.root.calculate(0, False)
    parent.globalvalue = calculated

    parent.fit = parent.root.fitness(calculated)

    return parent


def crossover(t1, t2):
    chosen1 = random.randint(0, t1.size - 1)
    chosen2 = random.randint(0, t2.size - 1)
    parent1 = t1.root.get_node(chosen1)
    parent2 = t2.root.get_node(chosen2)
    refact_tree(parent1, parent2)

    t1.size = t1.root.number_of_nodes()
    t2.size = t2.root.number_of_nodes()

    calculated1 = t1.root.calculate(0, False)
    t1.globalvalue = calculated1
    calculated2 = t2.root.calculate(0, False)
    t2.globalvalue = calculated2

    t1.fit = t1.root.fitness(calculated1)
    t2.fit = t2.root.fitness(calculated2)

    return t1, t2


def refact_tree(n1, n2):
    temp = copy.deepcopy(n1)
    n1.value = n2.value
    n1.left = n2.left
    n1.right = n2.right
    n2.value = temp.value
    n2.left = temp.left
    n2.right = temp.right
    return n1, n2
