#!/usr/bin/env python3
import random

def new_attempt():
    number = random.randint(1, 10) # случайное число от 1 до 10 включительно
    return number


def get_user_number():
    guess = input("Введите число от 1 до 10:\n")
    try:
        # разрешим принимать float на всякий случай
        return int(float(guess)) 
    except:
        print("Вы ввели не число, а что-то другое. Нужно ввести целое число. Попробуйте снова.")
        print('---------------------------------------------------------------------------------')
        # рекурсия пока не получим число
        return get_user_number()


def main():
    print('---------------------------------------------------------------------------------')
    print('Добро пожаловать в игру "Угадай число"!')
    print('---------------------------------------------------------------------------------')
    print('Правила:')
    print('1. Загадывается число от 1 до 10.')
    print('2. У вас одна попытка.')
    print('3. В случае неудачи число будет загадано снова.')
    print('4. Если угадаете — вас ждёт приз. Удачи!')
    print('---------------------------------------------------------------------------------')

    attempts = 0 # счётчик попыток

    while True:
        number = new_attempt()
        guess = get_user_number()
        attempts += 1
        if guess == number:
            break
        else:
            print('Вы проиграли. Загаданное число — {}. Попыток угадать — {}. Пробуйте еще!'.format(number, attempts))
            print('---------------------------------------------------------------------------------')
            continue

    print('---------------------------------------------------------------------------------')
    
    if attempts == 1:
        print('Поздравляю, вы угадали число {} с первой попытки. Невероятное везение!'.format(number))
    elif attempts % 10 == 1:
        print('Поздравляю, вы угадали число {} и потратили на это {} попытку!'.format(number, attempts))
    elif attempts % 20 == 2 or attempts % 20 == 3 or attempts % 20 == 4:
        print('Поздравляю, вы угадали число {} и потратили на это {} попытки!'.format(number, attempts))
    else:
        print('Поздравляю, вы угадали число {} и потратили на это {} попыток!'.format(number, attempts))
    print('Ваш приз:')
    print('https://terentev.online/gift.html')
    print('---------------------------------------------------------------------------------')


if __name__ == '__main__':
    main()
