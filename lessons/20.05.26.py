# from time import time
# start = time()
# for i in range(10):
#     print(123)
# end = time()
# print(end - start)

# from timeit import timeit
# s = """
# for i in range(100):
#     print(i)
#     """
# def a(num1, num2):
#     z = num1 + num2
#     z1 = num1 - num2
#     return z * z1
# time_result = timeit(
#     stmt = s, # Код который будет замеряться по времени
#     number = 1000,
#     setup = "a = 1000",
#     globals = globals(),
# )
# print(time_result / 1000)


# s = 'Hello world'

# table = {
#     ord('l'): ord('&'),
#     ord('o'): ord('@'),
#     ord('H'): None
# }
# table = str.maketrans('lo', '&@', 'H')
# table = str.maketrans({
#     'l':'&',
#     'o':'@',
#     'H': None
# })
# result = s.translate(table)
# print(result)


from timeit import timeit
# s = """
# a = ''
# for i in range(1000):
#     a += 'a'
# """
# s1 = """
# k = ''.join(['a' for i in range(1000)])
# """
# programm1 = timeit(
#     stmt = s,
#     number = 1000,
#     globals = globals()
# )
# programm2 = timeit(
#     stmt = s1,
#     number = 1000,
#     globals = globals()
# )
# print(f"Время выполнения первой: {programm1}\nВремя выполнения второй: {programm2}")

# code1 = """
# sum_nums = sum(list_nums)
# """
#
# code2 = """
# k = 0
# for i in list_nums:
#     k += i
# """
#
# programm1 = timeit(code1, number = 1000, setup = "list_nums = range(0, 10000)", globals = globals())
# programm2 = timeit(code2, number = 1000, setup = "list_nums = range(0, 10000)", globals = globals())
# print(f"Время выполнения первой: {programm1}\nВремя выполнения второй: {programm2}\nРазница = {programm2 / programm1}")


# code1 = """
# sum_nums = sum(list_nums)
# """
#
# code2 = """
# k = 0
# for i in list_nums:
#     k += i
# """

