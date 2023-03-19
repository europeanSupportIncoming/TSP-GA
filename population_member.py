import copy
from dataclasses import dataclass, field
from typing import Tuple

from genetic_algorithm_utils import distance, create_list


@dataclass
class population_member:
    #list of town names in order used
    ordered_towns: list
    town_positions: dict = field(default_factory=dict)


    def fitness_value(self) -> float:
        path_length = distance(self.ordered_towns[0], self.ordered_towns[-1], self.town_positions)
        for list_position, town_name in enumerate(self.ordered_towns[:-1]):
            path_length += distance(town_name, self.ordered_towns[list_position + 1], self.town_positions)
        return path_length


def get_probabilities(parent1: population_member, parent2: population_member) -> Tuple[float, float]:
    fitness_1 = parent1.fitness_value()
    fitness_2 = parent2.fitness_value()
    total_fitness = fitness_1 + fitness_2
    # take the probability from the other fitness, as the lowest score gets the highest probability
    p1 = fitness_2/total_fitness
    p2 = fitness_1/total_fitness
    return p1, p2


def breed_with(parent1: population_member, parent2: population_member, mutation_probability: float) -> population_member:
    #get 3 probabilites which add up to 1
    p1, p2 = get_probabilities(parent1, parent2)
    mutation_probability = min(mutation_probability, p1, p2)
    p1 -= mutation_probability/2
    p2 -= mutation_probability/2

    child_townlist = create_list(parent1.ordered_towns, parent2.ordered_towns, p1, p2, mutation_probability)
    child_town_position_dic = parent1.town_positions.copy()
    child = population_member(child_townlist, child_town_position_dic)
    return child

