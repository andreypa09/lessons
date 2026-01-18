# square = lambda x: x ** 2
# print(square(5))

# numbers = [-1, 2, -3, 4, 5]
# def double_pos(num):
#     if num > 0:
#         return num * 2
#     return num
# pos_doubled = [double_pos(i) for i in numbers]
# print(pos_doubled)

# double_pos = lambda num: num * 2 if num > 0 else num
# pos_doubled = [double_pos(i) for i in numbers]
# print(pos_doubled)

# dict_students = [
#     {"name": "John", "age": 25, "grade": 10},
#     {"name": "Борис", "age": 10, "grade": 1},
#     {"name": "Аркадий", "age": 30, "grade": 4}
# ]
# get_name = lambda student: student.get("name")
# get_age = lambda student: student.get("age")
# get_student = lambda student: student.get("grade") if student.get("grade") > 3 else None
#
# names = [get_name(student) for student in dict_students]
# ages = [get_age(student) for student in dict_students]
# grades = [get_student(student) for student in dict_students if get_student(student)]
# print(names)
# print(ages)
# print(grades)

# unsorted_list = [4, 3, 2, 5, 1]
# print(sorted(unsorted_list))
# unsorted_str = "ZV-bc-aA"
# print(sorted(unsorted_str))

# unsorted_dict = {
#     4 : "Maria",
#     2: "Ivan",
#     1: "Pavel",
#     3: "Alisa"
# }
# print(sorted(unsorted_dict))



# words = ["Andrey", "my", "name"]
# sorted_list = sorted(words, key = len)
# print(sorted_list)

# nums = [14, 5, 23, 42, 31]
# sorted_nums = sorted(nums, key = lambda num: num % 10)
# print(sorted_nums)

# students = [
#     ('John', 98),
#     ('Michael', 77),
#     ('Bob', 92),
#     ('Robert', 84),
#     ('Kevin', 85)
# ]
#
# print(sorted(students, key = lambda x: x[1]))


# dict_students = [
#     {"name": "John", "age": 25, "score": 98},
#     {"name": "Борис", "age": 10, "score": 77},
#     {"name": "Аркадий", "age": 30, "score": 92}
# ]
# sorted_dict_students = sorted(dict_students, key=lambda student: student["score"], reverse=True)
# print(sorted_dict_students)

# students = [
#     ("Алиса", 4),
#     ("Борис", 5),
#     ("Виктор", 4),
#     ("Галина", 3),
#     ("Дмитрий", 5),
#     ("Елена", 3)
# ]
# students_sorted = sorted(students, key=lambda student: student[1], reverse=True)
# for name, grade in students_sorted:
#     print(f"{name}: оценка {grade}")
# str_len = lambda x: len(x) * 8
# print(str_len('Python'))

# def my_logger(a, cube = lambda x: x ** 3):
#     result = cube(a)
#     return result
# print(my_logger(5))

# is_even = lambda x: x % 2 == 0
# print(is_even(4), is_even(7))

# Отсортируйте список data = [(1, "b"), (3, "a"), (2, "c")]
# по второму элементу кортежа (в лексикографическом порядке)
# data = [(1, "b"), (3, "a"), (2, "c")]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)

# Напишите функцию user_action_logger, которая принимает список actions
# (содержащий лямбда-функции для операций над числами, например, сложение, умножение и т.д.),
# лямбда-функцию log_func для форматирования лога (она принимает строку описания действия и возвращает форматированную строку лога).
# Функция должна в цикле запрашивать у пользователя ввод числа, применять по очереди каждую лямбда-функцию из списка actions
# к текущему значению, логировать каждое действие с помощью log_func (выводя лог на экран) и возвращать финальное значение
# после применения всех операций.
#
# Протестируйте функцию с тремя лямбда-функциями (для сложения на 2, умножения на 3 и вычитания 1),
# лямбдой для лога (добавляющей префикс "[LOG] ").

# def user_action_logger(actions, log_func = lambda x: x + "[LOG] "):
#     a = 0
#     b = int(input())
#     for i in range(3):
#         actions = [lambda x: x + 2]
#         a = b + actions[i](a)
# dodelat


# hw 1. Используйте лямбда-функцию в функции min с параметром key,
# чтобы найти человека с минимальным возрастом. Выведите имя и возраст.
# student = [
#     ("Анна", 16),
#     ("Бронислав", 15),
#     ("Федот", 18)
# ]
# min_student = min(student, key = lambda x: x[1])
# print(min_student[0], min_student[1])
# 2.Создайте лямбда-функцию, которая принимает число и возвращает "positive", если
# оно положительное, "negative" — если отрицательное, и "zero" — если ноль.
# Присвойте её переменной sign и протестируйте на числах 5, -3 и 0, выведя результаты в цикле.

# sign = lambda x: "positive" if x > 0 else "zero" if x == 0 else "negative"
# new_sign = [sign(i) for i in [5, -3, 0]]
# print(new_sign)
# 3.Напишите функцию calculator, которая принимает две лямбды (для сложения и вычитания)
# и два числа, затем применяет каждую лямбду к числам и возвращает список результатов.
# Создайте соответствующие лямбды и вызовите функцию для 10 и 4. Выведите результат.
# def calculator(num1, num2):
#     plus = lambda a, b: a + b
#     minus = lambda a, b: a - b
#     return plus(num1, num2), minus(num1, num2)
# print(calculator(10, 4))
# 4.В магазине для упаковки подарков есть N кубических коробок. Самой интересной считается упаковка подарка по принципу матрёшки
# – подарок упаковывается в одну из коробок, та, в свою очередь, в другую коробку и т.д.
# Одну коробку можно поместить в другую, если длина её стороны меньше длины стороны другой коробки не менее чем на 9 единиц.
# Определите наибольшее количество коробок, которое можно использовать для упаковки одного подарка,
# и максимально возможную длину стороны самой маленькой коробки, где будет находиться подарок.
# Размер подарка позволяет поместить его в самую маленькую коробку.
# with open('2601.txt') as f:
#     N = int(f.readline())
#     data = [list(map(int, i)) for i in f]
# def f1(lenght):
#     for lenght in data:

