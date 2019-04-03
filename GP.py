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
dsetpath = ".\\datasets"

dset = os.path.join(dsetpath, csvname)
savepopdir = '.\\individuals'
savesheetdir = '.\\sheets'
# load = os.path.join(fpath,loadname)
sys.setrecursionlimit(100000)


#training_x, training_y, test_x, test_y = load_data(dset)

def main():

    run = 0
    start_time = time.time()
    while run < nruns:
        print("Parsing Data...")
        training_x, training_y, test_x, test_y = load_data(dset)
        print(test_y, '\n')
        print(test_y.numpy())
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

            del chosen

            newgen = elitism(treelist, offspring, popsize)

            del offspring

            treelist = newgen

            del newgen

            calctest = treelist[0].root.calculate(0, True)


            print("RMSE: ", treelist[0].fit)
            print("size: ", treelist[0].size, '\n')


            save_best(savepopdir, savename + str(run) + str(cgen), [treelist[0]])
            tf.random.set_seed(1)
            gc.collect()
            cgen += 1

        save_spreadsheet(savesheetdir, sheetname + str(run), [treelist.fit, calctest.numpy(), test_y.numpy()])


        tf.random.set_seed(1)
        gc.collect()
        run += 1
        #treelist[0][0].print_tree()
    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    main()