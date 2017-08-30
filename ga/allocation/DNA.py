from random import randint
import math


class DNA(object):
    def __init__(self,length):
        self.length=length
        self.genes = []
        self.fitness_score=0
        for _ in range(length):
            ascii_num = randint(0, 11)
            self.genes.append(ascii_num)

    def calculate_fitness(self,target):
        if sum(self.genes) == target:
            self.fitness_score=1
        else:
            self.fitness_score = float(1)/float(abs(target-sum(self.genes)))
            print (self.fitness_score)

    def crossover(self,partner):
        midpoint = randint(0,len(self.genes))
        #midpoint = int(len(self.genes)/2)
        child = DNA(self.length)
        child.genes=self.genes[:midpoint]+partner.genes[midpoint:]
        return child

    def mutate(self,mutation_rate,target):
        num_chars = int(math.ceil(mutation_rate*self.length))
        for _ in range(num_chars):
            index=randint(0,self.length-1)
            for _ in range(self.length):
                ascii_num = randint(0, 11)
                self.genes[index] = ascii_num