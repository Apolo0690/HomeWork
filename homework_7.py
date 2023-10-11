'''Task_1'''
'''Доопрацюйте гру з занятя наступним чином:

додайте підказки для користувача. 
-якщо різниця між числами 1-2 - "Гаряче"
-якщо різниця між числами 3-5 - "Тепло"
-якщо різниця між числами 6 і більше- "Холодно"

додайте лічильник спроб вгадати. користувач повинен 
вгадати число за фіксовану кількість спроб (визначіть 
кількість спроб самостійно). якщо він не вгадав за 
фіксовану кількість спроб - гра завершується з 
відповідним повідомленням'''



# guess the number

from random import randint


def get_user_number(prompt='Enter number', lower_limit=None, upper_limit=None):
    while True:
        try:
            res = int(input(f'{prompt} (int number): '))
        except Exception:
            print('Wrong input!')
        else:
            if lower_limit is not None:
                if res < lower_limit:
                    print(f'Number should be bigger than {lower_limit}!')
                    continue
            if upper_limit is not None:
                if res > upper_limit:
                    print(f'Number should be less than {upper_limit}!')
                    continue
            return res



def get_comp_number(lower_limit, upper_limit):
    res = randint(lower_limit, upper_limit)
    # print(f'Hint: {res}')
    return res



def compare_numbers(comp_number, user_number):
    difference = abs(comp_number - user_number)

    if comp_number == user_number:
        return True
    elif difference < 3:
        print("Hot.")
    elif difference < 6:
        print("Heat.")
    elif difference >= 6:
        print("Cold.")



def game_guess_number():
    lower_limit = 0
    upper_limit = 9

    comp_number = get_comp_number(lower_limit, upper_limit)
    print(comp_number)
    attempt = 0
    max_attempt = 5
    balance = max_attempt - attempt
    while True:

        user_number = get_user_number(f'Guess the number [{lower_limit}-{upper_limit}]', lower_limit, upper_limit)

        if attempt == 4:
            print("Game over!")
            break
        elif user_number != comp_number:
            compare_numbers(comp_number, user_number)
            attempt += 1
            balance -= 1
            print(f'Try again! You have {balance} chances')
        else:
            print('Congratulations!')
            break


game_guess_number()