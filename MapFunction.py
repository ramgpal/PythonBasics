# Function to square a number
def square(x):
    return x ** 2
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Applying the square function to each element in the numbers list using map()
squared_numbers = map(square, numbers)
# Convert the map object to a list to see the results
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]
