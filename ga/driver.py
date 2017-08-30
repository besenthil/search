from ga.population import Population
import time
import sys

TARGET = list('tobeornotto')
POPULATION_SIZE=200
MUTATION_RATE=0.01

if __name__ == "__main__":
    for _ in range(100):
        pop = Population(TARGET,POPULATION_SIZE,MUTATION_RATE)
        found=False
        while (not found):
            pop.calculate_fitness()
            pop.generate_mating_pool()
            for element in pop.elements:
                #print (element.genes,element.fitness_score)
                if ''.join(TARGET) == ''.join(element.genes):
                    found = True
                    #print (element.genes,element.fitness_score)
                    break
            pop.reproduce()

                #print (element.genes,element.fitness_score)
        print (pop.generations)
        #time.sleep(1)

