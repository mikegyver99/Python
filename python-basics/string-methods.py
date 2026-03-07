# The Goal: Write a function that takes a string (e.g., "apple banana apple cherry banana apple")
#  and returns a dictionary showing the count of each word.
my_string="apple banana apple cherry banana apple cherry cherry cherry"
# AI code
# def count_words(s):
#     word_count = {}
#     words = s.split()  # Split the string into words
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1  # Increment count if the word is already in the dictionary
#         else:
#             word_count[word] = 1   # Initialize count to 1 if the word is not in the dictionary
#     return word_count

# print(count_words(my_string))

# my code
words=my_string.split()
print(words)
word_count={}
print(word_count)
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
# try to sort the dictionary by value
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=False))
print(sorted_word_count)