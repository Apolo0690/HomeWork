raw_str = input()

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
