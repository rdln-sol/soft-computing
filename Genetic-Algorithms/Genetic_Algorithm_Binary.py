import matplotlib.pyplot as plt
import obj_fit_functions
import obj_fit_functions
from GA_Initialize import bin_Initialization, bin_Create_First_Generation
from GA_Evaluate import bin_Evaluate_Generation
from GA_Selection import (
    Roulette_Wheel_Selection,
    Classified_Roulette_Wheel_Selection,
    Linear_scaling,
)
from numpy import mean
from GA_Crossover import One_Point_Crossover
from GA_Mutation import bin_Mutation


algorithm_parameters = bin_Initialization()
population = bin_Create_First_Generation(algorithm_parameters)

best_solution = []
best_so_far = []
average_solution = []


def Fitness_Function(x):
    return obj_fit_functions.rastrigin(x)


for i in range(algorithm_parameters.get("num_Generations")):

    fitness_list = bin_Evaluate_Generation(
        population, algorithm_parameters, Fitness_Function
    )
    parents = Roulette_Wheel_Selection(fitness_list)

    population = One_Point_Crossover(
        population, parents, algorithm_parameters.get("Pc")
    )
    population = bin_Mutation(
        population, algorithm_parameters, algorithm_parameters.get("Pm")
    )
    best_solution_index = fitness_list.index(max(fitness_list))
    best_solution.append(fitness_list[best_solution_index])
    best_so_far.append(max(best_solution))
    average_fitness = mean(fitness_list)
    average_solution.append(average_fitness)

print("\nThe final population is: \n", *population, sep="\n")
plt.plot(best_solution, label="Best Solution")
plt.plot(average_solution, label="Average Solution")
plt.plot(best_so_far, label="Best So Far")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Best and Average Fitness over Generations")
plt.legend()
plt.grid(True)
plt.show()
