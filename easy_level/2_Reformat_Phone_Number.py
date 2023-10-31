'''
number => str with ' ' and '-'

Input: number = "1-23-45 6" :6
Output: "123-456"

Input: number = "123 4-567" :7
Output: "123-45-67"
'''


def create_proper_number(number: str):
    number = str(number)
    number = number.replace(' ', '').replace('-', '')
    len_number = len(number)
    result = ''
    while len_number > 0:
        if len_number == 2:
            len_number -= 2
            result += number[:2]
            continue
        elif len_number == 3:
            len_number -= 3
            result += number[:3]
            continue
        elif len_number == 4:
            len_number -= 4
            result += number[:2] + '-' + number[2:]
            continue
        elif len_number == 5:
            len_number -= 5
            result += number[:3] + '-' + number[3:]
            continue
        else:
            len_number -= 3
            result += number[:3] + '-'
            number = number[3:]
            continue
    return result


print(create_proper_number('123 4-5678'))









