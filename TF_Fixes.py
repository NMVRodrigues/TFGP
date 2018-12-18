#genetic operators
import tensorflow as tf
import numpy as np


def divide(x,y):
    #temp = tf.divide(x,y).numpy()
    #original = x.numpy()
    #temp[temp == np.inf] = original[temp == np.inf]    #magic, for any place in temp that is equal to np.inf, replace it with the equivalent index from original
    #result = tf.Variable(temp)
    result = tf.where(abs(y) <= 0., x, x/y) # result = where(abs(denominator) < epsilon, numerator, numerator / denominator)
    return result

def ln(x):
    result = tf.where(abs(x) <= 0., x, tf.log(x)) # result = where(abs(value) <= 0., value, log(value))
    return result

def sqrt(x):
    result = tf.where(abs(x) < 0., x, tf.sqrt(x)) # result = where(abs(value) <= 0., value, log(value))
    return result

