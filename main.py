string = str(input("Введите строку: ")) #приглашение для ввода
words = string.split() #разделяем строку на слова
rev = [word[::-1] for word in words] #используем генератор списка для создания нового списка с перевернутыми словами
res  = ' '.join(rev) #соединяем перевёрнутые слова в строку
print(res) #выводим перевёрнутую строку