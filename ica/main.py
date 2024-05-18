from ICA import ICA
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':

    ica = ICA()

    countryCount = int(input('enter the number of countries: '))
    optArrayLength = int(input('enter the number of dimensions for every country: '))
    lowerBound = float(input('please enter the lower bound number for each dimension (float): '))
    upperBound = float(input('please enter the upper bound number for each dimension (float): '))
    ica.createCountries(count = countryCount, dCount=optArrayLength, lb=lowerBound, ub=upperBound)

    imperialistCount = int(input('enter the number of imperialists: '))
    zetta = float(input('please enter the empire cost rate constant(ZETTA): '))
    ica.createEmpires(empireCount = imperialistCount, zetta=zetta)

    betta = float(input('please enter a number as BETTA (float): '))
    
    pr = float(input('please enter the probabilty of a revolution happening (float): '))
    
    ii = 0

    currentCost = list()

    while len(ica.empires) != 1:
        print(f'\n**************** iterations {ii} ****************\n')
        print(f'\nremaining empires are : {[j.name for j in ica.empires]}')
        ica.absorb(betta = betta)
        ica.revolution(pr = pr, lowerBound = lowerBound, upperBound = upperBound)
        ica.switch()
        ica.competition(zetta)
        currentCost.append(ica.empires[0].cost)
        ii += 1

    print(f'Empire {ica.empires[0].name} with cost : {ica.empires[0].cost} is the winner in {ii} iterations')
    print(f'the dimensions are : {ica.empires[0].getImperialist().dimensions}')