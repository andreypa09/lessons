
# открытие файла(маршрут) / тип открытия / кодировка при чтении / записи
# file = open("test.txt", "r", encoding="utf-8")


# r - чтение
# w - запись
# a - добавлять в конец файла
# x - открывает файл для записи только если он не существует
# rb, wb, ab, xb - бинарные действия
# r+/x+ - открывает файл для чтения и записи (файл должен существовать)
# w+/a+ - открывает файл для записи если файла нет он его создаст

# print(file.read()) считывает все строки текстового файла
# print(file.readline()) считывает одну строку текст. файла
# print(file.readlines()) считывает файл как список строк


# print(file.readline()) #курсор в начале первой строки
# print(file.readline()) #курсор в начале второй строки
# print(file.readline()) #курсор в начале третьей строки
# print(file.readline()) #курсор в начале четвертой строки


# print(file.readline(10))
# print(file.tell()) #позиция указателя (число)

# file.seek(0) #возвращает курсор на указанное место

# print(file.readline(10)) # читает 10 элемент строки


# file.close() #закрытие файлов

# контекстный менеджер
# with open("test.txt","r", encoding="utf-8") as file:
    # file_item = file.readline()
    # while file_item:
    #     print(len(file_item))-1
    #     file_item = file.readline()


    # for file_item in file:
    #     print(len(file_item))-1

# with open("test.txt","w+", encoding="utf-8") as file:
#     file.write("hello world")
#
# with open("test.txt","r+", encoding="utf-8") as file:
#     file.write("\nhello world")


# s = ["hello\n", "world"]
# with open("test.txt","w", encoding="utf-8") as file:
#     file.writelines(s)

# s = ['a\n', 'b\n', 'c']
# with open("test1.txt", "w+", encoding="utf-8") as file:
#     file.writelines(s)
# with open("test1.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# homework
# 1.Cоздайте файл в режиме 'w' с текстом "Привет\nКак дела\n".
# Затем в режиме 'a' добавьте строку "Как погода\n"
# с помощью write(). Прочитайте весь файл в режиме 'r' с помощью readlines() и выведите список строк.

# with open("hw1.txt", "w+", encoding="utf-8") as file:
#     file.write("Привет\nКак дела\n")
# with open("hw1.txt", "a", encoding="utf-8") as file:
#     file.write("Как погода\n")
# with open("hw1.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())

# 2.Дан словарь:
# python
#
# {"A": 10, "B": 20, "C": 30}
# Замените ключи на случайные трехзначные числа. Запишите полученный словарь в файл в режиме 'w',
# каждую пару ключ-значение на новой строке в формате "ключ:значение\n".
# Затем прочитайте файл в режиме 'r' с помощью readlines() и выведите пары.


# from random import randint
# d = {"A": 10, "B": 20, "C": 30}
# new_dict = {}
# new_dict.update({
#     randint(100,999): d["A"],
#     randint(100,999): d["B"],
#     randint(100,999): d["C"],
# })
# with open("hw2.txt", "w+", encoding="utf-8") as file:
#     for key, value in new_dict.items():
#         file.write(f"{key}:{value}\n")
# with open("hw2.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())

# Создайте файл в режиме 'w' с 50 строками случайных чисел от 1 до 100.
# В режиме 'a' добавьте 20 строк. Прочитайте все в режиме 'r' с readlines() и выведите сумму всех чисел.


import random
with open("hw3.txt", "w+", encoding='utf-8') as file:
    for i in range(50):
        a = random.randint(1,100)
        file.write(str(a) + '\n')
with open("hw3.txt", "a", encoding='utf-8') as file:
    for i in range(20):
        a = random.randint(1, 100)
        file.write(str(a) + '\n')
with open("hw3.txt", "r", encoding='utf-8') as file:
    a = file.readlines()
    summ = 0
    for i in a:
        summ += int(i)
    print((summ))
