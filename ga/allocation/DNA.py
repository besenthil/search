from random import randint
import math


class DNA(object):
    def __init__(self,length,cost):
        self.length=length
        self.genes = []
        self.fitness_score=0
        self.cost=cost
        for index in range(0,self.length):
            ascii_num = randint(0, 1)
            self.genes.append(ascii_num)

    def calculate_fitness(self,target):
        element_cost=0
        for key,value in enumerate(self.genes):
            #print (key,value)
            element_cost += value*self.cost[key]

        if element_cost == target:
            self.fitness_score=1
        else:
            self.fitness_score = float(1)/float(abs(target-element_cost))
            #print (self.fitness_score)

    def crossover(self,partner):
        midpoint = randint(0,len(self.genes))
        #midpoint = int(len(self.genes)/2)
        child = DNA(self.length,self.cost)
        child.genes=self.genes[:midpoint]+partner.genes[midpoint:]
        return child

    def mutate(self,mutation_rate,target):
        num_chars = int(math.ceil(mutation_rate*self.length))
        for _ in range(num_chars):
            index=randint(0,self.length-1)
            for _ in range(self.length):
                ascii_num = randint(0, 1)
                self.genes[index] = ascii_num