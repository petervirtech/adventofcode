def is_increasing_or_decreasing(levels):
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    return increasing or decreasing

def is_difference_valid(levels):
    return all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

def can_be_valid_by_removing_one(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_increasing_or_decreasing(modified_levels) and is_difference_valid(modified_levels):
            return True
    return False

def validate_reports(filename):
    valid_reports_count = 0

    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_increasing_or_decreasing(levels) and is_difference_valid(levels):
                valid_reports_count += 1
            elif can_be_valid_by_removing_one(levels):
                valid_reports_count += 1

    return valid_reports_count

if __name__ == "__main__":
    filename = "day2/data.txt"
    valid_reports = validate_reports(filename)
    print(f"Number of valid reports: {valid_reports}")