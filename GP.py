from Tree import set_data
from DataHandler import *
from Forest import ramped_forest
from Selection import select, elitism, tournament, double_tournament
from ReproductionHandler import Generate_Offsprings, apply_operators
import time
import sys
import pickle as cPickle
import tensorflow as tf
from SavingHandler import *

import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'



nruns = 1
popsize = 500
tsize = 5
ngens = 100
resume = False
tournament_type = "tournament"
tournament_size = 5
forest_type = 'ramped_forest'

csvname = "breast_cancer_wis.csv"
savename = "Maria"
loadname = "lastgenSara.p"
sheetname = "bcw"
dsetpath = '.' + os.sep + 'datasets'

dset = os.path.join(dsetpath, csvname)
savepopdir = '.' + os.sep + 'individuals'
savesheetdir = '.' + os.sep + 'sheets'
# load = os.path.join(fpath,loadname)
sys.setrecursionlimit(100000)


#training_x, training_y, test_x, test_y = load_data(dset)

def main():

    rmselist = []
    appendrmse = rmselist.append
    acclist = []
    appendacl = acclist.append
    tacclist = []
    appendtacl = tacclist.append
    nodelist = []
    appendnl = nodelist.append

    run = 0
    start_time = time.time()
    while run < nruns:
        print("Parsing Data...")
        training_x, training_y, test_x, test_y = load_data(dset)
        set_data(training_x, training_y, test_x, test_y)
        print("number of run: ",run, '\n')
        cgen = 0
        if not resume:
            treelist = ramped_forest(popsize)
        else:
            # treelist = cPickle.load(open(load, "rb"))
            pass
        while cgen < ngens:
            print("gen number : ",cgen)

            chosen = double_tournament(tournament(treelist, popsize, tournament_size), popsize)
            offspring = apply_operators(chosen, popsize, [])
            newgen = elitism(treelist, offspring, popsize)
            treelist = newgen

            calctest = treelist[0].root.calculate(0, True)
            acc = treelist[0].root.accuracy(treelist[0].globalvalue)
            tacc = treelist[0].root.test_accuracy(calctest)

            print("RMSE: ", treelist[0].fit)
            print("size: ", treelist[0].size)
            print("Training Accuracy: ", acc)
            print("Test Accuracy: ", tacc, '\n')

            #appendrmse(treelist[0][2])
            #appendacl(acc)
            #appendtacl(tacc)
            #appendnl(treelist[0][0].size)

            #save_best(savepopdir, savename + str(run) + str(cgen), [treelist[0]])

            cgen += 1

        #save_spreadsheet(savesheetdir, sheetname + str(run), [rmselist, acclist, tacclist, nodelist])
        rmselist.clear()
        acclist.clear()
        tacclist.clear()
        nodelist.clear()

        run += 1
        #treelist[0][0].print_tree()
    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    main()