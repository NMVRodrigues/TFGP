import random as rand
from Utils import *
from scipy.stats import pearsonr


def set_data(training_x, training_y, test_x, test_y):
    global cols, ncols, labels, nlabels, tcols, tncols, tlabels, tnlabels
    cols = training_x
    labels = training_y
    tcols = test_x
    tlabels = test_y
    ncols = len(cols)
    nlabels = len(labels.numpy())
    tncols = len(tcols)
    tnlabels = len(tlabels.numpy())


#------------------------------------

biFunctions = ['+', '-', '*', '//']
uniFunctions = ['ln', 'sqrt', 'synapse']
maxDepth = 2




def getCol(x, t):
    if isinstance(x, float):    # se for literal
        if not t:
            return [x for i in range(len(cols[0].numpy()))]
        else:
            return [x for i in range(len(tcols[0].numpy()))]
    else:
        if not t:
            return cols[x]
        else:
            return tcols[x]

class Tree(object):
    def __init__(self):
        self.size = 0
        self.globalvalue = 0
        self.fit = 0
        self.root = None

class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    # checks if self is leaf
    def is_leaf(self):
            return self.left is None

    # TODO pruning the tree
    def prune(self):
        pass

    # creates a tree using the full method
    def full(self, depth):
        if depth == maxDepth:
            # > 3 to remove literal chances
            if rand.random() > 3:
                self.value = rand.random()
            else:
                self.value = rand.randint(0, ncols - 1)
        else:
            self.value = rand.choice(biFunctions)
            self.left = Node().full(depth+1)
            self.right = Node().full(depth+1)
        return self

    # creates a tree using the grow method
    def grow(self, depth):
        if depth == maxDepth:
            if rand.random() > 3:   #garante que não ah terminais 
                self.value = rand.random()
            else:
                self.value = rand.randint(0, ncols - 1)
        else:
            if self.left is None:
                if rand.randint(0, 1) == 0:
                    if rand.random() > 3:   # same thing
                        self.value = rand.random()
                    else:
                        self.value = rand.randint(0, ncols - 1)
                else:
                    if rand.randint(0,1) == 0:
                        self.value = rand.choice(uniFunctions)
                        self.left = Node().grow(depth + 1)
                    else:
                        self.value = rand.choice(biFunctions)
                        self.left = Node().full(depth + 1)
                        self.right = Node().full(depth + 1)
            else:
                if rand.randint(0, 1) == 0:
                    self.value = rand.choice(uniFunctions)
                    self.left = Node().grow(depth + 1)
                else:
                    self.value = rand.choice(biFunctions)
                    self.left = Node().full(depth + 1)
                    self.right = Node().full(depth + 1)
        return self

    # gets the number of nodes on the tree
    def number_of_nodes(self):
        return 1 + \
            (self.left.number_of_nodes() if self.left is not None else 0) + \
            (self.right.number_of_nodes() if self.right is not None else 0)

    # returns a node fromt he tree
    def get_node(self, i):
        if i == 0:
            return self
        ls = (self.left.number_of_nodes() if self.left is not None else 0)
        if i - 1 < ls:
            if self.left is not None:
                return self.left.get_node(i - 1)
        else:
            if self.right is not None:
                return self.right.get_node(i - ls - 1)

    # mutates a node by growing it
    def mutate(self, i):
        if i == 0:
            self.grow(0)
            return
        ls = (self.left.number_of_nodes() if self.left is not None else 0)
        if i - 1 < ls:
            if self.left is not None:
                self.left.mutate(i - 1)
        else:
            if self.right is not None:
                self.right.mutate(i - ls - 1)

    # prints the tree
    def print_tree(self):
        print(self.value)
        (self.left.print_tree() if self.left is not None else 0)
        (self.right.print_tree() if self.right is not None else 0)

    # calculates the tree
    def calculate(self, result, test):
        if self.is_leaf():
            result = getCol(self.value, test)
        else:
            if self.value == '+':
                result = self.left.calculate(result, test) + self.right.calculate(result, test)
            elif self.value == '-':
                result = self.left.calculate(result, test) - self.right.calculate(result, test)
            elif self.value == '*':
                result = self.left.calculate(result, test) * self.right.calculate(result, test)
            elif self.value == '//':
                result = divide(self.left.calculate(result, test), self.right.calculate(result, test))
            elif self.value == 'ln':
                result = ln(self.left.calculate(result, test))
            elif self.value == 'sqrt':
                result = sqrt(self.left.calculate(result, test))
            else:
                result = synapse(self.left.calculate(result, test))
        return result

    # RMSE
    # def fitness(self, result):
    #     return tf.sqrt(tf.losses.mean_squared_error(labels,result)).numpy()

    # Pearson correlation
    # def fitness(self, result):
    #     return pearsonr(result.numpy(), labels.numpy())[0] * 100

    def fitness(self, result):
         return (tf.metrics.mean_absolute_error(labels, result)).numpy()

    def test_fitness(self, result):
         return (tf.metrics.mean_absolute_error(tlabels, result)).numpy()