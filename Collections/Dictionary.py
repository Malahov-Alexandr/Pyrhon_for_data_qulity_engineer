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


def dicts_generator():
    import random
    import string
    # Creating an empty list with a random empty dicts
    list_of_dicts = [{} for _ in range(random.randint(2, 10))]
    # for each dict from list of dicts
    for current_dict in list_of_dicts:
        # count of iteration for numbers of keys
        for i in range(random.randint(1, len(string.ascii_lowercase))):
            # creating pairs keys and values, a key is taken from list if letters and assigned with value from 0 to 100
            current_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
    return list_of_dicts


def key_counter(lst):
    import collections
    # create a list and collect all value of each key
    result = collections.defaultdict(list)
    for dictionary in lst:
        for key, value in dictionary.items():
            result[key].append(value)
    return result


def max_value(m_value):
    final_dict = {}
    # found index of max value and add it to the name of the key
    for key, value in m_value.items():
        if len(value) > 1:
            final_dict[f'{key}_{value.index(max(value)) + 1}'] = max(value)
        else:
            final_dict[key] = max(value)
    print(final_dict)


max_value(key_counter(dicts_generator()))
