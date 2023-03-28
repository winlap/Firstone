# List of elements
n = int(input("Enter the number of element for list"))
lst = []
for x in range(1,n):
    lst.append(int(input("Enter the element of list: ")))
    
# Create an empty dictionary to store element frequency
freq_dict = {}

# Count frequency of each element in the list
for element in lst:
    if element in freq_dict:
        freq_dict[element] += 1
    else:
        freq_dict[element] = 1

# Find the element with the highest frequency
most_freq_element = max(freq_dict, key=freq_dict.get)

# Print the most frequent element and its frequency
print("Most frequent element:", most_freq_element)
print("Frequency:", freq_dict[most_freq_element])
