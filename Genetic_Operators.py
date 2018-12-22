from Node import *
import copy
import random


# performs the mutation operator
def mutation(node):
    chosen = random.randint(0, node.number_of_nodes()-1)
    node.mutate(chosen)
    return node


def crossover(t1,t2):
    chosen1 = random.randint(0, t1.number_of_nodes() - 1)
    chosen2 = random.randint(0, t2.number_of_nodes() - 1)
    parent1 = t1.getNode(chosen1)
    parent2 = t2.getNode(chosen2)
    refactTree(parent1, parent2)
    return t1,t2


def refactTree(n1,n2):
    temp = copy.deepcopy(n1)
    n1.value = n2.value
    n1.left = n2.left
    n1.right = n2.right
    n2.value = temp.value
    n2.left = temp.left
    n2.right = temp.right
    return n1, n2
