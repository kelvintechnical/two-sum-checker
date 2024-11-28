# Define a function to find two numbers in the list that add up to the target
def find_two_sum(numbers, target):  # 'numbers' is a list, 'target' is an integer
    # Loop through each number in the list using its index
    for i in range(len(numbers)):  # 'i' is an integer, used to track the current index
        # Loop through the numbers that come after the current number
        for j in range(i + 1, len(numbers)):  # 'j' is an integer, starting after 'i'
            # Check if the sum of the numbers at indices i and j equals the target
            if numbers[i] + numbers[j] == target:  # numbers[i] and numbers[j] are integers
                # Return the indices of the two numbers as a list
                return [i, j]  # List is used to group the two indices together
    # Return an empty list if no solution is found
    return []  # Empty list indicates no valid pairs found

# Test the function with a sample input
numbers = [2, 7, 11, 15]  # List of integers to search in
target = 9  # Integer target value to find
result = find_two_sum(numbers, target)  # Call the function with the input list and target
print(result)  # Print the result to check if the function works correctly
