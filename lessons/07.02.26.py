# асинхронность
# def a():
#     print("hello")
# a()
# print("world")
import asyncio


# процессы(ресурсы/память/файлы/соеденения) ->
# Потоки -> (ресурсы от процессы / быстрее создаются и переключаются / могут обменивать данными)

import asyncio
# async with async for
# async def f():
#     print("Привет")
#     await asyncio.sleep(1)
#     print("мир")
#
# asyncio.run(f())

# def sync_f():
#     return "Результат"
# async def async_f():
#     return "Тоже"
# print(sync_f())
# print(async_f())
# asyncio.run(async_f())

# async def one(num):
#     print("f_1 start")
#     await asyncio.sleep(num)
#     print("f_1 end")
# async def two(num):
#     print("f_2 start")
#     await asyncio.sleep(num)
#     print("f_2 end")
# async def main():
#     await one(1)
#     await two(2)

    # results = await asyncio.gather(one(10), two(2))



#     task1 = asyncio.create_task(one())
#     task2 = asyncio.create_task(two())
#     while True:
#         await asyncio.sleep(1)
#         task1.cancel()
#         print("hello")
#     result1 = await task1
#     result2 = await task2


# asyncio.run(main())


# async def download_page(url):
#     print(f'Загружаю {url}')
#     await asyncio.sleep(1)
#     return f"Содержимое {url}"
# async def main():
#     urls = [
#         "https://www.baidu.com/",
#         'https://www.baidu.com/1',
#         'https://www.baidu.com/2',
#         'https://www.baidu.com/3',
#         'https://www.baidu.com/4',
#     ]
#     TASK = asyncio.create_task(download_page(urls[0]))
#     await asyncio.gather(TASK)
#     pages = await asyncio.gather(*[download_page(url) for url in urls])
#     print(f"Загружено {len(pages)} страниц")
#     for content in pages:
#         print(content)
#
# asyncio.run(main())

# async def make_coffe():
#     print("Коффе готовится")
#     await asyncio.sleep(1)
#     print('Коффе готов')
# async def make_toast():
#     print('Тост готовится')
#     await asyncio.sleep(1)
#     print("Тост готов")
#
# async def main():
#     await make_coffe()
#     await make_toast()
#
# asyncio.run(main())

# 1.Создайте функцию calculate(x, delay), которая ждёт delay секунд и возвращает квадрат числа x.
# Запустите три вызова параллельно для чисел 2, 3, 4 с задержками 1, 2, 1 секунда соответственно.
# Выведите все результаты.
#
# async def calculate(x, delay):
#     await asyncio.sleep(delay)
#     print(x ** 2)
# async def main():
#     await asyncio.gather(calculate(2, 1), calculate(3, 2), calculate(4, 1))
# asyncio.run(main())

# 2.Создайте функцию long_task(), которая ждёт 5 секунд.
# Запустите её как задачу, подождите 2 секунды и отмените задачу.
# Выведите сообщение об отмене.

# async def long_task():
#     await asyncio.sleep(5)
# def main():
#     await asy