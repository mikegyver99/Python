# The Goal: Create a function is_palindrome(word) that returns True if a word reads
#  the same backward as forward (like "radar" or "level") and False otherwise. 
list_words=["apple", "radar", "cherry", "level", "elderberry", "fig", "grape"]
def is_palindrome(p):
    for word in list_words:
        if word == word[::-1]:
            print(f"word is a palindrome,{word}")
        else:
            print(f"word is not a palindrome, {word}")
    return word
print(is_palindrome(list_words))
    