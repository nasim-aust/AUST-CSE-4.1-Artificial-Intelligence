"""
import header.py and all its functions
"""

import helper
from helper import *

"""
Scheduling functions
"""

def do_linear_schedule(t):
    
    """
    generates a temparature based on input time(linear)
    keywords:
    t - input time
    returns 100-0.5*t
    """
    T = 100-0.5*t
    return T
    
def do_exponential_schedule(t):
    """
    generates a temparature based on input time(exponential)
    keywords:
    t - input time
    returns 100*math.exp(-0.5*t)
    """

    
    T = 100*math.exp(-0.5*t)
    return T

def do_simulated_annealing(tweak_function=swap_function, schedule_function = do_linear_schedule):
    """
    Runs hill climmbing algorithm
    Keyword argument:
    tweak_function- the tweaking function you want to use- it can be swap_function(default) or shuffle_function
    schedule_function- the scheduling function you want to use- it can be do_linear_schedule(default) or do_exponential_schedule
    returns solution state and its fitnes
    """
    #Initialization step

    current = generate_random_permutation()
    
    
    iteration = 200

    for t in range(0,iteration):
    
        current_fitness = fitness_function(current)
        T = schedule_function(t)
        if T <= 0:
            return current,current_fitness
        #Modification step
        #generates next step and calculates fitness
        
        neighbour = generate_next_state(current,tweak_function)
        neighbour_fitness = fitness_function(neighbour)
        delta_E = neighbour_fitness - current_fitness
        if delta_E>0:
            current = neighbour
            
        else:
        #Choosing worse solution based on probability    
            selection_probability = math.exp(delta_E/T)
            random_generated_value = random.random()
            if random_generated_value <= selection_probability:
                current = neighbour
                
    return current,current_fitness
    
if __name__ == "__main__":

    random.seed()
    print("Solving 5 queen 3 rooks problem")
    #You can use shuffle_function instead of swap_function
    solution, fitness = (do_simulated_annealing(swap_function,do_linear_schedule))
    print("Solution using Simulated Annealing")
    printBoard(solution)
    print("Fitness is ",fitness)
    