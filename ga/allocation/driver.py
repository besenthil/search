from ga.allocation.population import Population
import time
import sys
from random import randint

COST = [randint(1,10) for _ in range(1,30)]
print (COST)
BENEFIT = [randint(1,10) for _ in range(1,30)]
#COST=[2,3,2,1,4,10]
#BENEFIT=[1,1,1,1,1,1]

TARGET_COST=14
POPULATION_SIZE=50
MUTATION_RATE=0.01

if __name__ == "__main__":
    for _ in range(1):
        pop = Population(TARGET_COST,POPULATION_SIZE,MUTATION_RATE,COST,BENEFIT)
        found = False
        while (not found):
            pop.calculate_fitness()
            pop.generate_mating_pool()
            #print(pop.elements)
            #print(pop.mating_pool)
            #for element in pop.elements:
            #    print (element.genes,element.fitness_score)
            pop.reproduce()
            found = pop.evaluate()
            #print ('Number of generations : ', pop.generations)


