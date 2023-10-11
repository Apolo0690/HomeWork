'''Task_1'''
'''Наришіть декоратор, який вимірює час виконання функції.'''


def time_counter(func):
    import time

    def wrapper():
        start_time = time.time()
        func()
        print("Час виконання програми з урахуванням користувацького введення = ", time.time() - start_time)
    return wrapper



'''Task_2'''
'''Задекоруйте цим декоратором вашу програму "Касир"'''


@time_counter
def imax():
    print('\t\t\t\t\t\tКАСА IMAX')
    print('Касир:\n-Вітаємо! Ця кінолента має обмеження за віком. Скільки Вам років?')

    def get_age(visitor_age):
        while True:
            try:
                visitor = int(input(f'{visitor_age}'))
                return visitor
            except Exception:
                print('Це не вік! Спробуйте ще раз.')

    age = get_age('Введіть свій вік: ')



    kid = age >= 0 and age < 6
    teenager = age < 16 and age >= 6
    old_person = age > 65 and age <= 100
    norm = age <= 65 and age >= 16
    lucky = '7' in str(age)




    def word_ending():
        if age >= 5 and age <= 20 or age == 0 or age % 10 >= 5 and age % 10 <= 9 or age % 10 == 0:
            ending = "років"
        elif age >= 2 and age <= 4 or age % 10 >= 2 and age % 10 <= 4:
            ending = "роки"
        elif age == 1 or age % 10 == 1 and age != 11:
            ending = "рік"
        return ending

    end = word_ending()


    def response_message():
        if lucky:
            res = f"Касир:\n-Вам {age} {end}? Вам пощастить!"
        elif kid:
            res = f"Касир:\n-Тобі ж {age} {end}! Де товї батьки?"
        elif teenager:
            res = f"Касир:\n-Вибачте, Вам {age} {end}, а цей фільм для дорослих."
        elif old_person:
            res = f"Касир:\n-Вам {age} {end}? У нас є акційна пропозиція для пенсіонерів.\nПокажіть Ваше пенсійне посвідчення, будь-ласка."
        elif norm:
            res = f"Касир:\n-Не зважаючи на те що Вам {age} {end}, нажаль, білетів вже нема!"
        else:
            res = f"Касир:\n-Цей вік не є можливим."
        return res

    res_mes = response_message()
    print(res_mes)

imax()