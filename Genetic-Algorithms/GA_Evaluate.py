def Evaluate_Generation(population: list, fitness_function):

    fitness_list = []
    for i in range(len(population)):
        fitness_list.append(fitness_function(population[i]))
    return fitness_list


def bin_decode(chromosome: list, algorithm_parameters: dict):
    decoded_chromosome = []
    for i in range(0, len(chromosome), algorithm_parameters.get("num_Genes")):
        temp = "".join(
            str(bit)
            for bit in chromosome[i : i + algorithm_parameters.get("num_Genes")]
        )
        base_number = int(temp, 2)
        Xn = base_number / ((2 ** algorithm_parameters.get("num_Genes")) - 1)
        real_number = algorithm_parameters.get("min_range") + (
            Xn
            * (
                algorithm_parameters.get("max_range")
                - algorithm_parameters.get("min_range")
            )
        )
        decoded_chromosome.append(real_number)
    return decoded_chromosome


def bin_Evaluate_Generation(
    population: list, algorithm_parameters: dict, fitness_function
):

    fitness_list = []
    for i in range(len(population)):
        fitness_list.append(
            fitness_function(bin_decode(population[i], algorithm_parameters))
        )
    return fitness_list
