# The Goal: Given the list numbers = [1, 5, 8, 12, 15, 20, 27, 30], 
# use a List Comprehension to create a new list that only contains numbers greater than 10 that are also even.
numbers = [1, 5, 8, 12, 15, 20, 27, 30]
# AI
filtered_numbers = [num for num in numbers if num > 10 and num % 2 == 0]
print(filtered_numbers)

# Me
new_list = []
for num in numbers:
    if num > 10 and num % 2 == 0:
        new_list.append(num)
print(new_list)