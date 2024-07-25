import statistics
import math

# Example list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate mean
mean = sum(numbers) / len(numbers)

# Calculate median
median = statistics.median(numbers)

# Calculate standard deviation
std_dev = statistics.stdev(numbers)

# Print the results
print(f"List: {numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
