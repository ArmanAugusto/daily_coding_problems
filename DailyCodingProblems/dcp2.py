# Daily Coding Problem #2

# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would
# be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
# would be [2, 3, 6].


def product_array(integer_list):
    new_list = []
    product = 0
    result = 1
    for i in integer_list:
        result *= i
    for j in integer_list:
        new_list.append(result / j)
    return (new_list)
        


input_lst = input('\n\nEnter a list of numbers with each number separated by a space (press enter when finished):  ')
lst = input_lst.split()
lst = list(map(int, lst))

print('\nList:  ', lst)

array_result = product_array(lst)
array_result = list(map(int, array_result))

print('\nProduct Array Result:  ', array_result)

print('\n')
