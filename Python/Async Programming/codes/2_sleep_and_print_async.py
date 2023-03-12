import asyncio
from datetime import datetime
import click  # print with style (req pip install)

async def sleep_and_print(t):  # define async function that can later await
    """
    takes a time t in sec, sleeps for t asynchonously and returns t. 
    """
    print(f'[{datetime.now()}] starting {t} sleep')
    asyncio.sleep(t)  # non-blocking alternative to time.sleep 
    print(f'[{datetime.now()}] finished {t} sleep')
    return t

async def caller(min:int=0 ,max:int=0):
    """
    takes min and max values 
    programmatically adds co-routines sleep_and_print(x): x in range(min,max)
    runs them asynchronously 
    """
    if not (min and max):
        # gather: takes multiple co-routines and run them concurrently 
        result = await asyncio.gather(sleep_and_print(3), sleep_and_print(6)) 
    else:
        # programatically add multiple co-routine 
        coroutine_list = []
        for t in range(min,max):
            coroutine_list.append(sleep_and_print(t)) #function will not be called here 
        
        result = await asyncio.gather(*coroutine_list)  #passing list members as individual args
        print(result)


start = datetime.now()
asyncio.run(caller()) # should take MAX(3,6)=6 sec
click.secho(f'Time taken: {datetime.now()-start}',bold=True, bg='blue', fg='white')

start = datetime.now()
asyncio.run(caller(min=1,max=10)) # should take MAX(min,max)=max sec
click.secho(f'Time taken: {datetime.now()-start}',bold=True, bg='blue', fg='white')