# Original multi-dimensional list
multi_dim_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Flatten the list using list comprehension
flattened_list = [item for sublist in multi_dim_list for item in sublist]

# Print the flattened list
print(flattened_list)
