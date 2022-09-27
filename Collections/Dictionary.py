# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.

import random
import string

general_dict = {}
# Creating a tuple with the letters for future dicts
list_of_letters = string.ascii_lowercase
# Creating an empty list with a random empty dicts
list_of_dicts = [{} for _ in range(random.randint(2, 10))]
# for each dict from list of dicts
for dct in list_of_dicts:
    # count of iteration for numbers of keys
    for i in range(random.randint(1, len(list_of_letters))):
        # creating pairs keys and values, a key is taken from list if letters and assigned with value from 0 to 100
        dct[random.choice(list_of_letters)] = random.randint(0, 100)
# for each dict in the list of dicts
for dct in list_of_dicts:
    # print for debug
    print(dct)
    # for each key from the dict
    for key in dct:
        # If kye not in the dict, add key to new_dict
        if key not in general_dict:
            general_dict[key] = dct.get(key)

# set variable for counting dicts
number = 0
# for each dict in list of dicts
for dct in list_of_dicts:
    # increase value by 1
    number += 1
    # for each key in dict
    for ky in dct:
        # if key has been already added to the new_dict, and it's value more that value already existed in the new_dict
        if ky in general_dict and dct.get(ky) > general_dict.get(ky):
            # assign for the key current name of the key + '_'+ number of dict
            general_dict[f'{ky}_{number}'] = max(dct.get(ky), general_dict.get(ky))
            # deleting old key
            general_dict.pop(ky)
print(general_dict)
