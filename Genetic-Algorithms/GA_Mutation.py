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
