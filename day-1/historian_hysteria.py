from collections import Counter

# Function to parse the input file
def parse_file(filename):
    left_list = []
    right_list = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            try:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
            except ValueError:
                print(f"Skipping line: {line}")
    return left_list, right_list

# Function to calculate total distance (Part 1)
# Iterate through both lists simultaneously using zip
def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return sum(abs(left - right) for left, right in zip(left_list, right_list))

# Function to calculate similarity score (Part 2)
def calculate_similarity_score(left_list, right_list):
    right_counts = Counter(right_list)
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_counts.get(number, 0)
    return similarity_score

# Main execution
if __name__ == "__main__":
    # Step 1: Parse input
    left_list, right_list = parse_file("input.txt")

    # Step 2: Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print("Total Distance:", total_distance)
# *********** spoiler ***********
# Total Distance is: 1879048 so far...

    # Step 3: Calculate similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity Score:", similarity_score)
# *********** spoiler ***********   
# The similarity score is 21024792
