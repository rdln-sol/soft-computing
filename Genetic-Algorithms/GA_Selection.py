import random
from numpy import mean


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


def Linear_scaling(fitness_list: list):
    scaled_fitness_list = []
    total_fitness = sum(fitness_list)
    num_chromosomes = len(fitness_list)
    best_fitness = max(fitness_list)
    average_fitness = mean(fitness_list)
    Cm = ((best_fitness / total_fitness) * num_chromosomes) / (
        (average_fitness / total_fitness) * num_chromosomes
    )
    for fitness in fitness_list:
        a = ((Cm - 1) * average_fitness) / (best_fitness - average_fitness)
        b = (1 - a) * average_fitness
        scaled_fitness_list.append((a * fitness) + b)
    return scaled_fitness_list


def Classified_Roulette_Wheel_Selection(fitness_list: list):
    q = float(input("q :"))
    q0 = float(input("q0 :"))
    Pi = []
    for i in range(len(fitness_list)):
        if i == fitness_list.index(max(fitness_list)):
            Pi.append(q)
        elif i == fitness_list.index(min(fitness_list)):
            Pi.append(q0)
        else:
            Ri = round(random.uniform(0, 1), 5)
            Pi.append((q - (q - q0)) * ((Ri - 1) / len(fitness_list) - 1))

    Ci = [0] * len(fitness_list)
    for i in range(len(fitness_list)):
        if i == 0:
            Ci[i] = Pi[i]
        else:
            Ci[i] = Pi[i] + Ci[i - 1]

    parents = []
    for _ in range(len(fitness_list)):
        rand_val = random.uniform(0, 1)
        parent_index = lower_bound(Ci, rand_val)
        parents.append(parent_index)

    return parents


def Roulette_Wheel_Selection(fitness_list: list):

    total_fitness = sum(fitness_list)
    Pi = [f / total_fitness for f in fitness_list]

    Ci = [0] * len(fitness_list)
    for i in range(len(fitness_list)):
        if i == 0:
            Ci[i] = Pi[i]
        else:
            Ci[i] = Pi[i] + Ci[i - 1]

    parents = []
    for _ in range(len(fitness_list)):
        rand_val = random.uniform(0, 1)
        parent_index = lower_bound(Ci, rand_val)
        parents.append(parent_index)

    return parents


def Binary_Tournament_Selection(fitness_list):
    parents = []
    population_size = len(fitness_list)

    for _ in range(population_size):

        i1, i2 = random.sample(range(population_size), 2)

        if fitness_list[i1] > fitness_list[i2]:
            parents.append(i1)
        else:
            parents.append(i2)

    return parents
