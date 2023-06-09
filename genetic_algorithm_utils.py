import copy
import math
import random
import numpy as np

#haversine function, to calculate distance
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


#mutate children to avoid inbreeding
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
def create_list(parent1: list, parent2: list, mutation_probability : float) -> list:
    # Choose two random crossover points
    cxpoint1 = random.randint(0, len(parent1) - 1)
    cxpoint2 = random.randint(0, len(parent1) - 1)
    if cxpoint2 < cxpoint1:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    # Replace the elements between the two crossover points with elements from unused parent
    child = parent1[cxpoint1:cxpoint2+1]

    for i in range(cxpoint2, len(parent2)):
        if parent2[i] not in child:
            child.append(parent2[i])

    for i in range(0, cxpoint1+1):
        if parent2[i] not in child:
            child.append(parent2[i])

    for i in range(cxpoint1, cxpoint2+1):
        if parent2[i] not in child:
            child.append(parent2[i])

    #mutate the child
    child = mutate(child, mutation_probability)
    return child


