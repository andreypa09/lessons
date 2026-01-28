# def create_discount(category, discount):
#     def bronze(price):
#         return price * 2 - (discount / 100)
#     def silver(price):
#         return price * 0.5
#     def gold(price):
#         return price * 0.1
#     if category == 'bronze':
#         return bronze
#     elif category == 'silver':
#         return silver
#     elif category == 'gold':
#         return gold
# bronze_discount = create_discount('bronze', 100)
#
# product_price = 1000
# print(f"{bronze_discount(product_price)}")

# def make_even_generator(start):
#     def even():
#         nonlocal start
#         result = start
#         start = start + 2
#         return result
#     return even
# add_2 = make_even_generator(2)
# print(add_2())
# print(add_2())
# print(add_2())
# print(add_2())

# def make_string_builder(string):
#     builder = ''
#     def new_string():
#         nonlocal builder
#         builder += string
#         return builder
#     return new_string
# make_new_string = make_string_builder('hello ')
# print(make_new_string())
# print(make_new_string())
# print(make_new_string())


# def make_product_accumulator(x1):
#     def product(x2):
#         nonlocal x1
#         x1 *= x2
#         return x1
#     return product
# accumulator = make_product_accumulator(2)
# print(accumulator(0.5))
# print(accumulator(2))
# print(accumulator(2))

# def make_counter(start, step):
#     def new_step():
#         nonlocal start
#         start = start + step
#         distance = start
#         return distance
#     return new_step
# counter = make_counter(1, 1)
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())

# def create_length_filter(min_length):
#     def length_filter(a):
#         return len(a) >= min_length
#     return length_filter
# string = create_length_filter(5)
# print(string('assss'))

# hw
# 1. Создайте функцию с замыканием make_stats_tracker(), которая возвращает четыре функции: для добавления числа,
# получения среднего значения, получения минимума и максимума.
# Функция должна эффективно отслеживать все необходимые статистики.



# 2. Создайте функцию с замыканием make_task_manager(), которая возвращает набор функций для управления задачами:
# добавление задачи, пометка задачи как выполненной по ID, получение списка всех задач, получение списка невыполненных задач и
# получение статистики.
# Каждая задача должна иметь уникальный ID, название и статус выполнения.
# def make_task_manager():
#     def add_task():
#         return

# 3. Напишите функцию apply_to_each(numbers, operation), которая принимает список чисел и функцию-колбэк,
# применяет эту функцию к каждому элементу списка и возвращает новый список с результатами.
# Протестируйте её с функциями возведения в квадрат и удвоения числа.

# def apply_to_each(numbers, operation):
#     new_numbers = list(map(operation, numbers))
#     return new_numbers
# print(apply_to_each([1, 2, 3, 4, 5], lambda x: x * 2))
# print(apply_to_each([1, 2, 3, 4, 5], lambda x: x * x)) 