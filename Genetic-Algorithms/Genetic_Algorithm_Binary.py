import obj_fit_functions
from GA_Initialize import bin_Initialization, bin_Create_First_Generation
from GA_Evaluate import bin_decode


algorithm_parameters = bin_Initialization()
population = bin_Create_First_Generation(algorithm_parameters)
for i in range(algorithm_parameters.get("num_Generations")):
    bin_decode(population[i],algorithm_parameters)

