from random import randint
import os
import time

def start():
    os.system('cls')  # Очистка консоли
    print(f'Привет! Это игра "Угадай число"\nПравила очень простые:\nУгадать число от 1 до 100 за 7 попыток, после каждой попытки я буду говорить больше или меньше загаданное число.\nПочему так много? Потому что 7 - счастливое число ;)\nНачинаем...')
    game()

def game():
    global attempt, num, gnum
    num = randint(1, 100)
    attempt = 1
    while attempt <= 7:
        gnum = int(input(f'Итак, {attempt} попытка. Какое же число я загадал?\n'))
        if gnum == num:
            break
        elif gnum > num:
            attempt += 1
            print(f'{gnum} - больше моего числа. Попробуй ещё :)\n')
        elif gnum < num:
            attempt += 1
            print(f'{gnum} - меньше моего числа. Попробуй ещё :)\n')
    end()

def end():
    if gnum == num:
        print(f'Поздравляю! Моё число - {num}, ты угадал!')
    else:
        print(f'Ты проиграл! Моё число - {num}, не повезло :(')
    retry = int(input(f'Хочешь начать заново?\n1. Да\n2. Нет\n'))
    if retry == 1:
        game()
    else:
        print(f"Надеюсь ещё увидимся, удачи :')")
        time.sleep(5)

start()