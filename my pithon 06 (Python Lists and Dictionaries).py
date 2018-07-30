#Python Lists and Dictionaries
'''
Метод берет числа из одного списка
и с помощью стандартного для таких случаев
FOR возводит в квадрат каждый элемент списка.
Потом зачем-то (можно удаолить за ненадобностью)
сортирует полученные элементы нового списка
по возрастанию и выводит на экран поочередно
'''

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for x in start_list:
    x = x**2
    square_list.append(x)
square_list.sort()
print square_list
'''
'''
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')

for x in inventory['gold']:
    y = x+50
inventory['gold'].remove()
inventory['gold'].append(y)