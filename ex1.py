# Exercise 1:
    # Write a recursive function ispalindrome(word) that returns true if the string word is a
    # palindrome, false otherwise. You can start with an implementation that does not deal with
    # punctuation, and then refactor your code to take into account punctuation.

def ispalindrome(word: str) -> bool:
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False

    return ispalindrome(word[1:-1])