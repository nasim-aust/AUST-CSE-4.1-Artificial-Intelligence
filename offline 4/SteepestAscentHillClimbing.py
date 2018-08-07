"""
import header.py and all its functions
"""

import helper
from helper import *

def do_steepest_ascent_hill_climbing(tweak_function = swap_function):
    
    """
    Runs steepest ascent hill climmbing algorithm
    Keyword argument:
    tweak_function- the tweaking function you want to use- it can be swap_function(default) or shuffle_function
    returns solution state and its fitnes
    """
    #Initialization step
    current_fitness = None
    current = generate_random_permutation()
    iteration = 200 #number of iterations, you can change it
    number_of_tweaks = 10 #number of tweaks, you can change it
    
    while(iteration>=0):
        iteration -=1
        current_fitness = fitness_function(current) #calculating fitness
        #print('current',current, current_fitness)
        if current_fitness == 28:
            break
        #Modification step
        #generates next step and calculates fitness
        
        neighbour = generate_next_state(current,tweak_function)
        
        neighbour_fitness = fitness_function(neighbour)
        #print('neighbour',neighbour, neighbour_fitness)
        #Choosing new generation from candidates
        for i in range(1,number_of_tweaks):
            
            candidate_neighbour = generate_next_state(current,tweak_function) 
            candidate_neighbour_fitness = fitness_function(neighbour)
            if neighbour_fitness < candidate_neighbour_fitness:
                #print("assigning")
                neighbour = candidate_neighbour
    
        
        if current_fitness < neighbour_fitness:
            #print("assigning")
            current = neighbour

    return current,current_fitness
    
    
if __name__ == "__main__":

    random.seed()
    print("Solving 5 queen 3 rook problem")
    #You can use shuffle_function instead of swap_function
    solution, fitness = (do_steepest_ascent_hill_climbing(swap_function))
    print("Solution using Steepest Ascent Hill Climbing")
    printBoard(solution)
    print("Fitness is ",fitness)
    
