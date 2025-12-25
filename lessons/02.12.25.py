# 1.Напишите функцию которая принимает натуральное число а возвращает список его цифр

def func(a):
    return list(map(int, str(a)))
print(func(10))

# 2.Напишите функцию которая принимает текст и именнованные аргументы, и возвращает словарь с подсчетом слов
# с учетом опций, опции задаются через именнованные аргументы
# например, ignore_case = True, придумать 2 опции для посчета слов, опции могут быть не обязательными
s = '1234567890'
def words(text, **options):
    if options.get("ignore_case"):
        text = text.lower()
    if options.get("ignore_numbers"):
        for i in s:
            text = text.replace(i, '')
    text_list:list = text.split()
    text_set = set(text_list)
    dict_new = {}
    for text_set_item in text_set:
        dict_new[text_set_item] = text_list.count(text_set_item)
    return dict_new
print(words("hello23 World HeLLO", ignore_case=True, ignore_numbers=True))