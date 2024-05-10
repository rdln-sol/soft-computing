import matplotlib.pyplot as plt
import obj_fit_functions
import obj_fit_functions
from GA_Initialize import bin_Initialization, bin_Create_First_Generation
from GA_Evaluate import Evaluate_Generation, bin_decode
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

objective = input(
    """\nWhich of the following functions do you wish to optimize?
                   1) fGriewank
                   2) griewank
                   3) michalewicz
                   4) rastrigin
                   5) booth
                   6) bukin_n6
                   7) cross_in_tray
                   8) holder_table
                   9) mccormick
                   10) poloni
                   11) viennet
                   Answer : """
)
match objective:
    case "1":
        Fitness_Function = obj_fit_functions.fGriewank
    case "2":
        Fitness_Function = obj_fit_functions.griewank
    case "3":
        Fitness_Function = obj_fit_functions.michalewicz
    case "4":
        Fitness_Function = obj_fit_functions.rastrigin
    case "5":
        Fitness_Function = obj_fit_functions.booth
    case "6":
        Fitness_Function = obj_fit_functions.bukin_n6
    case "7":
        Fitness_Function = obj_fit_functions.cross_in_tray
    case "8":
        Fitness_Function = obj_fit_functions.holder_table
    case "9":
        Fitness_Function = obj_fit_functions.mccormick
    case "10":
        Fitness_Function = obj_fit_functions.poloni
    case "11":
        Fitness_Function = obj_fit_functions.viennet

answer = int(
    input(
        """\nHow would you like the Roulette Wheel to function? 
        1) Normal 
        2) Linear Scaled 
        3) Linear Classified
        Answer : """
    )
)
if answer == 3:
    q = float(
        input("\nWhat will the possibality of choosing the best solution be ?  q = ")
    )
    q0 = (2 / algorithm_parameters.get("num_Genes")) - q
    print("q = ", q, " q0 = ", q0)

for i in range(algorithm_parameters.get("num_Generations")):

    decoded_population = bin_decode(population, algorithm_parameters)
    fitness_list = Evaluate_Generation(decoded_population, Fitness_Function)

    if answer == 1:
        parents = Roulette_Wheel_Selection(fitness_list)
    elif answer == 2:
        scaled_fitness_list = Linear_scaling(fitness_list)
        parents = Roulette_Wheel_Selection(scaled_fitness_list)
    elif answer == 3:
        parents = Classified_Roulette_Wheel_Selection(fitness_list, q, q0)

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
