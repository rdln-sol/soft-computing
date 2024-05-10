import random


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


def bin_Mutation(chromosomes, algorithm_parameters, mutation_probability):
    num_genes = algorithm_parameters.get("num_Genes")
    for chromosome in chromosomes:
        for i in range(len(chromosome)):
            if random.random() < mutation_probability:
                chromosome_list = list(chromosome)
                chromosome_list[i] = "1" if chromosome_list[i] == "0" else "0"
                chromosome = "".join(chromosome_list)
    return chromosomes
