import requests
import timeit
from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio

session = requests.session()
url = "http://127.0.0.1:5000"

Count = 100


def req(url: str):
    print('req1', url)
    req = requests.get(url)
    req.status_code


def requests_test():
    """
    第一组:循环的方式
    :return:
    """
    for i in range(Count):
        req(url)


def pool_requests_test():
    """
    第二组:线程池的方式
    :return:
    """
    url_list = [url for _ in range(Count)]
    with ThreadPoolExecutor(max_workers=20) as pool:
        pool.map(req, url_list)


async def fetch(url: str):
    async with aiohttp.TCPConnector(ssl=False) as tc:
        async with aiohttp.ClientSession(connector=tc) as session:
            async with session.get(url) as req:
                req.status


async def start():
    tasks = [asyncio.create_task(fetch(url)) for _ in range(Count)]
    await asyncio.wait(tasks)


def aiohttp_test():
    """
    第三组:aiohttp 的方式
    :param url:
    :return:
    """
    asyncio.run(start())


if __name__ == '__main__':
    # 循环的
    # print(timeit.timeit(stmt=requests_test, number=1))
    # 使用线程池的
    # print(timeit.timeit(stmt=pool_requests_test, number=1))
    # 使用 aiohttp 的
    print(timeit.timeit(stmt=aiohttp_test, number=1))
