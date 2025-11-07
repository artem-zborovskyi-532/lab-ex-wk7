# Exercise 4:
    # Write a recursive function flatten(mlist) where mlist is a multidimensional list that
    # returns all the element from mlist into a one-dimensional list. Note, empty lists are ignored.
    # For examples:
        # >>> flatten([1,[2,3],4])
        # [1,2,3,4]
        # >>> flatten([1,[2,[3,[4]]]])
        # [1,2,3,4]
        # >>> flatten([1,2,3,4])
        # [1,2,3,4]
        # >>> flatten([1,[]])
        # [1]

def flatten(mlist) -> list:
    res = []
    for el in mlist:
        if type(el) == list:
            res += flatten(el)
        else:
            res.append(el)

    return res