# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.

# Commit script to git repository and provide link as home task result.


# import 'random' library for random numbers
import random

# creating a list of 100 random numbers from 0 to 1000
rand_list = random.sample(range(0, 1000), 100)

# an empy list for a sorted list
sorted_list = []
list_of_odd_numbers = []
list_of_even_numbers = []

# while rand_list has the numbers execute next iteration
while rand_list:
    # creation the variable for first number in rand_list
    minimum = rand_list[0]  # arbitrary number in list
    # call a number from the rand_list
    for x in rand_list:
        # comparing the iteration number with the first number in the rand_list
        if x < minimum:
            # if the iteration number lower than the first number of the rand_list, the iteration number become a new
            # minimum number
            minimum = x
    # sorted_list append with the minimum number
    sorted_list.append(minimum)
    # deleting the iteration number from the rand_list
    rand_list.remove(minimum)

# searching the odd numbers from sorted list
for i in sorted_list:
    # checking the number whether the number is  an odd number
    if i % 2 != 0:
        list_of_odd_numbers.append(i)
    # if the number is not odd, adding the number to list_of_even numbers
    else:
        list_of_even_numbers.append(i)
# print the average value of the list with the odd numbers, the sum of all the numbers in the list divide by length of
# the numbers of the list
print(f'The average value of odd numbers is {sum(list_of_odd_numbers) * len(list_of_odd_numbers)}')
# print the average value of the list with the even numbers the sum of all the numbers in the list divide by length
# of the numbers of the list
print(f'The Average value of the even numbers is {sum(list_of_even_numbers) * len(list_of_even_numbers)}')
