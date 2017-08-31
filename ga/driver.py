from ga.population import Population
import time
import sys

TARGET = list('To be or not to be')
POPULATION_SIZE=500
MUTATION_RATE=0.01

if __name__ == "__main__":
    for _ in range(10):
        pop = Population(TARGET,POPULATION_SIZE,MUTATION_RATE)
        found=False
        while (not found):
            pop.calculate_fitness()
            pop.generate_mating_pool()
            for element in pop.elements:
                #print (element.genes,element.fitness_score)
                if ''.join(TARGET) == ''.join(element.genes):
                    found = True
                    print (''.join(element.genes),element.fitness_score)
                    break
            pop.reproduce()

                #print (element.genes,element.fitness_score)
        print (pop.generations)
        #time.sleep(1)

