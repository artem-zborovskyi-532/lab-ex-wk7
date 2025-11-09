# Exercise 2: from “Python Programming Fundamental”- Kent L, 2 nd Ed. (2014)
    # There is an elegant algorithm for converting a decimal number to a binary number. You need
    # to carry out long division by 2 to use this algorithm. If we want to convert 83 10 to binary, then
    # we can repeatedly perform long division by 2 on the quotient of each result until the quotient
    # is zero. Then, the string of the remainders that were accumulated while dividing make up the
    # binary number. For example,
        # 83/2 = 41 remainder 1
        # 41/2 = 20 remainder 1
        # 20/2 = 10 remainder 0
        # 10/2 = 5 remainder 0
        # 5/2 = 2 remainder 1
        # 2/2 = 1 remainder 0
        # 1/2 = 0 remainder 1
    # The remainders from last to first are (1010011)2 which is (83)10.
        # a) Implement a recursive function to_binary(number) that takes a positive integer
        # as parameter and returns a binary representation of that number as a string.
        # b) Implement the reverse function to_base10(binary) that takes a string containing
        # a binary number and returns its representation in base 10. The function must be
        # recursive. To test your solution once implemented to_base10(to_binary(83))
        # should return 83.

def to_binary(number:int) -> str:
    if number == 1:
        return "1"
    
    return to_binary(number // 2) + str(number % 2)

def to_base10(binary_str):
    if not binary_str:
        return 0
    
    first_digit = int(binary_str[0])
    
    power = len(binary_str) - 1
    
    return first_digit * pow(2, power) + to_base10(binary_str[1:])