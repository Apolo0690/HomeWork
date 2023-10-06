'''Task_1'''
'''Напишіть функцію, що приймає один аргумент будь-якого типу 
та повертає цей аргумент, перетворений на float. Якщо перетворити 
не вдається функція має повернути 0.'''


enter = input()
def datatype(enter):
    try:
        enter == int or float
        zamena = float(enter)
        return zamena
    except:
        return 0

datatype(enter)
print(datatype(enter))

