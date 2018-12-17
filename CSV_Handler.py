import tensorflow as tf
from sklearn.model_selection import train_test_split


def read_split_csv(fname, cols, rows, training_size):
    defaults = [tf.float64] * cols
    dataset = tf.data.experimental.CsvDataset(fname, defaults)
    #TODO -> ver isto das lists
    #dataset.shuffle(len(list(dataset))) #usar int grande
    dataset.shuffle(1000000) #1 million for safe measure
    iterator = dataset.make_one_shot_iterator()
    temp = []
    append = temp.append
    temp = list(map(tf.convert_to_tensor, temp))
    try:
        while True:
            append(iterator.get_next())
    except tf.errors.OutOfRangeError:
        pass
    training_cols , test_cols = train_test_split(temp, test_size=0.3, shuffle=False)
    training_cols, test_cols = np.array(training_cols).T, np.array(test_cols.T)
    training_cols, test_cols = list(map(tf.convert_to_tensor, training_cols)), list(map(tf.convert_to_tensor, test_cols))
    training_labels = training_cols[-1]
    test_labels = test_cols[-1]
    #tf.stack([temp[0][0], temp[0][1]], 0)
    #col_list = []
    #append = col_list.append
    #to_tensor = tf.convert_to_tensor
    #for i in range(0,cols):
    #    col = dataset.map(lambda *row: row[i])
    #    col = to_tensor(*col.batch(rows))
    #    append(col)
    #training, testing = list(dataset)[:int((len(list(dataset))*training_size))], list(dataset)[int((len(list(dataset))*training_size)):]
    #label_list = col_list[-1]
    return training_cols, training_labels, test_cols, test_labels

