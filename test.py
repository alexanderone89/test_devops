import asyncio

async def my_task():
    while True:
        print('[+]   TEST RUN!')
        await asyncio.sleep(2)


async def main():
    task1 = loop.create_task(my_task())
    await asyncio.wait([task1])



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
