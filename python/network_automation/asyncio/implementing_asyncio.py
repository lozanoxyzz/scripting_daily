import asyncio
import time

# synchronous
def sync_f():
    print('one', end=' ')
    time.sleep(1)
    print('two', end=' ')

# asynchronous
async def async_f():
    print('one', end=' ')
    await asyncio.sleep(1)
    print('two', end=' ')


async def main():
    #task = [async_f(), async_f(), asyncio ]
    tasks = [async_f() for _ in range(3)]

    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()

print(f'\nAsynchornous time:{end - start}')
print('\n')
print('#' * 40)

start = time.time()
for _ in range(3):
    sync_f()
end = time.time()
print(f'\nSynchronous time: {end-start}')


# async def f():
#     pass
#
#
# async def g():
#     await f() #pause here and come back to g() when f() is ready