import random, math, numpy as np, matplotlib.pyplot as plt
from Firefly import Firefly

class FA:
    '''
        Firefly Algorithm
        =================

        Includes main functions of the 
        "firefly algorithm" using the Firefly module.
    '''
    def __init__(self) -> None:
        self.fireflies = list()
    
    def generateFireflies(self, count: int, dCount: int, lb: float, ub: float) -> None:
        '''
            Initiates some (count) fireflies and assigns 
            random dimensions (dCount) to each firefly object.
        '''
        for _ in range(count):
            firefly = Firefly()
            firefly.initDimensions(dCount, lb, ub)
            self.fireflies.append(firefly)
        self.colors = [plt.cm.jet(float(i) / count) for i in range(count)]

    def move(self, betta0: float, alpha0: float, alphaRC: float, gamma: float) -> None:
        '''
            Moves the fireflies with lower light intensity 
            towards the fireflies with higher light intensity.
        '''
        for i in range(len(self.fireflies)):
            for j in range(len(self.fireflies)):
                if self.fireflies[i].getBrightness() > self.fireflies[j].getBrightness():

                    rij = np.linalg.norm(np.array(self.fireflies[i].getDimensions()) - np.array(self.fireflies[j].getDimensions()))
                    beta = betta0 * math.exp(-gamma * (rij ** 2))
                    
                    new_dimensions = []
                    for k in range(len(self.fireflies[i].getDimensions())):
                        dim_i = self.fireflies[i].getDimensions()[k]
                        dim_j = self.fireflies[j].getDimensions()[k]
                        
                        new_dim = dim_i + beta * (dim_j - dim_i) + alpha0 * (random.random() - 0.5) * alphaRC
                        new_dimensions.append(new_dim)
                    
                    self.fireflies[i].setDimensions(new_dimensions)

    def plotFireflies(self, iteration: int) -> None:
        '''
            Plots the fireflies in 2D space.
        '''
        x = [firefly.getDimensions()[0] for firefly in self.fireflies]
        y = [firefly.getDimensions()[1] for firefly in self.fireflies]
        for i in range(len(self.fireflies)):
            plt.scatter(x[i], y[i], marker='o', color=self.colors[i])
        plt.title(f'Firefly positions at iteration {iteration}')
        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        plt.xlabel('Dimension 1')
        plt.ylabel('Dimension 2')
        plt.draw()
        plt.pause(0.0001)
        plt.clf()