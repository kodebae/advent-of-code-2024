from collections import Counter
# What is the total distance between your lists?

# Step 1: 1 rite a script to parse the list and write it to a file.
# Read from a file
# Read from a file
with open("input.txt", "r") as file:
    left_list = []
    right_list = []
    for line in file:
        line = line.strip()  # Remove extra whitespace
        if not line:  # Skip empty lines
            print("Skipping empty line.")
            continue
        try:
            # Split by space and convert to integers
            left, right = map(int, line.split())
            print(f"Split results: Left = {left}, Right = {right}")  # Debugging
            left_list.append(left)
            right_list.append(right)
        except ValueError as e:
            print(f"Skipping line due to error: {line} - {e}")

print("Final Left List:", left_list)
print("Final Right List:", right_list)

# Step 2: Sorting. We're sorting a list and checking it twice...
left_list.sort()  # Sorts the list in-place
right_list.sort()  # Sorts the list in-place

print("Sorted Left List:", left_list)
print("Sorted Right List:", right_list)


# Step 3: Pair and calculate the values with zip
# left_list and right_list are sorted
# Initialize the var to store total distance
total_distance = 0

# Iterate through both lists simultaneously using zip
for left, right in zip(left_list, right_list):
    # Calculate the absolute difference and add it to the total distance
    total_distance += abs(left - right)

# Print the total distance
print("Total Distance:", total_distance)

# *********** spoiler ***********
# Total Distance is: 1879048 