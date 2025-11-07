# Exercise 2:
    # To compute the sum of all elements in a list, you can use the built-in function sum.
    # For example:
        # >>> sum([1,2,3,4])
        # 10
        # >>> sum([])
        # 0
    # Write a recursive function rec_sum(numbers) that take a list of integers as a parameter
    # and returns the sum of all the elements in the list. The function should return 0 if the list is
    # empty.

def rec_sum(numbers:list[int]) -> int:
    if len(numbers) < 1:
        return 0
    
    return numbers[0] + rec_sum(numbers[1:])