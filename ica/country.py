from random import random, choices
import string
import numpy as np

class Country:
    def __init__(self) -> None:
        self.dimensions = list()
        self.cost = float('inf')
        self.name = ''.join(choices(string.ascii_lowercase, k=3))

    def calculateCost(self, dimensions):
        result = 0
        for x in dimensions:
            result += (x**2)
        return result

    def initDimensions(self, dCount, lb, ub):
        for i in range(dCount):
            Xi = lb + (random() * (ub - lb))
            self.dimensions.append(Xi)
        self.cost = self.calculateCost(self.dimensions)

    def getCost(self):
        return self.cost
    
    def getDimensions(self):
        return self.dimensions
    
    def setDimensions(self, dimensions):
        self.dimensions = dimensions
        self.cost = self.calculateCost(dimensions)