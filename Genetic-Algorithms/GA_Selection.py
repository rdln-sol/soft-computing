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


def Classified_Roulette_Wheel_Selection(fitness_list: list, q, q0):
    Pi = []
    for i in range(len(fitness_list)):
        if i == fitness_list.index(max(fitness_list)):
            Pi.append(q)
        elif i == fitness_list.index(min(fitness_list)):
            Pi.append(q0)
        else:
            Ri = round(random.uniform(0, 1), 5)
            Pi.append((q - (q - q0)) * ((Ri - 1) / len(fitness_list) - 1))

    Ci = []
    for i in range(len(fitness_list)):
        if i != 0:
            Ci.append(Pi[i] + Ci[i - 1])
        else:
            Ci.append(Pi[i])

    parents = []
    for i in range(len(fitness_list)):
        parents.append(lower_bound(Ci, round(random.uniform(0, 1), 5)))

    return parents


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
