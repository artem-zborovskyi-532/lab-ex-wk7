# Exercise 5: (from seminar 1)
    # Write a recursive function merge(sorted_listA, sorted_listB) that merges the
    # two lists into a single sorted list and returns it. The two parameters are list of comparable
    # objects that are sorted in ascending order. For example, the lists contain only strings, or the
    # lists contain only numbers. Neither of the two lists in the parameters must be modified.

def merge(sorted_listA: list, sorted_listB: list) -> list:
    if not sorted_listA:
        return sorted_listB
    if not sorted_listB:
        return sorted_listA

    if sorted_listA[0] < sorted_listB[0]:
        return [sorted_listA[0]] + merge(sorted_listA[1:], sorted_listB)
    else:
        return [sorted_listB[0]] + merge(sorted_listA, sorted_listB[1:])