import math


def fun1(x):
    result = 0
    for i in range(len(x)):
        result += math.pow(x[i], 2)
    return result
