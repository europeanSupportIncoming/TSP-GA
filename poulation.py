import copy
import random
import time
from dataclasses import dataclass, field

from population_member import population_member, breed_with

@dataclass
class whole_population:
    generation: int
    elitism: float
    mutation_probability: float
    population: list[population_member] = field(default_factory=list)

    def order_by_fitness(self) -> dict:
        return sorted(self.population, key=lambda x: x.fitness_value())


def evolve_next_gen(parent_gen: whole_population, paernthood_choice: int) -> whole_population:
    # get the elite gene members into the next round
    generation_index = parent_gen.generation
    elitism = parent_gen.elitism
    mutation_probability = parent_gen.mutation_probability
    current_gen_sorted = parent_gen.order_by_fitness()
    next_gen = current_gen_sorted[:elitism]
    # mate into new generation
    while len(next_gen) < len(current_gen_sorted):
        parent_1, parent_2 = random.sample(current_gen_sorted[:parenthood_choice +1], k=2)
        while parent_1 == parent_2:
            parent_1, parent_2 = random.sample(current_gen_sorted, k=2)

        next_gen.append(breed_with(parent_1, parent_2, mutation_probability))

    return whole_population(generation_index+1, elitism, mutation_probability, next_gen)

