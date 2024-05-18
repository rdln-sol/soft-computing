from country import Country
from empire import Empire
from tools import rouletteWheel
from random import random, shuffle
import numpy as np

class ICA:
    def __init__(self) -> None:
        self.countries = list()
        self.empires = list()
        self.colonies = list()

    def createCountries(self, count, dCount, lb, ub):
        for i in range(count):
            country = Country()
            country.initDimensions(dCount=dCount, lb=lb, ub=ub)
            self.countries.append(country)


    def createEmpires(self, empireCount, zetta):
        countries = self.countries

        costs = dict()
        for country in countries:
            cost = country.getCost()
            costs[country] = cost

        sortedDict = dict(sorted(costs.items(), key=lambda item: item[1]))
        sortedcountries = list(sortedDict)

        self.countries = sortedcountries

        imperialists = sortedcountries[:empireCount]
        self.colonies = sortedcountries[empireCount:]

        for imperialist in imperialists:
            self.empires.append(Empire(imperialist, zetta))

        empireColonies = len(self.colonies) // len(self.empires)

        tempList = self.colonies
        shuffle(tempList)

        for empire in self.empires:
            for i in range(empireColonies):
                empire.addColony(tempList.pop(), zetta)
                shuffle(tempList)
            empire.calculateCost(zetta)

        return self.empires
    
    def absorb(self, betta):
        for empire in self.empires:
            imperialist = empire.getImperialist()
            for colony in empire.getColonies():
                colonyDimensions = colony.getDimensions()
                empireDimensions = imperialist.getDimensions()
                
                for i in range(len(colonyDimensions)):
                    colonyDimensions[i] += (random() * (empireDimensions[i] - colonyDimensions[i]) * betta)
                colony.setDimensions(colonyDimensions)

    def revolution(self, pr, lowerBound, upperBound):
        for empire in self.empires:
            for colony in empire.getColonies():
                if random() <= pr:
                    dimensions = colony.getDimensions()
                    for i in range(len(dimensions)):
                        dimensions[i] = lowerBound + (random() * (upperBound - lowerBound))
                    colony.setDimensions(dimensions)
                    print(f'revolution for {colony.name} happened')
    
    def switch(self):
        for empire in self.empires:
            imperialist = empire.getImperialist()
            for colony in empire.getColonies():
                if colony.getCost() < imperialist.getCost():
                    print(f'imperialist {imperialist.name} with cost : "{imperialist.getCost()}" switched with colony {colony.name} with cost : "{colony.getCost()}"')
                    temp = imperialist
                    imperialist = colony
                    colony = temp

    

    def competition(self, zetta):
        if len(self.empires) == 1:
            return self.empires[0]
        
        
        costs = dict()
        for empire in self.empires:
            costs[empire] = empire.getCost()
        sortedDict = dict(sorted(costs.items(), key=lambda item: item[1]))
        sortedEmpires = list(sortedDict)
        weakestEmpire = sortedEmpires[-1]
        print(weakestEmpire.name)
        tc = np.array([empire.getCost() for empire in self.empires if not empire is weakestEmpire])
        ntc = np.divide(tc, tc.sum())

        if len(weakestEmpire.getColonies()) > 0:
            colonyCosts = dict()
            for colony in weakestEmpire.getColonies():
                colonyCosts[colony] = colony.getCost()
            sortedColonyDict = dict(sorted(colonyCosts.items(), key=lambda item: item[1]))
            sortedColonies = list(sortedColonyDict)
            weakestColony = sortedColonies[-1]
            chosenEmpire = self.empires[rouletteWheel(ntc)]
            temp = weakestEmpire.getColonies()
            ind = temp.index(weakestColony)
            chosenEmpire.addColony(weakestColony, zetta)
            weakestEmpire.rmColony(ind, zetta)
            print(f"{chosenEmpire.name} <= {weakestEmpire.name}'s colony : {weakestColony.name}")
        
        if len(weakestEmpire.getColonies()) == 0:
            chosenEmpire = self.empires[rouletteWheel(ntc)]
            chosenEmpire.addColony(weakestEmpire.getImperialist(), zetta)
            print(f'empire {weakestEmpire.name} was deleted')
            del self.empires[self.empires.index(weakestEmpire)]