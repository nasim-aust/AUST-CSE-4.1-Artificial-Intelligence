import sys
import copy
import math
import random
rook_count = 3

class Board:
    def __init__(self, board_size, goal):
        self.board_size = board_size
        self.goal = goal
        self.fitness = 0
        self.queens = []
        self.queens_index = {}
        for i in range(self.board_size-rook_count):
            s = "Q"+str(i)
            self.queens.append(s)
            self.queens_index[s] = i
            
        for i in range(rook_count):
            s = "R"+str(i)
            self.queens.append(s)
            self.queens_index[s] = i+self.board_size-rook_count
        '''
        for i in range(len(self.queens)):
            print(self.queens[i], "  pos = ", self.queens_index[self.queens[i]])
        
        self.queens=list(range(self.board_size-rook_count))
        self.rooks=list(range(rook_count))
        '''
        self.switch(self.board_size/2)

    def __del__(self):
        pass

    def switch(self, count):
        count=int(count)

        for i in range(count):
            j = random.randint(0, self.board_size-1)
            k = random.randint(0, self.board_size-1)
            #self.queens_index[self.queens[j]],self.queens_index[self.queens[k]] =  self.queens_index[self.queens[k]], self.queens_index[self.queens[j]]
            self.queens[j], self.queens[k] = self.queens[k], self.queens[j]

        self.compute_fitness()

    def regenerate(self):
        self.switch(2)

        if random.uniform(0,1) < 0.25:
            self.switch(1)

    def compute_fitness(self):
        self.fitness = self.goal
        for i in range(self.board_size):
            for j in range(i+1, self.board_size):
                #if(self.queens[i][0] == 'Q'):
                if math.fabs(self.queens_index[self.queens[i]] - self.queens_index[self.queens[j]]) == j - i:
                    self.fitness-=1
                '''
                elif(self.queens[i][0] == 'R'):
                    if(self.queens_index[self.queens[i]] == self.queens_index[self.queens[j]]):
                        self.fitness-=1
                '''
    def print_board(self):
        ''' prints current board in a nice way!'''
        for row in range(self.board_size):
            print ("", end="|")
            s = self.queens[row]
            idx = self.queens_index[s]
            for col in range(self.board_size):
                if col == idx:
                    if(s[0] == 'Q'):
                        print ("Q", end="|")
                    else:
                        print ("R", end="|")
                else:
                    print ("_", end="|")
            print ("")

class GaQueens:
    def __init__(self, board_size, population_size, generation_size):
        self.board_size = board_size
        self.population_size = population_size
        self.generation_size = generation_size

        self.generation_count = 0
        self.goal = int((self.board_size*(self.board_size-1))/2)
        self.population = []
        self.first_generation()

        while True:
            if self.is_goal_reached() == True:
                break
            if -1 < self.generation_size <= self.generation_count:
                break
            self.next_generation()

        print ("==================================================================")

        if -1 < self.generation_size <= self.generation_count:
            print ("Couldn't find result in %d generations" % self.generation_count)
        elif self.is_goal_reached():
            print ("Correct Answer found in generation %s" % self.generation_count)
            for population in self.population:
                if population.fitness == self.goal:
                    print (population.queens)
                    population.print_board()

    def __del__(self):
        pass

    def is_goal_reached(self):
        for population in self.population:
            if population.fitness == self.goal:
                return True
        return False

    def random_selection(self):
        population_list = []
        for  i in range(len(self.population)):
            population_list.append((i, self.population[i].fitness))
        population_list.sort(key=lambda pop_item: pop_item[1], reverse=True)
        return population_list[:int(len(population_list)/3)]

    def first_generation(self):
        ''' creates the first generation '''
        for i in range(self.population_size):
            self.population.append(Board(self.board_size, self.goal))

        self.print_cross()

    def next_generation(self):
        ''' creates next generations (all except first one)'''

        # add to generation counter
        self.generation_count+=1

        # get a list of selections to create next generation
        selections = self.random_selection()

        # creates a new population using given selection
        new_population = []
        while len(new_population) < self.population_size:
            sel = random.choice(selections)[0]
            new_population.append(copy.deepcopy(self.population[sel]))
        self.population = new_population

        for population in self.population:
            population.regenerate()

        self.print_cross(selections)

    def print_cross(self, selections=None):
        print ("Cross over #%d" % self.generation_count)

        if selections == None:
            selections = []

        print ("       Using: %s" % str([sel[0] for sel in selections]))

        count = 0
        for population in self.population:
            print ("%8d : (%d) %s" % (count, population.fitness, str(population.queens)))
            population.print_board()
            count+=1
            
if __name__ == '__main__':
    board_size = 8
    population_size = 20
    generation_size = -1

    # if there is arguments use them instead of default values
    if len(sys.argv) == 4:
        board_size = int(sys.argv[1])
        population_size = int(sys.argv[2])
        generation_size = int(sys.argv[3])

    # print some information about current quest!
    #print ("Starting:")
    #print ("    board size      : ", board_size)
    #print ("    population size : ", population_size)
    #print ("    generation size : ", generation_size)
    #print ("==================================================================")

    GaQueens(board_size, population_size, generation_size)
