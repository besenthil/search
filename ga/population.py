from ga.dna import DNA
from random import randint

class Population(object):
    def __init__(self,target,size,mutation_rate):
        self.size=size
        self.elements=[]
        self.mating_pool=[]
        self.target=target
        self.generations=0
        self.mutation_rate=mutation_rate

        for _ in range(size):
            self.elements.append(DNA(len(self.target)))

    def calculate_fitness(self):
        for element in self.elements:
            element.calculate_fitness(self.target)

    def generate_mating_pool(self):
        for element in self.elements:
            for _ in range(round(element.fitness_score*10)):
                self.mating_pool.append(element)
                element.calculate_fitness(self.target)

    def reproduce(self):
        for index in range(len(self.elements)):
            partnerA=self.mating_pool[randint(0,len(self.mating_pool)-1)]
            partnerB=self.mating_pool[randint(0,len(self.mating_pool)-1)]
            child=partnerA.crossover(partnerB)
            child.mutate(self.mutation_rate,self.target)
            self.elements[index]=child
        self.generations+=1





