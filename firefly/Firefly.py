import random, string

class Firefly:
    def __init__(self) -> None:
        self.name = ''.join(random.choices(string.ascii_lowercase, k=3))
        self.dimensions = list()
        self.brightness = float('inf')

    def calculateBrightness(self, dimensions: list) -> float:
        return sum(dimension ** 2 for dimension in dimensions)
    
    def initDimensions(self, count: int, lb: float, ub: float) -> None:
        self.dimensions = [lb + random.random() * (ub - lb) for _ in range(count)]
        self.brightness = self.calculateBrightness(self.dimensions)

    def getBrightness(self) -> float:
        return self.brightness
    
    def getDimensions(self) -> list:
        return self.dimensions
    
    def setDimensions(self, dimensions: list) -> None:
        self.dimensions = dimensions
        self.brightness = self.calculateBrightness(dimensions)