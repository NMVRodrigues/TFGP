import tensorflow as tf
import random as rand
import copy
import statistics
from TF_Fixes import divide, ln, sqrt
from Start import training_x, training_y, test_x, test_y

cols = training_x
ncols = len(cols)
labels = training_y
nlabels = len(labels.numpy())
tcols = test_x
tncols = len(tcols)
tlabels = test_y
tnlabels = len(tlabels.numpy())


#------------------------------------

biFunctions = ['+', '-', '*', '//']
uniFunctions = ['ln', 'sqrt']
maxDepth = 2
D = 0.7
MUTATIONPERCENT = 0.05      # probabilidade de mutacao
ROSSOVERPERCENT = 0.95     # probabilidade de crossover



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



class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    # checks if self is leaf
    def isLeaf(self):
            return self.left is None and self.right is None

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

    # creates a tree using the growth method
    def growth(self, depth):
        if depth == maxDepth:
            if rand.random() > 3:   #garante que não ah terminais 
                self.value = rand.random()
            else:
                self.value = rand.randint(0, ncols - 1)
        else:
            if self.left == None:
                if rand.randint(0, 1) == 0:
                    if rand.random() > 3:   # same thing
                        self.value = rand.random()
                    else:
                        self.value = rand.randint(0, ncols - 1)
                else:
                    if rand.randint(0,1) == 0:
                        self.value = rand.choice(uniFunctions)
                        self.left = Node().growth(depth+1)
                    else:
                        self.value = rand.choice(biFunctions)
                        self.left = Node().full(depth + 1)
                        self.right = Node().full(depth + 1)
            else:
                if rand.randint(0, 1) == 0:
                    self.value = rand.choice(uniFunctions)
                    self.left = Node().growth(depth + 1)
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
    def getNode(self, i):
        if i == 0:
            return self
        ls = (self.left.number_of_nodes() if self.left is not None else 0)
        if i - 1 < ls:
            if self.left is not None:
                return self.left.getNode(i-1)
        else:
            if self.right is not None:
                return self.right.getNode(i - ls - 1)

    # mutates a node by growing it
    def mutate(self, i):
        if i == 0:
            self.growth(0)
            return
        ls = (self.left.number_of_nodes() if self.left is not None else 0)
        if i - 1 < ls:
            if self.left is not None:
                self.left.mutate(i - 1)
        else:
            if self.right is not None:
                self.right.mutate(i - ls - 1)

    # prints the tree
    def printTree(self):
        print(self.value)
        (self.left.printTree() if self.left is not None else 0)
        (self.right.printTree() if self.right is not None else 0)
        # prints the tree

    #def printTree2(self):
        #print("(  %s  " % self.value, (self.left.printTree2() if self.left is not None else 0),(self.right.printTree2() if self.right is not None else 0),"  )" , end="", flush=True)
    #def printTree2(self):
    #    if self.isLeaf():
    #        print(self.value, end='')
    #    else:
    #        print('( ',self.value, ' ', self.left.printTree2(), ' ', (self.right.printTree2() if self.right is not None else 0), ' )', end='')
        

    # calculates the tree
    def calculate(self, result, test):
        if self.isLeaf():
            result = getCol(self.value, test)
        else:
            op = self.value
            if op == '+':
                result = self.left.calculate(result, test) + self.right.calculate(result, test)
            elif op == '-':
                result = self.left.calculate(result, test) - self.right.calculate(result, test)
            elif op == '*':
                result = self.left.calculate(result, test) * self.right.calculate(result, test)
            elif op == '//':
                result = divide(self.left.calculate(result, test), self.right.calculate(result, test))
            elif op == 'ln':
                result = ln(self.left.calculate(result, test))
            else:
                result = sqrt(self.left.calculate(result, test))
        return result

    # calculates the fitness of the tree
    def fitness(self):
        result = self.calculate(0, False)
        acc = 0
        for i in range(len(result)):
            acc += (float(labels[i]) - float(result[i])) ** 2
        return acc / nlabels

    # calculates the training accuracy
    def accuracy(self):
        correct = 0
        result = self.calculate(0, False)
        for x in range(len(result)):
            if result[x] < 0.5: #TODO -> por isto nos tf fix para nao ter de fazer loop
                r = 0
            else:
                r = 1
            if r == int(labels[x]):
                correct += 1
        return (correct / len(labels)) * 100

    # calculates the test accuracy
    def testAccuracy(self):
        correct = 0
        result = self.calculate(0, True)
        for x in range(len(result)):
            if result[x] < 0.5:
                r = 0
            else:
                r = 1
            if r == int(tlabels[x]):
                correct += 1
        return (correct / len(tlabels)) * 100
