def arithmetic_arranger(problems, show_answers=False):

    return problems

# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

first_numbers = []
second_numbers = []
operators = []
solutions = []
dash_gaps = []
vertical_gap = 4
final_string = ""
    
for problem in problems:
    if problem.find('+') is not None:
        splitted_numbers = problem.split(' ')
        first_numbers.append(splitted_numbers[0])
        operators.append(splitted_numbers[1])
        second_numbers.append(splitted_numbers[2])
        
    elif problem.find('-') is not None:
        splitted_numbers = problem.split(' ')
        first_numbers.append(splitted_numbers[0])
        operators.append(splitted_numbers[1])
        second_numbers.append(splitted_numbers[2])
        
for i in range(len(operators)):
    if operators[i] == '+':
        solutions.append(int(first_numbers[i]) + int(second_numbers[i]))
    elif operators[i] == '-':
        solutions.append(int(first_numbers[i]) - int(second_numbers[i]))

for i in range(len(operators)):
    dash_gap = len(str(max(first_numbers[i], second_numbers[i]))) + 1 # -----
    dash_gaps.append(dash_gap)
    white_space = dash_gap - len(str(first_numbers[i])) # white-space
    final_string += " " * white_space + first_numbers[i] + " " * (vertical_gap + 1)
final_string += "\n"    

for i in range (len(operators)):
    white_space = dash_gaps[i] - len(str(second_numbers[i]))
    if operators[i] == '+':
        final_string += "+" + " " * white_space + second_numbers[i] + " " * vertical_gap
    elif operators[i] == '-':
        final_string += "-" + " " * white_space + second_numbers[i] + " " * vertical_gap
final_string += "\n"

for i in range(len(operators)):
    final_string += "-" * (dash_gaps[i] + 1) + " " * vertical_gap
final_string += "\n"

for i in range(len(operators)):
    solution_space = dash_gaps[i] - len(str(solutions[i])) + 1  # Align solutions under the dashes
    final_string += " " * solution_space + str(solutions[i]) + " " * vertical_gap
final_string += "\n"

print("First Numbers: ", first_numbers)
print("Second Numbers: ", second_numbers)
print("Operators: ", operators)
print("Solutions: ", solutions)
print("Dash Gaps: ", dash_gaps)
print("Final String:\n", final_string)