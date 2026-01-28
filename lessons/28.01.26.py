from time import time
# без лога
# def add(a,b):
#     return a + b
#
# def mul(a,b):
#     return a * b
# с логом
# def add_with_logging(a,b):
#     result = add(a,b)
#     return result
# def mul_with_logging(a,b):
#     result = mul(a,b)
#     return result

# def create_logging_wrapper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Вызвана функция {func.__name__} с аргументом {args}, результат: {result}')
#         return result
#     return wrapper
# @create_logging_wrapper
# def add(a,b):
#     return a + b
#
# @create_logging_wrapper
# def mul(a,b):
#     return a * b
#
# print(add(1,2))
# print(mul(3,4))

# add_with_logging = create_logging_wrapper(add)
# mul_with_logging = create_logging_wrapper(mul)
# print(add_with_logging(10,20))
# print(mul_with_logging(10,20))



# start = time()
# a = 1+1
# end = time()
# print(end - start)

# def timeit_func(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args)
#         print(time() - start)
#         return result
#     return wrapper
#
# @timeit_func
# def add(nums:list = []):
#     summ = 0
#     for num in nums:
#         summ += num
#     return summ
# @timeit_func
# def mull(nums:list = []):
#     mullt = 1
#     for num in nums:
#         mullt *= num
#     return mullt

# a = mull([1,2,3,4,5])
# a = mull([1,2,3,4,5])
# a = mull([1,2,3,4,5])
# a = mull([1,2,3,4,5])
# b = add([1,2,3,4,5])
# print(a, b)

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time()
        a = func(*args)
        print(time() - start, a)
        return a
    return wrapper

@timeit
def test(tfunc, list_nums):
    for i, num in enumerate(list_nums):
        list_nums[i] = tfunc(num)
    return list_nums
a = test(lambda x: x**2, [1, 2, 3])
print(a)

