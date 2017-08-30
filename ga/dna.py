from random import randint
import math

class DNA(object):
    def __init__(self,length):
        self.length=length
        self.genes = []
        self.fitness_score=0
        for _ in range(length):
            ascii_num = randint(63, 122)
            if ascii_num == 63 or (ascii_num > 90 and ascii_num < 97):
                ascii_num = 32
            self.genes.append(chr(ascii_num))

    def calculate_fitness(self,target):
        self.fitness_score=0
        for index in range(len(self.genes)):
            if self.genes[index] == target[index]:
                self.fitness_score+=1
        self.fitness_score = float(self.fitness_score)/float(len(target))
        #self.fitness_score = pow(self.fitness_score,2)

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
            if self.genes[index] != target[index]:
                ascii_num = randint(63, 122)
                if ascii_num == 63 or (ascii_num > 90 and ascii_num < 97):
                    ascii_num = 32
                self.genes[index]=chr(ascii_num)
