import numpy as np
from random import random

def rouletteWheel(lst):
    randomNum = random()
    cumulativeSum = np.cumsum(lst)
    indexList = [i for i, x in enumerate(cumulativeSum) if randomNum <= x]
    return indexList[0]