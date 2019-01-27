import Node as n
from Data_Handler import *
from Forest import Generate_forest
from Selection import select, Elitism
from Reproduction_Handler import Generate_Offsprings
import time
import sys
import os.path
import Node as n
import pickle as cPickle
import tensorflow as tf
import Forest as forest



tf.enable_eager_execution()

nruns = 1
popsize = 500                             # tamanho da populacao
tsize = 5                                   # tamanho do torneio
ngens = 100     
resume = False                             # numero de geracoes
tournament_type = "tournament"
tournament_size = 5
forest_type = 'RampedForest'                                   # tipo de tornei, 1 -> standard, 2 -> double

csvname = "heart_processed.csv"                       # nome do dataset
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


training_x, training_y, test_x, test_y = load_data(dset)

def main():

    #print("nlabels: ", len(training_y.numpy()), '\n')

    run = 0
    start_time = time.time()
    while run < nruns:
        print("number of run: ",run, '\n')
        cgen = 0
        if not resume:
            treelist = Generate_forest(popsize, forest_type)
        else:
            treelist = cPickle.load(open(load, "rb"))
        while cgen < ngens:
            print("gen number : ",cgen)
            chosen = select(treelist, tournament_type, popsize, tournament_size)
            offspring = Generate_Offsprings(chosen,popsize)
            newgen = Elitism(treelist,offspring,popsize)
            treelist = newgen
            print("RMSE: ", treelist[0][1])
            print("size: ", treelist[0][3])
            print("Training Accuracy: ", treelist[0][0].accuracy(treelist[0][2]), '\n')
            #print("Test Accuracy: ", treelist[0][0].testAccuracy(treelist[0][2]), '\n')
            cgen += 1
        run += 1
    #treelist[0][0].printTree()
    print("--- %s seconds ---" % (time.time() - start_time))

    #t = n.Node().full(0)
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