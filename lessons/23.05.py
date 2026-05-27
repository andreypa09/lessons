from timeit import timeit
# setup = """
# s_list = list(range(10**6))
# s_set = set(range(10 ** 6))
# """
# def f1():
#     return int("9"*6) in s_list
# def f2():
#     return 999999 in s_set
#
# timer1 = timeit(setup = setup, stmt = "999999 in s_set", number = 1)
# timer2 = timeit(setup = setup, stmt = "999999 in s_list", number = 6)
# print(timer1, timer2)

# from random import randint
#
# s_list = [randint(1, 10000) for _ in range(10000)]
# def duplicates_loops(nums):
#     duplicates = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j] and nums[i] not in duplicates:
#                 duplicates.append(nums[i])
#     return duplicates
#
# def duplicates_set(nums):
#     seen = set()
#     duplicates = set()
#     for i in range(len(nums)):
#         if nums[i] in seen:
#             duplicates.add(nums[i])
#         else:
#             seen.add(nums[i])
#     return list(duplicates)
#
# timer1 = timeit("duplicates_loops(s_list)", globals=globals(), number=1)
# timer2 = timeit("duplicates_set(s_list)", globals=globals(), number=1)
#
# print(f"Время работы через циклы: {timer1:.6f} сек")
# print(f"Время работы через set:   {timer2:.6f} сек")


s_list = list(range(1, 100000))
def reverse_list(nums):
    return nums.reverse()
def srez_list(nums):
    return nums[::-1]
def cikl_list(nums):
    k = []
    for i in range(len(nums)-1, -1, -1):
        k.append(nums[i])
    return k
print(srez_list(s_list))
timer1 = timeit(stmt="srez_list(s_list)", number=100, globals=globals())
timer2 = timeit(stmt="cikl_list(s_list)", number=100, globals=globals())
timer3 = timeit(stmt="reverse_list(s_list)", number=100, globals=globals())

print(timer1, timer2, timer3)
