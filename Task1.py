# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите любую фразу: ')
print(f'Исходный текст: {text}')

find_txt = 'абв'
lst = [i for i in text.split() if find_txt not in i]
print(f'Обработанный текст: {" ".join(lst)}')



