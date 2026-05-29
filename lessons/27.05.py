from timeit import timeit
# # 3.
# # Есть длинная строка. Нужно узнать, сколько раз встречается "ab" тремя способами:
# #
# # count()
# #
# # Цикл с проверкой среза
# #
# # Разбиение через split()
#
# s = 'ab' * 50000
#
# def count_func():
#     return s.count('ab')
#
# def for_func():
#     counter = 0
#     for i in range(len(s)):
#         if s[i:i+2] == 'ab':
#             counter += 1
#     return counter
#
# def split_func():
#     return len(s.split('ab'))
#
# print('count()', timeit('count_func()', globals = globals(), number =1000))
# print('loop', timeit('for_func()', globals = globals(), number =1000))
# print('split_func', timeit('split_func()', globals = globals(), number =1000))


# 4.
# Есть строка длиной 200 000 символов. Нужно проверить, есть ли в ней "abcde" и сравнить работу:
# оператор in
# метод find()
# разбиение через split()
# ручной перебор

# s = 'abc' * 40000 + 'abcde' * 300
#
# def in_func():
#     return 'abcde' in s
#
# def find_func():
#     s.find('abcde')
#
# def split_func():
#     return len(s.split('abcde')) > 1
#
# def for_func():
#     for i in range(len(s)):
#         if s[i:i+5] == 'abcde':
#             return True
#     return False
#
# print('in_func:', timeit('in_func()', globals=globals(), number=1000))
# print('find_func:', timeit('find_func()', globals=globals(), number=1000))
# print('split_func:', timeit('split_func()', globals=globals(), number=1000))
# print('for_func:', timeit('for_func()', globals=globals(), number=100))



nums = [1, 3, 5, 6]
target = 2
def func():
    global nums, target
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def find_target_2(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (r + l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1





