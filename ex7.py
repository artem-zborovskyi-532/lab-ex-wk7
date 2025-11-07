# Exercise 7:
    # A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a recursive
    # function called is_power(a,b) that takes parameters a and b and returns True if a is a
    # power of b, False otherwise.
    # For example:
        # • 27 is power of 3 if 27/3 = 9 is power of 3, that is 9/3 = 3 is power of 3, which is true.
        # • 18 is power of 3 if 18/3 = 6 is power of 3, that is if 6/3 = 2 is power of 3 which is false.
    # Could you also write an iterative version of this function?

def is_power(a:int, b:int) -> bool:
    if a == b:
        return True
    if a % b == 0 and is_power(a // b, b):
        return True
    else: return False

def is_power_iterative(a:int, b:int) -> bool:
    while a > 1:
        if a % b != 0:
            return False
        a //= b
    return True