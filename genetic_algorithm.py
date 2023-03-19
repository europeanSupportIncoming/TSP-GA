import copy
import csv
import random
import time

from poulation import whole_population, evolve_next_gen, population_member


if __name__ == '__main__':
    # set up dictionairy to contain longitude and latitude
    town_positions = {}

    # read in town names and positions
    with open("/home/kothgasser-paul/Downloads/european-no-duplicates.csv") as townfile:
        reader = csv.reader(townfile)
        # skip first line
        reader.__next__()
        for line in reader:
            town_positions[line[0]] = [float(i) for i in line[1:]]

    # create separate list for town names
    town_names = list(town_positions.keys())

    population_size = 500

    first_generation = [population_member(random.sample(town_names, len(town_names)), town_positions) for i in range(population_size)]
    generation = 0
    elitism = int(0.1 * population_size)
    mutation_probability = 0.2

    current_population = whole_population(generation, elitism, mutation_probability, town_names.copy(), first_generation)
    current_fittest = current_population.order_by_fitness()[0].fitness_value()


    startime = time.time()
    while generation < 1000:
        old_fittest = copy.deepcopy(current_fittest)
        current_fittest = current_population.order_by_fitness()[0].fitness_value()
        
        current_population = evolve_next_gen(current_population)
        generation = current_population.generation
        if generation in [1, 10, 100, 150, 200, 400, 500, 700, 1000]:
            print(f'generation: {generation} || fitness : {current_population.order_by_fitness()[0].fitness_value()} || time {time.time() - startime}')
    print(f'generation: {generation} || fitness : {current_population.order_by_fitness()[0].fitness_value()} || time {time.time() - startime}')
    print(current_population.order_by_fitness()[0])
    print(time.time() - startime)
