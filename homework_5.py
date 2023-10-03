'''Task_1'''
'''Виконайте задачу №3 з заняття.

AI. Порграма має відповісти на питання чи є введений стрінг
1 - номером телефону
2 - email-ом
3 - Іменем з ініціалами
4 - Даними невідомого формату

+380631112233 -> Phone
bcdef@abc.efg -> email   3+ letters @ 3 letters. 3 letters
Bill J.I. -> name   2 words
something else -> unknown'''


raw_str = input("Enter information: ")

if "+" in raw_str:

    phone_conditions = (
        len(raw_str) == 13,
        raw_str[0] == '+',
        raw_str[1:].isdigit(),
        raw_str[3:6] in ('063', '067', '050'),
    )

    if all(phone_conditions):
        print('Phone number')
    else:
        print("Unknown")

elif not "+" in raw_str:
    if "@" in raw_str:

        import re

        separation = re.split("[@, .]", raw_str)

        email_condition = (
            len(separation[0]) >= 3,
            len(separation[1]) == 3,
            len(separation[2]) == 3
        )
        if all(email_condition):
            print('email')
        else:
            print("Unknown")

    elif not "@" in raw_str:
        print("Unknown")
