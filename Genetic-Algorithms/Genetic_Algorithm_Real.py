import random


def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


def Fitness_Function(chromosme: list):
    return 1


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


def Evaluate_Generation(population: list, fitness_function):

    fitness_list = []
    for i in range(len(population)):
        fitness_list.append(fitness_function(population[i]))
    return fitness_list


def Roulette_Wheel_Selection(fitness_list: list):

    total_fitness = sum(fitness_list)
    Pi = 0
    Ci = []
    for i in range(len(fitness_list)):
        Pi = fitness_list[i] / total_fitness
        if i != 0:
            Ci.append(Pi + Ci[i - 1])
        else:
            Ci.append(Pi)
    parents = []
    for i in range(len(fitness_list)):
        parents.append(lower_bound(Ci, round(random.uniform(0, 1), 5)))

    return parents


def One_Point_Crossover(population: list, parents: list, Pc):

    for i in range(0, len(parents), 2):
        population[i], population[i + 1] = (
            population[parents[i]],
            population[parents[i + 1]],
        )

    for i in range(0, len(population), 2):
        breaking_point = round(random.uniform(0, 1), 6)
        if breaking_point < Pc:
            breaking_point = random.randint(0, len(population))
            temp1 = population[i][:breaking_point] + population[i + 1][breaking_point:]
            temp2 = population[i + 1][:breaking_point] + population[i][breaking_point:]
            population[i], population[i + 1] = temp1, temp2
        else:
            continue

    return population


def Mutation(population: list, algorithm_parameters: dict, Pm):

    for chromosome in population:
        rand = round(random.uniform(0, 1), 6)
        if rand < Pm:
            mutation_point = random.randint(0, len(chromosome) - 1)
            chromosome[mutation_point] = round(
                random.uniform(
                    algorithm_parameters.get("min_range"),
                    algorithm_parameters.get("max_range"),
                ),
                4,
            )
        else:
            continue

    return population


algorithm_parameters = Initialization()
population = Create_First_Generation(algorithm_parameters)
best_solution = []
average_solution = []
for i in range(algorithm_parameters.get("num_Generations")):
    fitness_list = Evaluate_Generation(population, Fitness_Function)
    parents = Roulette_Wheel_Selection(fitness_list)
    population = One_Point_Crossover(
        population, parents, algorithm_parameters.get("Pc")
    )
    population = Mutation(
        population, algorithm_parameters, algorithm_parameters.get("Pm")
    )
    best_solution.append(population.index(max(fitness_list)))
    average_solution.append(sum(fitness_list) / len(fitness_list))

print("\nThe final population is: \n", *population, sep="\n")
