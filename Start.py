import Node as n
from Data_Handler import *
import time
import sys
import os.path
import Node as n
import pickle as cPickle
import tensorflow as tf



nruns = 30
popsize = 500                               # tamanho da populacao
tsize = 5                                   # tamanho do torneio
ngens = 100                                  # numero de geracoes
ttype = 2                                   # tipo de tornei, 1 -> standard, 2 -> double
resume = False
csvname = "heart.csv"                       # nome do dataset
savename = "hrtSINGULAR"                         # nome do ficheiro a gravar
loadname = "lastgenSara.p"                         # nome do ficheiro a carregar
graphname = "hrtSINGULAR"
dsetpath = "F:\GEEGP\datasets"              #
fpath = "F:\GEEGP\STGP\individuals"              #
graphpath = "F:\GEEGP\STGP\graphs"
dset = os.path.join(dsetpath, csvname)      #
save = os.path.join(fpath,savename)         #
load = os.path.join(fpath,loadname)         #
sys.setrecursionlimit(100000)



def main():

    tf.enable_eager_execution()
    training_x, training_y, test_x, test_y = load_data(dset)




    n.setTrainingCols(training_x)
    n.setTrainingLabels(training_y)
    n.setTestCols(test_x)
    n.setTestLabels(test_y)

    t = n.Node().full(0)
    t.printTree()


if __name__ == "__main__":
    main()