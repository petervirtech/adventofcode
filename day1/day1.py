import re
from icecream import ic
from collections import Counter

def calculate_total_difference(column1, column2):
    # Sort both columns individually
    column1.sort()
    column2.sort()

    # Calculate the differences and the total difference
    total_difference = 0
    for num1, num2 in zip(column1, column2):
        # Calculate the difference
        difference = abs(num1 - num2)
        # Log the difference using IceCream
        ic(f'Difference between {num1} and {num2} = {difference}')
        # Add the difference to the total
        total_difference += difference

    # Print the total difference
    ic(f'Total difference of all rows: {total_difference}')

def calculate_similarity_score(column1, column2):
    # Count occurrences of each number in column2
    count_column2 = Counter(column2)

    # Calculate the total similarity score
    total_similarity_score = 0
    for num1 in column1:
        count_in_column2 = count_column2.get(num1, 0)
        similarity_score = num1 * count_in_column2
        ic(f'Number {num1} appears {count_in_column2} times in column2, contributing {similarity_score} to the similarity score')
        total_similarity_score += similarity_score

    # Print the total similarity score
    ic(f'Total similarity score: {total_similarity_score}')

def main():
    # Read the content of the file with the dataset
    column1 = []
    column2 = []
    with open('day1/data.txt', 'r') as file:
        for line in file:
            # Extract the two numbers from each row
            num1, num2 = map(int, line.split())
            # Add numbers to their respective columns
            column1.append(num1)
            column2.append(num2)

    # Perform calculations
    calculate_total_difference(column1, column2)
    calculate_similarity_score(column1, column2)

if __name__ == "__main__":
    main()