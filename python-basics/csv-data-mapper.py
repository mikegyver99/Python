# Write a script that converts this into a list of dictionaries,
# where the first list provides the keys.
data = [["Name", "Age"], ["Alice", "25"], ["Bob", "30"]]
# Your code here
keys = data[0]
# print(keys)
my_list = []
for row in data[1:]:
    print(list(zip(keys, row))) # list() to convert the zip object into a list
    print(dict(zip(keys, row))) # dict() to convert the zip object into a dictionary
    my_list.append(dict(zip(keys, row)))
print(my_list)

# keys = data[0]
# result = []
# for row in data[1:]:
#     entry = {}
#     for i in range(len(keys)):
#         entry[keys[i]] = row[i]
#     result.append(entry)
# print(result)
