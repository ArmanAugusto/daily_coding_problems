# Daily Coding Problem #1

# Given a list of numbers and a number k, return whether any two numbers from the list
# add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

########################################################################################

# dcp1.py

input_num_list = input('\n\nEnter a list of numbers separted by a space (press enter when finished):  ')
num_list = input_num_list.split()
num_list = list(map(int, num_list))

k = input('\nNow enter a number that will be checked if any two numbers from the list add up to it:  ')
k = int(k)
print("The word 'TRUE' will be displayed if a sum is found.")

print('\nYour list:  ', num_list)
print('\nYour sum to be checked:  ', k)
print('\n')

check_list = set()
for num in num_list:
    if k - num in check_list:
        print('True\n\n')
    check_list.add(num)

