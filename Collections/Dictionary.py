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
final_dict = {}
general_dict = {}
list_with_idex = {}
# Creating an empty list with a random empty dicts
list_of_dicts = [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
#for each dict from list of dicts
for dct in list_of_dicts:
    # count of iteration for numbers of keys
    for i in range(random.randint(1, len(string.ascii_lowercase))):
        # creating pairs keys and values, a key is taken from list if letters and assigned with value from 0 to 100
        dct[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
#for each dict in the list of dicts
for dct in list_of_dicts:
    print(dct)
    # for each key from the dict
    for key in dct:
        # If kye not in the dict, add key to new_dict
        if key not in general_dict:
            general_dict[key] = dct.get(key)
        elif key in general_dict:
            general_dict[key] = max(dct.get(key),general_dict.get(key))
#add an index of a dict to the key
for i,dict in enumerate(list_of_dicts,start=1):
    for key in general_dict:
        for gkey in dict:
            if general_dict.get(key) == dict.get(key):
                list_with_idex[f'{key}_{i}'] = general_dict.get(key)
# if key more than one in the dicts, name of the key is just a lette, without index
for key in list_with_idex:
    #count how many times the key has been met in dicts
    s = sum(key[0] in d for d in list_of_dicts)
    if s == 1:
        final_dict[key[0]] = list_with_idex.get(key)
    else:
        final_dict[key] = list_with_idex.get(key)



print({key: final_dict[key] for key in sorted(final_dict)})