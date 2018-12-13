import Node as n
from Data_Handler import *
import time
import sys
import os.path
import Node as n
import pickle as cPickle



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
    # Read the dataset
    X, Y, features = load_data(dset)
    # normalizes the labels
    Y = normalizelabels(Y)
    X = sci2floatFeatures(X)
    # Shuffle the dataset to mix up the rows.
    X, Y = shuffle(X, Y, random_state=1)
    # splits the dataste into test and training parts
    training_x, test_x, training_y, test_y = train_test_split(X, Y, test_size=0.20, random_state=415)




    n.setTrainingCols(training_x)
    n.setTrainingLabels(training_y)
    n.setTestCols(test_x)
    n.setTestLabels(test_y)

    t = n.Node().full(0)
    t.printTree()


if __name__ == "__main__":
    main()