# Exercise 3: (from practical 03)
    # During practical 03, we implemented the function sum_digits(number) to calculate and
    # return the sum of digits of a given whole number (int) given as parameter. For example,
    # >>> print(sum_digits(1234))
    # 10
    # At the time we used loops in our implementation. This time you must use recursion. In
    # addition, you are not allowed to convert the int into a list or a string.

def sum_digits(number: int) -> int:
    if number == 0:
        return 0
    return (number % 10) + sum_digits(number // 10)