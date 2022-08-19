def arithmetic_arranger(problems, answers=False):

    # Error Checks!
    if len(problems) > 5:
        return "Error: Too many problems."

    # Error Check 2!
    for problem in problems:
        if "*" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."

    # Error Check 3!
    for problem in problems:
        operand_list = problem.split()
        operand1 = operand_list[0]
        operand2 = operand_list[2]
        if operand1.isnumeric() == False or operand2.isnumeric() == False:
            return 'Error: Numbers must only contain digits.'

    # Error Check 4!
    for problem in problems:
        operand_list = problem.split()
        operand1 = operand_list[0]
        operand2 = operand_list[2]
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # Code
    final_re = ''
    arranged_problems = []
    for i in range(0, 3):
        arranged_problems.append("")
    prob_list = []
    for problem in problems:
        operand_list = problem.split()
        operand1 = operand_list[0]
        operand2 = operand_list[2]
        prob_list.append(operand_list)

    # line 1
    for i in range(0, len(prob_list)):
        x = prob_list[i][0]
        y = prob_list[i][2]
        op = prob_list[i][1]
        if len(x) > len(y):
            arranged_problems[0] = arranged_problems[0] + \
                f"{' '*2 + x + ' '*4}"
        elif len(x) < len(y):
            arranged_problems[0] = arranged_problems[0] + \
                f"{' '*2 + ' '*(len(y)-len(x)) + x + ' '*4}"
        else:
            arranged_problems[0] = arranged_problems[0] + \
                f"{' '*2 + x + ' '*4}"
    arranged_problems[0] = arranged_problems[0].rstrip() + "\n"

    # line 2
    for i in range(0, len(prob_list)):
        x = prob_list[i][0]
        y = prob_list[i][2]
        op = prob_list[i][1]
        if len(x) > len(y):
            arranged_problems[1] = arranged_problems[1] + \
                f"{op + ' ' + ' '*(len(x)-len(y)) + y + ' '*4}"
        elif len(x) < len(y):
            arranged_problems[1] = arranged_problems[1] + \
                f"{op + ' ' + y + ' '*4}"
        else:
            arranged_problems[1] = arranged_problems[1] + \
                f"{op + ' ' + y + ' '*4}"

    arranged_problems[1] = arranged_problems[1].rstrip() + "\n"

    # line 3
    for i in range(0, len(prob_list)):
        x = prob_list[i][0]
        y = prob_list[i][2]
        op = prob_list[i][1]
        arranged_problems[2] = arranged_problems[2] + \
            f"{'-'*(2+max(len(x), len(y))) + ' '*4}"

    # line 4
    if answers == True:
        arranged_problems[2] = arranged_problems[2].rstrip() + "\n"
        arranged_problems.append("")
        for i in range(0, len(prob_list)):
            x = int(prob_list[i][0])
            y = int(prob_list[i][2])
            op = prob_list[i][1]
            if '+' in op:
                result = str(x + y)
            elif '-' in op:
                result = str(x - y)

            if int(result) >= 0:
                if len(result) > len(str(max(x, y))):
                    arranged_problems[3] = arranged_problems[3] + \
                        f"{' ' + result + ' '*4}"
                elif len(result) < len(str(max(x, y))):
                    arranged_problems[3] = arranged_problems[3] + \
                        f"{' '*(2 + (len(str(max(x, y))) - len(result))) + result + ' '*4}"
                elif len(result) == len(str(max(x, y))):
                    arranged_problems[3] = arranged_problems[3] + \
                        f"{' '*2 + result + ' '*4}"
            else:
                if len(result) > len(str(max(x, y))):
                    arranged_problems[3] = arranged_problems[3] + \
                        f"{' ' + result + ' '*4}"
                elif len(result) < len(str(max(x, y))):
                    arranged_problems[3] = arranged_problems[3] + \
                        f"{' '*(2 + len(result) - len(str(max(x, y)))) + ' '*4}"
                elif len(result) == len(str(max(x, y))):
                    arranged_problems[3] = arranged_problems[3] + \
                        f"{' '*2 + result + ' '*4}"
        arranged_problems[3] = arranged_problems[3].rstrip() + "\n"
        for i in range(0, 4):
            final_re = final_re + arranged_problems[i]
        final_re = final_re.rstrip()
    else:
        arranged_problems[2] = arranged_problems[2].rstrip()
        for i in range(0, 3):
            final_re = final_re + arranged_problems[i]
        final_re = final_re.rstrip()

    return final_re
