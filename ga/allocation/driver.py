from ga.allocation.population import Population
import time
import sys

TARGET = [0,0,0,0]
TARGET_COST=25
POPULATION_SIZE=5
MUTATION_RATE=0.01

if __name__ == "__main__":
    for _ in range(1):
        pop = Population(TARGET_COST,POPULATION_SIZE,MUTATION_RATE)
        found = False
        while (not found):
            pop.calculate_fitness()
            pop.generate_mating_pool()
            found = pop.evaluate()
            for element in pop.elements:
                print (element.genes,element.fitness_score)
            pop.reproduce()
            print ('Number of generations : ', pop.generations)

