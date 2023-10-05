'''Task_1'''
'''Дана довільна строка. Напишіть код, який знайде 
в ній і віведе на екран кількість слів, які містять 
дві голосні літери підряд.'''

# Actually we cannot count our mother's daily activities.

text = input("Type the text: ")
separate = text.split(' ')

vowels = set("aeyoiu")
consonants = set("qwrtpsdfghjklzxcvbnm")

two_vowel_word = []

for word in separate:
    pass
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
        elif letter in consonants:
            count = 0
        if count == 2:
            two_vowel_word.append(word)
            break
if len(two_vowel_word) >= 2 or len(two_vowel_word) == 0:
    plural = "'s "
else:
    plural = " "
print(two_vowel_word, "\n",len(two_vowel_word), f"word{plural}that have two vowel letters in a row.")







'''Task_2'''
'''Є два довільних числа які відповідають за мінімальну і 
максимальну ціну. Є Dict з назвами магазинів і цінами: 
{ "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, 
"main-service": 37.245, "buy.now": 38.324, "x-store": 
37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 
38.003}. Напишіть код, який знайде і виведе на екран назви 
магазинів, ціни яких попадають в діапазон між мінімальною і 
максимальною ціною.'''


# store = { "cito" : 47.999, "BB_studio" : 42.999, "momo" : 49.999,
#           "main-service" : 37.245, "buy.now" : 38.324, "x-store" : 37.166,
#           "the_partner" : 38.988, "store" : 37.720, "rozetka" : 38.003}
#
# store_1 = float(input("Type the store min: "))
# store_2 = float(input("Type the store max: "))
#
# for key, value in store.items():
#     if value >= store_1 and value <= store_2:
#         print(key)