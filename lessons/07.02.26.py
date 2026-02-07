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
#     results = await asyncio.gather(one(10), two(2))
#     print(results)


#     task1 = asyncio.create_task(one())
#     task2 = asyncio.create_task(two())
#     while True:
#         await asyncio.sleep(1)
#         task1.cancel()
#         print("hello")
    # result1 = await task1
    # result2 = await task2
    # await one()
    # await two()

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

async def make_coffe():
    print("Коффе готовится")
    await asyncio.sleep(1)
    print('Коффе готов')
async def make_toast():
    print('Тост готовится')
    await asyncio.sleep(1)
    print("Тост готов")

async def main():
    await make_coffe()
    await make_toast()

asyncio.run(main())