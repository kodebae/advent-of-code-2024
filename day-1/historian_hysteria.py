# What is the total distance between your lists?

# step 1, write a script to parse the list and write it to a file.
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
