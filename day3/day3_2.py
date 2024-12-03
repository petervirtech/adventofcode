import re
from icecream import ic

# Read the content of the file with the messed-up data
with open('day3/data.txt', 'r') as file:
    data = file.read()

# Regular expression pattern to match the required mul(xxx,xxx) format
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

# Find all occurrences of the pattern in the data
matches = re.finditer(pattern, data)

# Initialize the sum of all multiplication results
total_sum = 0

# Track whether we are in an include or exclude state
include_state = True

# Process each match in the order they appear
for match in matches:
    # Check the part of data before the current match to see if there's a don't() or do() statement
    preceding_text = data[:match.start()]
    dont_statements = preceding_text.rfind("don't()")
    do_statements = preceding_text.rfind("do()")

    # Update the include_state based on the last don't() or do() statement
    if dont_statements > do_statements:
        include_state = False
    elif do_statements > dont_statements:
        include_state = True

    # Only process the match if we are in an include state
    if include_state:
        # Extract the numbers from the match
        num1, num2 = map(int, match.groups())
        # Calculate the product
        result = num1 * num2
        # Log the function and result using IceCream
        ic(f'mul({num1},{num2}) = {result}')
        # Add the result to the total sum
        total_sum += result

# Print the total sum of all multiplication results
ic(f'Total sum of all mul() results: {total_sum}')
