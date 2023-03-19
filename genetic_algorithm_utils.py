import copy
import math
import random
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    r = 6371  # radius of Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c
    return d

# get euclidean distance from latitude and longitude
def distance(town_one: str, town_two: str, town_positions):
    town_one_position = town_positions[town_one]
    town_two_position = town_positions[town_two]
    lat1 = town_one_position[0]
    lat2 = town_two_position[0]
    lon1 = town_one_position[1]
    lon2 = town_two_position[1]

    r = 6371  # radius of Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c
    return d

import random

def mutate(original: list, mutation_probability: float) -> list:
    #randomly set mutation to True or False
    mutation_yes = random.uniform(0, 1)
    #select how many strings to mutate, as 20%, but always even amount
    number_of_strings_to_mutate = max(2, round(len(original)*0.2))
    #switch randomly chosen strings
    if mutation_yes <= mutation_probability:
        string_positions = random.sample(list(np.arange(len(original))), k=number_of_strings_to_mutate)
        for i in range(0, len(string_positions), 2):
            index1, index2 = string_positions[i], string_positions[i + 1]
            original[index1], original[index2] = original[index2], original[index1]
    return original









# function to generate new population member from old one
def create_list(parent1: list, parent2: list, p1: float, p2: float, mutation_probability : float) -> list:
    # Choose two random crossover points
    cxpoint1 = random.randint(0, len(parent1) - 1)
    cxpoint2 = random.randint(0, len(parent1) - 1)
    if cxpoint2 < cxpoint1:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    parents = [parent1, parent2]
    prob_list = [p1, p2]
    # Create the child as a copy of one parent, weighted by fitness probability
    child = copy.deepcopy(random.choices(parents, weights=prob_list, k=1)[0])
    #remove already used parent
    parents.remove(child)
    # Replace the elements between the two crossover points with elements from unused parent
    for i in range(cxpoint1, cxpoint2 + 1):
        if parents[0][i] not in child[cxpoint1:cxpoint2 + 1]:
            child[i] = parents[0][i]
        else:
            for j in range(cxpoint2 + 1, len(parent1)):
                if parent2[j] not in child:
                    child[j] = parent2[i]
                    break
    child = mutate(child, mutation_probability)
    return child

