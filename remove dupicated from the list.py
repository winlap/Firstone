my_list = [1, 2, 3, 3, 4, 4, 5]

# create a new list to hold unique values
unique_list = []

# iterate over each element in the original list
for elem in my_list:
    # if the element is not already in the unique list, add it
    if elem not in unique_list:
        unique_list.append(elem)

# print the unique list
print(unique_list)
