def is_safe_report(report):
    levels = list(map(int, report.split()))

    # Check if the sequence is valid as-is
    if is_valid_sequence(levels):
        return True

    # Check if removing one level makes it valid
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_valid_sequence(modified_levels):
            return True

    return False

def is_valid_sequence(levels):
    # Check if levels are increasing or decreasing with valid differences
    is_increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
    is_decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
    return is_increasing or is_decreasing

def count_safe_reports(filename):
    # Read data from the input file
    with open(filename, 'r') as file:
        reports = file.readlines()
    # Count safe reports
    return sum(1 for report in reports if is_safe_report(report.strip()))

# File to read input from
input_file = "input.txt"

# Calculate and print the number of safe reports
print(count_safe_reports(input_file))
