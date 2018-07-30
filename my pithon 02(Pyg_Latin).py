# Это Свиная Латынь, детка!!!
pyg = 'ay' #Задаем суффикс для для операции над СЛОВОМ
original = raw_input('Enter a word:') #Запрос на ввод СЛОВА

if len(original) > 0:
    word = original.lower()
    first = word[0]
    new_word = word + first +pyg
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print (empty)