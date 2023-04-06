def arithmetic_arranger(problems):
    digits = 0
    arranged_problems = ''
    first_line = ''
    second_line = ''
    for item in problems:
        first_space = item.find(' ')
        first_line += ' '*(5 - first_space) + item[:first_space + 1]
        for x in item:
            digits += 1
        second_line += item[first_space + 1] + ' '*(5 - (digits - (first_space+2))) + item[first_space + 3:] + ' '
        digits = 0
    arranged_problems = first_line + '\n' + second_line + '\n' + '----- ----- ----- -----'
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["3 + 1423", "2 - 1", "45 + 4374", "123 - 1234"]))