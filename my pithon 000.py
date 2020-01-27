#управление кол-вом знаков после запятой в вещественных числах
total = 42
print("%.2f" % total)
print('\n', sep='')

#управление выводом префиксов и значений
name = 'John'
quest = '\"the Secret Treasure\"'
color = 'magenta'
print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
print('\n', sep='')


''' 
print('%s/%s/%s %s:%s:%s' % \
(time.now.month, now.day, now.year, \
now.hour, now.minute, now.second))
print('\n', sep='')
'''

#удаление из списков
n = [1, 3, 5, 7, 9]
n.pop(0) # Удаляет (1) элемент списка с заданным индексом
n.remove(9) # Удаляет (9) элемент списка совпадающий с заданным значением
del(n[0]) # Удаляет (3) элемент списка с заданным индексом, но не физически, а только из выдачи
print(n) # >>> [5, 7]
print('\n', sep='')

# Гибкость в передаче параметров в функциях
m = 5
n = 13
def add_function(x, y): # Свои переменные x и y.
    return x + y
print(add_function(m, n)) # m и n подставляются в функцию в качестве x и y.
print('\n', sep='')

# Еще пример
def string_function(s):
    return s + "world!"
n = "Hello, "
print(string_function(n)) # n поступает в функцию на место s.
print('\n', sep='')

def list_function(x):	# Пример ...
    return x		# ... с передачей ...
n = [3, 5, 7]
print(list_function(n))	# ... списка.
print('\n', sep='')

# Функция добавляет элемент "9" в конец списка
def list_extender(lst):
    lst.append(9)
    return lst
n = [3, 5, 7]
print(list_extender(n)) # Напечатает: [3, 5, 7, 9]
print('\n', sep='')

# return в функции может отсутствовать (когда возвращает не одно значение?)
n = [3, 5, 7]
def print_list(x):
    for i in range(len(x)):
        print(x[i])
print(print_list(n))
print('\n', sep='')

# Умножение каждого члена списка любой длины (с помощью range и len) на число 2.
def double_list(x):
    for i in range(0, len(x)): # range(start, stop, step) . Здесь старт - 0-индекс списка (если пропущен, то по умолчанию - 0), стоп - последний индекс списка (определяется встроенной функцией len). Шаг не указан, по умолчанию равен 1.
        x[i] = x[i] * 2 # можно так: x[i] *= 2
    return x
print(double_list(n)) 
print('\n', sep='')

'''
# range с помощью ф-ции создает список. Пока не совсем понятно зачем нужна такая конструкция.
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
print(my_function(range(3))) # Напечатает: [0, 2, 4]
print('\n', sep='')
'''

# Сумма членов списка (обратите внимание на оба способа и различие в синтаксисе доступа к элементам в циклах).
def total(numbers):
    result = 0
    for i in numbers:
        result = result + i
    return result
n = [3, 5, 7]
print(total(n))
print('\n', sep='')

''' Памятка

for item in list:	
    print(item)

for i in range(len(list)):
    print(list[i])
'''

# Конкантенация списков
def flatten(lists):
    results = []
    for numbers in lists:
        for i in numbers:
            results.append(i)
    return results
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
print(flatten(n))
print('\n', sep='')

# Рисует матрицу 5х5 из букв "O". 
def print_board(board): # Функция построчно выодит эти 5 списков. Как бы такой перевод каретки.
    for row in board:
        print(row)
board = []
for i in range(5):
    board.append(["O"] * 5) # Создается 5 списков, в каждом по пять "O".
print_board(board)
print('\n', sep='')

# Иллюстрация .join
def print_board(board):
    for row in board:
        print(" ".join(row))
board = []
for i in range(5):
    board.append(["O"] * 5)

print_board(board)
print('\n', sep='')

'''
# Использование генератора случайных чисел
from random import randint 
board = []
for x in range(0, 5):
    board.append(["O"] * 5)
def print_board(board):
    for row in board:
        print(" ".join(row))
def random_row(board):
    return randint(0, len(board) - 1) # Генератор 1
def random_col(board):
    return randint(0, len(board) - 1) # Генератор 2
print(random_row(board))	# Генератор 1
print(random_col(board)) # Генератор 2
print('\n', sep='')
'''

# Запрос числа от пользователя и помещение его в var.
var = input("var = (Input digit/text): ")
print("Ok!\nvar = %s" % var, sep='')
input()
