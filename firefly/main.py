from FA import FA
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fa = FA()
    count = int(input('enter the number of fireflies : '))
    dCount = int(input('enter the number of dimensions : '))
    lb = int(input('enter the lower bound for every dimension : '))
    ub = int(input('enter the upper bound for every dimension : '))
    fa.generateFireflies(count, dCount, lb, ub)
    iterations = int(input('enter the number of iterations : '))
    
    plt.ion()

    for iteration in range(iterations):
        fa.move(2.0, 0.2, 0.9, 0.5)

        fa.plotFireflies(iteration)
    
    plt.ioff()