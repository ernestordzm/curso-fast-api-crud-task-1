

import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def taskAsyncio(text = 'Message'):
     while(True):
        print(text)
        await asyncio.sleep(1)



try:
    print('antes de la tarea...')

    # loop.run_until_complete(taskAsyncio())
    # loop.run_until_complete(taskAsyncio('Other Message'))

    asyncio.ensure_future(taskAsyncio())
    asyncio.ensure_future(taskAsyncio('Other message'))

    loop.run_forever()
    print('despues de la tarea...')
except KeyboardInterrupt:
        pass
finally:
    loop.close()

