def Evaluate_Generation(population: list, fitness_function):

    fitness_list = []
    for i in range(len(population)):
        fitness_list.append(fitness_function(population[i]))
    return fitness_list

def bin_decode(chromosome: list,algorithm_parameters : dict):
    decoded_chromosome = []
    i = 0
    for i in range(0, algorithm_parameters.get("num_Bits"), algorithm_parameters.get("num_Genes")):
        temp = ''.join(str(chromosome[i:i+algorithm_parameters.get("num_Genes")]))
        base_number = int(temp,2)
        Xn = base_number / (2**algorithm_parameters.get("num_Bits") - 1)
        real_number = algorithm_parameters.get("min_range") + (Xn * (algorithm_parameters.get("max_range") - algorithm_parameters.get("min_range")))
        decoded_chromosome.append(real_number)
    print(*decoded_chromosome,sep=" ")
