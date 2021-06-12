import re

def get_suffix(index, number_of_problems):
    if index == number_of_problems - 1:
        return '\n'
    else:
        return '    '

def arithmetic_arranger(problems, show_answers = False):
    number_of_problems = len(problems)
    if number_of_problems > 5:
        return('Error: Too many problems.')
    key = 'abcdefghij'[:number_of_problems * 2]
    arranged_problems = key[:]

    lines = ''
    answers = ''
    for index, problem in enumerate(problems):
        first = re.findall('^([0-9]*)', problem)[0]
        try:
            second = re.findall('[-+]', problem)[0]
        except:
            return("Error: Operator must be '+' or '-'.")
        if len(re.findall('[^0-9-+\s]', problem)):
            return('Error: Numbers must only contain digits.')
        third = re.findall('([0-9]*)$', problem)[0]
        len_first = len(first)
        len_third = len(third)
        if len_first > 4 or len_third > 4:
            return 'Error: Numbers cannot be more than four digits.'
        width = max((len_first, len_third)) + 2
        sub_string = ' ' * (width - len_first) + first + get_suffix(index, number_of_problems)
        arranged_problems = re.sub(f'[{key[index]}]', sub_string, arranged_problems)
        sub_string = second + ' ' * (width - len_third - 1) + third + get_suffix(index, number_of_problems)
        arranged_problems = re.sub(f'[{key[index + number_of_problems]}]', sub_string, arranged_problems)
        lines += '-' * width
        if index < number_of_problems - 1:
            lines += '    '
        else:
            if show_answers:
                lines += '\n'
        if show_answers:
            if second == '+':
                answer = str(int(first) + int(third))
            else:
                answer = str(int(first) - int(third))
            answers += ' ' * (width - len(answer)) + answer
        if index < number_of_problems - 1:
            answers += '    '

    arranged_problems += lines
    if show_answers:
        arranged_problems += answers

    return (arranged_problems)
