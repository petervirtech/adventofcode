import re
from icecream import ic

# Read the content of the file with the messed-up data
with open('day3/data.txt', 'r') as file:
    data = file.read()

# Regular expression pattern to match the required mul(xxx,xxx) format
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

# Find all occurrences of the pattern in the data
matches = re.findall(pattern, data)

# Initialize the sum of all multiplication results
total_sum = 0

# Process each valid match
for match in matches:
    # Extract the numbers from the match
    num1, num2 = map(int, match)
    # Calculate the product
    result = num1 * num2
    # Log the function and result using IceCream
    ic(f'mul({num1},{num2}) = {result}')
    # Add the result to the total sum
    total_sum += result

# Print the total sum of all multiplication results
ic(f'Total sum of all mul() results: {total_sum}')
