from random import randint

"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
"""

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
hidden_number = randint(LOWER_LIMIT, UPPER_LIMIT)
attempt = 10
attempt = abs(attempt)

print(f'Я загадал число от {LOWER_LIMIT} до {UPPER_LIMIT}. Угадайте его за {attempt} попыток')

while attempt != 0:
    num = int(input(f'Введите число: '))
    if num < 0 or num > 1000:
        print(f'Вы ввели число вне диапазона от {LOWER_LIMIT} до {UPPER_LIMIT}')
    elif num < hidden_number:
        print('больше')
    elif num > hidden_number:
        print('меньше')
    else:
        print('Вы угадали! ヽ(°◡° )ノ')
        break
    attempt -= 1
if attempt == 0:
    print('Попытки закончились')
