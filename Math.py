#genetic operators
import tensorflow as tf
import numpy as np


def divide(x,y):
    #temp = tf.divide(x,y).numpy()
    #original = x.numpy()
    #temp[temp == np.inf] = original[temp == np.inf]    #magic, for any place in temp that is equal to np.inf, replace it with the equivalent index from original
    #result = tf.Variable(temp)
    result = tf.where(tf.math.equal(y,0.), x, tf.math.divide(x,y)) # result = where(abs(denominator) < epsilon, numerator, numerator / denominator)
    return result


def ln(x):
    result = tf.where(tf.math.less_equal(x, 0.), x, tf.math.log(x)) # result = where(abs(value) <= 0., value, log(value))
    return result


def sqrt(x):
    result = tf.where(tf.math.less(x, 0.), x, tf.math.sqrt(x)) # result = where(abs(value) <= 0., value, log(value))
    return result


def synapse(x):
    return tf.math.log(x + tf.math.sqrt(1 + x**2))

def binary_round(x):
    result = tf.where(x >= 0.5, x/x, abs(x*0)) # result = where(value >= 0.5, 1, 0)
    return result

