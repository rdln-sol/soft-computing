import random


def Initialization():

    algorithm_parameters = {}
    num_Chromosomes = int(input("Enter the number of Chromosomes: "))
    algorithm_parameters["num_Chromosomes"] = num_Chromosomes
    num_Genes = int(input("Enter the number of Genes: "))
    algorithm_parameters["num_Genes"] = num_Genes
    num_Generations = int(input("Enter the number of Generations: "))
    algorithm_parameters["num_Generations"] = num_Generations
    Pc = round(random.uniform(0.6, 0.9), 3)
    print("The Possibality of Crossover is: ", Pc)
    algorithm_parameters["Pc"] = Pc
    Pm = round(random.uniform(0.01, 0.1), 3)
    print("The Possibality of Mutation is: ", Pm)
    algorithm_parameters["Pm"] = Pm
    min_range = float(input("Enter the Minimum Range: "))
    algorithm_parameters["min_range"] = min_range
    max_range = float(input("Enter the Maximum Range: "))
    algorithm_parameters["max_range"] = max_range

    print("\nThe parameters have been set as: \n", algorithm_parameters)
    return algorithm_parameters


def Create_First_Generation(algorithm_parameters):

    population = []

    for i in range(algorithm_parameters.get("num_Chromosomes")):
        line = []
        for j in range(algorithm_parameters.get("num_Genes")):
            line.append(
                round(
                    random.uniform(
                        algorithm_parameters.get("min_range"),
                        algorithm_parameters.get("max_range"),
                    ),
                    4,
                )
            )
        population.append(line)

    print("\nThe first Generation is : \n", *population, sep="\n")
    return population
