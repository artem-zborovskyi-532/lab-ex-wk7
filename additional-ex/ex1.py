# Exercise 1:
    # 1. Write a recursive function print_all(numbers) that prints all the
    # elements of list of integers, one per line (use no while loops or for loops).
    # The parameters numbers to the function is a list of int.
    # 2. Same problem as the last one but prints out the elements in reverse order.

def print_all(numbers:list[int]) -> None:
    if not numbers:
        return
    
    print(numbers[0])
    print_all(numbers[1:])

def print_all_reverse(numbers:list[int]) -> None:
    if not numbers:
        return
    
    print(numbers[-1])
    print_all_reverse(numbers[:-1])