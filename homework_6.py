'''Task_1'''
'''Напишіть функцію, що приймає один аргумент будь-якого типу 
та повертає цей аргумент, перетворений на float. Якщо перетворити 
не вдається функція має повернути 0.'''


enter = input("Enter the info: ")
def datatype(enter):
    try:
        enter == int or float
        zamena = float(enter)
        return zamena
    except:
        return 0

datatype(enter)
print(datatype(enter))



'''Task_2'''
'''Напишіть функцію, що приймає два аргументи. Функція повинна
якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
у будь-якому іншому випадку повернути кортеж з цих аргументів'''



def datatype(info_1, info_2):
    info_1 = 'ergver'
    info_2 = 2
    if isinstance(info_1, (int, float)) and isinstance(info_2, (int, float)):
        res = info_1 * info_2
    elif isinstance(info_1, str) and isinstance(info_2, str):
        res = f"{info_1} {info_2}"
    else:
        res = [info_1, info_2]
    return res
print(datatype(1, 2))

datatype(1, 2)



'''Task_3'''
'''Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. 
Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 
35 - років і тд...). 
Наприклад :
"Тобі ж 5 років! Де твої батьки?"
"Вам 81 рік? Покажіть пенсійне посвідчення!"
"Незважаючи на те, що вам 42 роки, білетів всеодно нема!"'''



print('\t\t\t\t\t\tКАСА IMAX')
print('Касир:\n-Вітаємо! Ця кінолента має обмеження за віком. Скільки Вам років?')

visitor = int(input("Введіть свій вік: "))

kid = visitor >= 0 and visitor < 6
teenager = visitor < 16 and visitor >= 6
old_person = visitor > 65 and visitor <= 100
norm = visitor <= 65 and visitor >= 16
lucky = '7' in str(visitor)


def word_ending(rik, roku, rokiv):
    try:
        remainder = visitor % 10
        rik = "рік"
        roku = "роки"
        rokiv = "років"

        if visitor >= 5 and visitor <= 20 or visitor == 0 or remainder >= 5 and remainder <= 9 or remainder == 0:
            res = rokiv
        elif visitor >= 2 and visitor <= 4 or remainder >= 2 and remainder <= 4:
            res = roku
        elif visitor == 1 or remainder == 1 and visitor != 11:
            res = rik

        return res

    except:
        print("Невірній формат!")
        word_ending(1, 2, 3)

end = word_ending(1, 2, 3)

if lucky:
    print(f"Касир:\n-Вам {visitor} {end}? Вам пощастить!")
elif kid:
    print(f"Касир:\n-Тобі ж {visitor} {end}! Де товї батьки?")
elif teenager:
    print(f"Касир:\n-Вибачте, Вам {visitor} {end}, а цей фільм для дорослих.")
elif old_person:
    print(f"Касир:\n-Вам {visitor} {end}? У нас є акційна пропозиція для пенсіонерів.\nПокажіть Ваше пенсійне посвідчення, будь-ласка.")
elif norm:
    print(f"Касир:\n-Не зважаючи на те що Вам {visitor} {end}, нажаль, білетів вже нема!")
else:
    print(f"Касир:\n-Цей вік не є можливим.")







