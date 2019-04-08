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



nruns = 10
popsize = 500
tsize = 5
ngens = 100
resume = False
tournament_type = "tournament"
tournament_size = 5
forest_type = 'ramped_forest'

csvname = "curvasRWC.csv"
savename = "d2_t_syn_mae"
loadname = "lastgenSara.p"
sheetname = "d2_t_syn_mae"
dsetpath = ".\\datasets"

dset = os.path.join(dsetpath, csvname)
savepopdir = '.\\individuals'
savesheetdir = '.\\sheets'
# load = os.path.join(fpath,loadname)
sys.setrecursionlimit(100000)




def main():

    lixo = []
    appendlixo = lixo.append

    data = ten_fold(dset)



    run = 0
    start_time = time.time()
    while run < nruns:
        print("Parsing Data...")
        training_x, training_y, test_x, test_y = load_data(dset)
        #np.random.shuffle(data)
        #boxes = data
        #test = np.array(boxes.pop())
        #test_y = tf.convert_to_tensor(test[:, -1])
        #test_x = list(map(tf.convert_to_tensor, np.delete(test, -1, axis=1).T))
        #boxes = np.concatenate(boxes)
        #training_y = tf.convert_to_tensor(boxes[:, -1])
        #training_x = list(map(tf.convert_to_tensor, np.delete(boxes, -1, axis=1).T))

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

            #chosen = double_tournament(tournament(treelist, popsize, tournament_size), popsize)
            chosen = tournament(treelist, popsize, tournament_size)

            offspring = apply_operators(chosen, popsize, [])

            del chosen

            newgen = elitism(treelist, offspring, popsize)

            del offspring

            treelist = newgen

            del newgen

            calctest = treelist[0].root.calculate(0, True)


            print("MAE: ", treelist[0].fit)
            print("size: ", treelist[0].size, '\n')

            appendlixo(0)

            tf.random.set_seed(1)
            gc.collect()
            cgen += 1

        RMSE = treelist[0].fit
        rmse = [RMSE for i in range(len(calctest.numpy()))]
        save_best(savepopdir, savename + str(run), [treelist[0]])
        save_spreadsheet(savesheetdir, sheetname + str(run), [rmse, calctest.numpy(), test_y.numpy()])
        del rmse


        tf.random.set_seed(1)
        gc.collect()
        run += 1
        #treelist[0][0].print_tree()
    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    main()