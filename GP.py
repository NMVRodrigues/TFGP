import Node as n
from DataHandler import *
from Forest import Generate_forest, ramped_forest
from Selection import select, elitism, tournament, double_tournament
from ReproductionHandler import Generate_Offsprings, apply_operators
import time
import sys
import pickle as cPickle
import tensorflow as tf
from SavingHandler import *

import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.enable_eager_execution()
tfe = tf.contrib.eager

nruns = 1
popsize = 100
tsize = 5
ngens = 100
resume = False
tournament_type = "tournament"
tournament_size = 5
forest_type = 'ramped_forest'

csvname = "heart_processed.csv"
savename = "hrtTest"
loadname = "lastgenSara.p"
sheetname = "hrtTest"
dsetpath = "F:\GEEGP\datasets"

dset = os.path.join(dsetpath, csvname)
savepopdir = '.\\individuals'
savesheetdir = '.\\sheets'
# load = os.path.join(fpath,loadname)
sys.setrecursionlimit(100000)


training_x, training_y, test_x, test_y = load_data(dset)

def main():

    # rmselist = []
    acclist = []
    appendacl = acclist.append
    tacclist = []
    appendtacl = tacclist.append
    nodelist = []
    appendnl = nodelist.append

    run = 0
    start_time = time.time()
    while run < nruns:
        print("number of run: ",run, '\n')
        cgen = 0
        if not resume:
            treelist = ramped_forest(popsize, [])
        else:
            # treelist = cPickle.load(open(load, "rb"))
            pass
        while cgen < ngens:
            print("gen number : ",cgen)

            chosen = double_tournament(tournament(treelist, popsize, tournament_size), popsize)
            offspring = apply_operators(chosen, popsize, [])
            newgen = elitism(treelist, offspring, popsize)
            treelist = newgen

            acc = treelist[0][0].accuracy(treelist[0][2])
            tresults = treelist[0][0].calculate(0, True)
            tacc = treelist[0][0].test_accuracy(tresults)

            print("RMSE: ", treelist[0][1])
            print("size: ", treelist[0][3])
            print("Training Accuracy: ", acc)
            print("Test Accuracy: ", tacc, '\n')

            appendacl(acc)
            appendtacl(tacc)
            appendnl(treelist[0][3])

            save_best(savepopdir, savename + str(run) + str(cgen), [treelist[0]])

            cgen += 1

        save_spreadsheet(savesheetdir, sheetname + str(run), [acclist, tacclist, nodelist])
        acclist.clear()
        tacclist.clear()
        nodelist.clear()

        run += 1
    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    main()