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


def breed_with(parent1: population_member, parent2: population_member, mutation_probability: float) -> population_member:

    child_townlist = create_list(parent1.ordered_towns, parent2.ordered_towns, mutation_probability)
    child_town_position_dic = parent1.town_positions
    child = population_member(child_townlist, child_town_position_dic)
    return child

