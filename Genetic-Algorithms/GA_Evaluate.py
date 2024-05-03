def Evaluate_Generation(population: list, fitness_function):

    fitness_list = []
    for i in range(len(population)):
        fitness_list.append(fitness_function(population[i]))
    return fitness_list
