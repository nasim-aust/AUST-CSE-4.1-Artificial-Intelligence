import random
import re
import math
from itertools import permutations
import h2
from h2 import *

c = generate_random_permutation_of_char()
def generate_random_permutation(combination = '12345678'):

    perms = permutations(combination)
    permList = list(perms) 
    idx = random.randint(0,len(permList))    
    random_combination = ''.join(permList[idx])
     
    return random_combination
	 
def printBoard(combination):
   
    board_array = []
    for i in range(0,8):
        board_array.append([])
        for j in range(0,8):
            board_array[i].append("*")
	
    for i in range(len(combination)):
        board_array[i][int(combination[i])-1] = c[i]
    for i in range(0,8):
        print(board_array[i])

def swap_function(combination_main):
   
    combination = combination_main [:]
    i = random.randint(0,len(combination)-2)
    j = random.randint(i,len(combination)-1)
    list_combination = list(combination)
    list_combination[i],list_combination[j] = list_combination[j],list_combination[i]
    combination = ''.join(list_combination)
    return combination

def generate_next_state(combination, tweak_function = swap_function):
   
    return tweak_function(combination)

def fitness_function(combination):
    
    fitness = 28 #non-attacking pairs
    for i in range(0,7):
        for j in range(i+1,8):
            if re.match(r'q', c[i]):
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness -= 1 #one attacking pair found
					
    for i in range(7,0,-1):
        for j in range(i-1,-1,-1):
            if re.match(r'q', c[i]):
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness -= 1 #one attacking pair found	
    return fitness
