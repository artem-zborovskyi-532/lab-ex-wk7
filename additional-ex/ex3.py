# Exercise 3:
    # We are given a set of items, each with a weight and a value and we need to determine the
    # number of each item to include in a collection (a bag for example) so that the total weight is
    # less than or equal to a given limit and the total value is as large as possible. In addition, the
    # items are indivisible; we can either take an item or not. Note that there might be more than one
    # item with same value and same weight. For example,
    #     Input:
    #     value = [20, 5, 5, 10, 40, 15, 25]
    #     weight = [1, 2, 2, 3, 8, 7, 4]
    #     max_weight = 10
    #     Output: 60
    #     value = 20 + 40 = 60
    #     weight = 1 + 8 = 9
    # The idea is to use recursion to solve this problem. For each item, there are two possibilities
    #     1. We include current item in the bag and recur for remaining items with decreased
    #     capacity of the bag. If the capacity becomes negative, do not recur or return -INFINITY.
    #     2. We exclude current item from the bag and recur for remaining items
    # Finally, we return maximum value we get by including or excluding current item. The base
    # case of the recursion would be when no items are left, or capacity becomes 0.

    # Naïve Implementation:
    #     Implement fill_bag(max_weight, values, weights) a naïve implementation that
    #     try all possible solution and returns the maximum.
    # Memoization
        # The time complexity of a naïve implementation of above solution is exponential 𝑂𝑂(2𝑛𝑛) and
        # auxiliary space used by the program is constant 𝑂𝑂(1). However, the above solution has an
        # optimal substructure, that is optimal solution can be constructed efficiently from optimal
        # solutions of its subproblems. It also has overlapping subproblems, that is the problem can be
        # broken down into subproblems which are reused several times (in the same way as computing
        # the Fibonacci sequence 𝐹𝐹2 was used multiple times). In order to reuse subproblems solutions,
        # we can apply Dynamic Programming, in which subproblem solutions are memoized (this is
        # the correct spelling by the way) rather than computed over and over again.
        # Try to find by yourself, how subproblem can be memoized rather than looking at the solution
        # on the web. As a hint, I can tell you that the space needed to store the information is of size
        # 𝑛𝑛 × 𝑤𝑤 where n is the number of items available, and w is the maximum weight allowed.

# Naïve Implementation:

def fill_bag(max_weight:int, values:list[int], weights:list[int]) -> int:
    if not values or not weights:
        return 0
    
    arr = []

    for i, w in enumerate(weights):
        remaining_weight = max_weight - w
        if remaining_weight < 0:
            continue
        v = values[i] + fill_bag(remaining_weight, values[i + 1:], weights[i + 1:])
        arr.append(v)

    if arr:
        return max(arr)
    else:
        return 0
    
# Memoization:

def fill_bag_memo(max_weight:int, values:list[int], weights:list[int]) -> int:
    memo = {}

    def helper(index:int, remaining_weight:int) -> int:
        if index >= len(values) or remaining_weight <= 0:
            return 0

        key = (index, remaining_weight)
        if key in memo:
            return memo[key]

        best_value = 0
        for i in range(index, len(values)):
            w = weights[i]
            if w <= remaining_weight:
                v = values[i] + helper(i + 1, remaining_weight - w)
                best_value = max(best_value, v)

        memo[key] = best_value
        return best_value

    return helper(0, max_weight)