from random import choices
import string

class Empire:
    def __init__(self, imperialist, zetta) -> None:
        self.imperialist = imperialist
        self.colonies = list()
        self.cost = float('inf')
        self.name = ''.join(choices(string.ascii_uppercase, k=2))

    def calculateCost(self, zetta):
        if self.colonies:
            colonyCost = 0
            for colony in self.colonies:
                colonyCost += colony.getCost()

            totalCost = self.imperialist.getCost() + (zetta * (colonyCost/len(self.colonies)))

        else:
            totalCost = self.imperialist.getCost()
        return totalCost

    def addColony(self, colony, zetta):
        self.colonies.append(colony)
        self.cost = self.calculateCost(zetta=zetta)
    
    def rmColony(self, index, zetta):
        del self.colonies[index]
        self.cost = self.calculateCost(zetta=zetta)

    def getCost(self):
        return self.cost
    
    def getColonies(self):
        return self.colonies
    
    def getImperialist(self):
        return self.imperialist