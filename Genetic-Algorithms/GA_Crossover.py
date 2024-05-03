import random


def One_Point_Crossover(population: list, parents: list, Pc):

    for i in range(0, len(parents) - 1, 2):
        population[i], population[i + 1] = (
            population[parents[i]],
            population[parents[i + 1]],
        )

    for i in range(0, len(population) - 1, 2):
        breaking_point = round(random.uniform(0, 1), 6)
        if breaking_point < Pc:
            breaking_point = random.randint(0, len(population))
            temp1 = population[i][:breaking_point] + population[i + 1][breaking_point:]
            temp2 = population[i + 1][:breaking_point] + population[i][breaking_point:]
            population[i], population[i + 1] = temp1, temp2
        else:
            continue

    return population
