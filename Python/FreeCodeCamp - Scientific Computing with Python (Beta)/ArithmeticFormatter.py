def arithmetic_arranger(problems, show_answers=False):
    first_numbers = []
    second_numbers = []
    operators = []
    solutions = []
    dash_gaps = []
    vertical_gap = 4
    final_string = ""

    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Separate the numbers and operators
    for problem in problems:
        if '+' in problem or '-' in problem:
            splitted_numbers = problem.split(' ')
            first_num = splitted_numbers[0]
            operator = splitted_numbers[1]
            second_num = splitted_numbers[2]
            
            # Check if the numbers contain only digits
            if not first_num.isdigit() or not second_num.isdigit():
                return "Error: Numbers must only contain digits."
            
            # Check if the numbers are more than 4 digits
            if len(first_num) > 4 or len(second_num) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            # Append the numbers and operators
            first_numbers.append(first_num)
            operators.append(operator)
            second_numbers.append(second_num)
        else:
            return "Error: Operator must be '+' or '-'."

    # Calculate the solutions if show_answers is True
    if show_answers:
        for i in range(len(operators)):
            if operators[i] == '+':
                solutions.append(int(first_numbers[i]) + int(second_numbers[i]))
            elif operators[i] == '-':
                solutions.append(int(first_numbers[i]) - int(second_numbers[i]))

    # Determine the length for dashes and proper formatting
    for i in range(len(operators)):
        dash_gap = max(len(first_numbers[i]), len(second_numbers[i])) + 2  # +2 for operator and space
        dash_gaps.append(dash_gap)

    # Prepare the first line (first numbers)
    for i in range(len(operators)):
        difference = dash_gaps[i] - len(first_numbers[i])
        final_string += " " * difference + first_numbers[i] + " " * vertical_gap
    final_string += "\n"

    # Prepare the second line (operators and second numbers)
    for i in range(len(operators)):
        blank_space = dash_gaps[i] - len(second_numbers[i]) - 1  # -1 for the operator
        final_string += operators[i] + " " * blank_space + second_numbers[i] + " " * vertical_gap
    final_string += "\n"

    # Prepare the third line (dashes)
    for i in range(len(operators)):
        final_string += "-" * dash_gaps[i] + " " * vertical_gap
    final_string += "\n"

    # Optionally, prepare the fourth line (solutions)
    if show_answers:
        for i in range(len(operators)):
            solution_space = dash_gaps[i] - len(str(solutions[i]))
            final_string += " " * solution_space + str(solutions[i]) + " " * vertical_gap

    return final_string

# Test the function
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')

print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
