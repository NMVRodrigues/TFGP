import tensorflow as tf
from tensorflow.python.keras.datasets import mnist

def read_split_csv(fname, cols, training_size):
    defaults = [tf.float64] * cols
    dataset = tf.data.experimental.CsvDataset(fname, defaults)
    #TODO -> ver isto das lists
    #dataset.shuffle(len(list(dataset))) #usar int grande
    dataset.shuffle(1000000) #1 million for safe measure
    training, testing = list(dataset)[:int((len(list(dataset))*training_size))], list(dataset)[int((len(list(dataset))*training_size)):]
