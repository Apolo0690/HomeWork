'''Task_1 and task_2'''
'''Створіть файл lib.py, помістіть в нього допоміжні функції вашої програми "Касир". 
Імпортуйте їх для основної функції в основний файл. Запустіть "Касир" з основного файлу
Помістіть в lib.py декоратор для вимірювання часу. Імпортуйте декоратор в основний файл, 
задекоруйте основну функцію "Касир".'''



from lib import time_counter
from lib import get_age
from lib import word_ending
from lib import age_group


@time_counter
def imax():
    print('\t\t\t\t\t\tКАСА IMAX')
    print('Касир:\n-Вітаємо! Ця кінолента має обмеження за віком. Скільки Вам років?')

    age = get_age('Введіть свій вік: ')

    end = word_ending(age)

    res_mes = age_group(age, end)
    print(res_mes)

imax()