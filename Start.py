import Node as n
from Data_Handler import *
import time
import sys
import os.path
import Node as n
import pickle as cPickle
import tensorflow as tf
import Forest as forest



nruns = 30
popsize = 500                               # tamanho da populacao
tsize = 5                                   # tamanho do torneio
ngens = 100                                  # numero de geracoes
ttype = 2                                   # tipo de tornei, 1 -> standard, 2 -> double
resume = False
csvname = "sample.csv"                       # nome do dataset
savename = "hrtSINGULAR"                         # nome do ficheiro a gravar
loadname = "lastgenSara.p"                         # nome do ficheiro a carregar
graphname = "hrtSINGULAR"
dsetpath = "F:\\GEEGP\\datasets"              #
fpath = "F:\GEEGP\STGP\individuals"              #
graphpath = "F:\GEEGP\STGP\graphs"
dset = os.path.join(dsetpath, csvname)      #
save = os.path.join(fpath,savename)         #
load = os.path.join(fpath,loadname)         #
sys.setrecursionlimit(100000)

tf.enable_eager_execution()
training_x, training_y, test_x, test_y = load_data(dset)


def main():


    t = n.Node().full(0)
    #t.printTree()
    #print('\n', '\n')
    #c = t.calculate(0, False)
    #print(t.fitness(c))
    #print('\n', '\n')
    #print(t.accuracy(c))

    #treelist = forest.Generate_forest(500, 'RampedForest')

    #print(treelist, '\n')
    #print(len(treelist), '\n')
    #print(treelist[0][0].printTree(),'\n')
    #print(treelist[0][3],'\n')
    #print(treelist[0][1])



if __name__ == "__main__":
    main()