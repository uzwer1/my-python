#управление кол-вом знаков после запятой в вещественных числах

print("%.2f" % total)

#управление выводом префиксов и значений

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

print '%s/%s/%s %s:%s:%s' % \
(now.month, now.day, now.year, \
now.hour, now.minute, now.second)

#удаление из списков

n = [1, 3, 5]

n.pop(0) # Удаляет элемент списка с заданным индексом
n.remove(1) # Удаляет элемент списка совпадающий с заданным значением
del(n[0]) # Удаляет элемент списка с заданным индексом, но не физически, а только из выдачи
print n

# Гибкость в передаче параметров в функциях

m = 5
n = 13

def add_function(x, y): # Свои переменные x и y.
    return x + y

print add_function(m, n) # m и n подставляются в функцию в качестве x и y.

# Еще пример

n = "Hello"

def string_function(s):
    return s + "world"

print string_function(n) # n поступает в функцию на место s.

def list_function(x):	# Пример ...
    return x			# ... с передачей ...

n = [3, 5, 7]
print list_function(n)	# ... списка.

# Функция добавляет элемент "9" в конец списка
n = [3, 5, 7]

def list_extender(lst):
    lst.append(9)
    return lst

print list_extender(n) # Напечатает: [3, 5, 7, 9]

# return в функции может отсутствовать (когда возвращает не одно значение?)

n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print print_list(n)

# Умножение каждого члена списка любой длины (с помощью range и len) на число 2.

n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)): # range(start, stop, step) . Здесь старт - 0-индекс списка (если пропущен, то по умолчанию - 0), стоп - последний индекс списка (определяется встроенной функцией len). Шаг не указан, по умолчанию равен 1.
        x[i] = x[i] * 2
    return x
    
print double_list(n) 

# range с помощью ф-ции создает список. Пока не совсем понятно зачем нужна такая конструкция.

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Напечатает: [0, 2, 4]

# Сумма членов списка (обратите внимание на оба способа и различие в синтаксисе доступа к элементам в циклах).

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in numbers:
    #for i in range(len(numbers)):
        result = result + i
        #result = result + numbers[i]
    return result

print total(n)

''' Памятка

for item in list:	
    print item

for i in range(len(list)):
    print list[i]
'''

# Конкантенация списков

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists:
        for i in numbers:
            results.append(i)
    return results

print flatten(n)

# Рисует матрицу 5х5 из букв "O". 
board = []
for i in range(5):
    board.append(["O"] * 5) # Создается 5 списков, в каждом по пять "O".

def print_board(board): # Функция построчно выодит эти 5 списков. Как бы такой перевод каретки.
    for row in board:
        print row

print_board(board)

# Иллюстрация .join

board = []
for i in range(5):
    board.append(["O"] * 5)
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

# Использование генератора случайных чисел

from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1) # Генератор 1

def random_col(board):
    return randint(0, len(board) - 1) # Генератор 2

print random_row(board)	# Генератор 1
print random_col(board) # Генератор 2

# Запрос числа от пользователя и помещение его в var.

var = int(raw_input("Prompt text"))