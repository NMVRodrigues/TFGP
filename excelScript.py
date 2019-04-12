
import os
import pandas as pd
import numpy as np

path = '.' + os.sep + 'sheets'+ os.sep

files = []
extend = files.extend
for (dirpath, dirnames, filenames) in os.walk(path):
    extend(filenames)
    break

df_arr = []
appendDF = df_arr.append
for f in files:
    df = pd.read_csv(os.path.join(path + f), sep=';', engine='python')
    appendDF(df)

mutation = []
crossover = []
rmse = []
nodes = []
training = []
test = []
dimensions = []

for dtf in df_arr:
    rmse.append(dtf['RMSE'])
    training.append(dtf['training'])
    test.append(dtf['test'])
    nodes.append(dtf['nodes'])
    #mutation.append(dtf['MutationP'])
    #crossover.append(dtf['crossoverP'])
    #dimensions.append(dtf['dimensions'])


rmse = pd.concat(rmse, axis=1)
training = pd.concat(training, axis=1)
test = pd.concat(test, axis=1)
nodes = pd.concat(nodes, axis=1)
#mutation = pd.concat(mutation, axis=1)
#crossover = pd.concat(crossover, axis=1)
#dimensions = pd.concat(dimensions, axis=1)

rmse = rmse.T
nodes = nodes.T
test = test.T
training = training.T
#mutation = mutation.T
#crossover = crossover.T
#dimensions = dimensions.T
line_saparator = pd.Series([np.nan])

pd.concat([line_saparator, rmse, line_saparator, training, line_saparator, test, line_saparator, nodes]).to_csv(os.path.join(path, "bcw" + '.csv'), sep=";",  index=True)
#pd.concat([mutation, crossover, training, test, nodes]).to_csv(os.path.join(path, "hrt9-1" + '.csv'), sep=";",  index=True)
#pd.concat([training, test, dimensions, nodes]).to_csv(os.path.join(path, "radioSelectK" + '.csv'), sep=";",  index=True)