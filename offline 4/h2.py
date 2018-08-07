import random
import math
from itertools import permutations


def generate_random_permutation_of_char(combination1 = 'qqqqqrrr'):
    
    perms1 = permutations(combination1)
    permList1 = list(perms1)
    idx1 = random.randint(0,len(permList1))  
    random_combination1 = ''.join(permList1[idx1])
     
    return random_combination1
    
    