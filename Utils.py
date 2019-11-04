#genetic operators
import tensorflow as tf
import numpy as np


def divide(x,y):
    result = tf.where(tf.math.equal(y,0.), x, tf.math.divide(x,y))
    return result


def ln(x):
    result = tf.where(tf.math.less_equal(x, 0.), x, tf.math.log(x))
    return result


def sqrt(x):
    result = tf.where(tf.math.less(x, 0.), x, tf.math.sqrt(x))
    return result


def binary_round(x):
    result = tf.where(x >= 0.5, x/x, abs(x*0))
    return result

