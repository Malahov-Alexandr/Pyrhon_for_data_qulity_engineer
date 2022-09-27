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

new_dict = {}
final_dict = {}
# Creating a tuple with the letters for future dicts
list_of_letters = string.ascii_lowercase
# Creating an empty list with a random empty dicts
list_of_dicts = [{} for _ in range(random.randint(2, 10))]
# for each dict from list of dicts
for current_dict in list_of_dicts:
    # count of iteration for numbers of keys
    for i in range(random.randint(1, len(list_of_letters))):
        # creating pairs keys and values, a key is taken from list if letters and assigned with value from 0 to 100
        current_dict[random.choice(list_of_letters)] = random.randint(0, 100)
# iteration for each dict in the list of dicts
for current_dict in list_of_dicts:
    # iteration for each key from a dict
    for current_key in current_dict:
        # check that the key is not in the new_dict, if key is not in the new_dict, new dict is updated with the
        # key, and it's value
        if current_key not in new_dict:
            new_dict[current_key] = current_dict.get(current_key)
# Iteration each dict in the list of the dicts
for rest_dict in list_of_dicts:
    # for each key in the dict
    for rest_key in rest_dict:
        # if the key is already in the new_dict then compare theis value and if new value is higher key is updated
        # with '_' and the highest value
        if rest_key in new_dict:
            # comparing existed in the new_dict value and new value of the rest keys
            if new_dict.get(rest_key) < rest_dict.get(rest_key):
                # if a new key's value is higher than existed, current key has name "name+'_'" and new value
                new_dict[rest_key + '_'] = rest_dict.get(rest_key)
                # deleting old key from the dict
                new_dict.pop(rest_key)
print(new_dict)
