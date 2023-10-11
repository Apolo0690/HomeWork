def time_counter(func):
    import time

    def wrapper():
        start_time = time.time()
        func()
        print("Час виконання програми з урахуванням користувацького введення = ", time.time() - start_time)
        return func
    return wrapper


def get_age(visitor_age):
    while True:
        try:
            visitor = int(input(f'{visitor_age}'))
            return visitor
        except Exception:
            print('Це не вік! Спробуйте ще раз.')




def word_ending(age):
    if age >= 5 and age <= 20 or age == 0 or age % 10 >= 5 and age % 10 <= 9 or age % 10 == 0:
        ending = "років"
    elif age >= 2 and age <= 4 or age % 10 >= 2 and age % 10 <= 4:
        ending = "роки"
    elif age == 1 or age % 10 == 1 and age != 11:
        ending = "рік"
    return ending




def age_group(age, end):
    kid = f"Касир:\n-Тобі ж {age} {end}! Де товї батьки?"
    teenager = f"Касир:\n-Вибачте, Вам {age} {end}, а цей фільм для дорослих."
    old_person = f"Касир:\n-Вам {age} {end}? У нас є акційна пропозиція для пенсіонерів.\nПокажіть Ваше пенсійне посвідчення, будь-ласка."
    norm = f"Касир:\n-Не зважаючи на те що Вам {age} {end}, нажаль, білетів вже нема!"
    lucky = f"Касир:\n-Вам {age} {end}? Вам пощастить!"
    if '7' in str(age) and age <= 100 and age >= 0:
        res_age = lucky
    elif age >= 0 and age < 6:
        res_age = kid
    elif age < 16 and age >= 6:
        res_age = teenager
    elif age > 65 and age <= 100:
        res_age = old_person
    elif age <= 65 and age >= 16:
        res_age = norm
    else:
        res_age = f"Касир:\n-Цей вік не є можливим."
    return res_age
