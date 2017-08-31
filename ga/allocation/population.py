from ga.allocation.DNA import DNA
from random import randint


class Population(object):
    def __init__(self,target,size,mutation_rate,cost,benefit):
        self.size=size
        self.elements=[]
        self.mating_pool=[]
        self.target=target
        self.generations=0
        self.mutation_rate=mutation_rate
        self.cost = cost
        self.benefit = benefit
        self.current_benefit = 1
        self.no_changes=0

        for _ in range(size):
            self.elements.append(DNA(len(cost),cost))

    def calculate_fitness(self):
        for element in self.elements:
            element.calculate_fitness(self.target)

    def generate_mating_pool(self):
        self.mating_pool=[]
        for element in self.elements:
            for _ in range(round(element.fitness_score*100)):
                self.mating_pool.append(element)
                #element.calculate_fitness(self.target)

    def reproduce(self):
        for index in range(len(self.elements)):
            #print (len(self.mating_pool))
            partnerA=self.mating_pool[randint(0,len(self.mating_pool)-1)]
            partnerB=self.mating_pool[randint(0,len(self.mating_pool)-1)]
            child=partnerA.crossover(partnerB)
            child.mutate(self.mutation_rate,self.target)
            self.elements[index]=child
        self.generations += 1

    def evaluate(self):
        found = False
        element_cost = 0
        benefit=0
        for element in self.elements:
            #print(element.genes,element.fitness_score)
            element_cost=0
            benefit=0
            for key,val in enumerate(element.genes):
                element_cost = element_cost + (val*self.cost[key])
                benefit = benefit + (val*self.benefit[key])
                #print (value,element_cost,self.target)
            if element_cost <= self.target:
                if benefit >= self.current_benefit:
                    self.no_changes += 1
                    self.current_benefit=benefit
                if benefit >= self.current_benefit and self.no_changes > 60:
                    found = True
                print (element_cost,self.target,self.current_benefit,self.no_changes)

            if found:
                print (element.genes)
                break

        return found





