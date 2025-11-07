# Exercise 6: An unexpected coding journey
    # A word is considered elfish if it contains all the letters: e, l, and f in it, in any order. For
    # example, we would say that the following words are elfish: whiteleaf, tasteful, unfriendly, and
    # waffles, because they each contain those letters.
        # a) Write a predicate function called iselfish(word) that, given a word, tells us if that
        # word is elfish or not. The function must be recursive.
        # b) Write something_ish(pattern, word) a more generalized predicate function
        # that, given two words, returns true if all the letters of pattern are contained in word.
        # I did not provide a unit test for this exercise, if you wish you could try to create a unit test for
        # that exercise and share it with someone else to test their code.

def iselfish(word:str) -> bool:
    if not word:
        return False
    
    ELFISH = "elf"

    if word[0].lower() in ELFISH:
        return True
    
    return iselfish(word[1:])

def something_ish(pattern:str, word:str) -> bool:
    if not word:
        return False

    if word[0].lower() in pattern:
        return True
    
    return iselfish(word[1:])