# Understanding Async Programs 

* __Problem__: Cooking step by step waiting for each step to finish (_sync but slow process_)
* __Solution 1__: Hire more people to work simultainusly (_costly_)
* __Solution 2__: Interleave independent tasks i.e., perform another task while waiting for an independent task. (_Async_)

Executing tasks asynchronously means _manage to perform multiple things at the same time not doing multiple things simultainusly_ (which is rather called concurrency or parallel processing); i.e., using a single cook efficiently than having multiple cook. 
* With async programming speed-up is only possible when there are 
    1. There are independent tasks (chopping salad while boiling water)
    2. Tasks are less CPU intensive (can walk away while boiling water but not while chopping salad)
* Async programming shines when the programming logic is IO bound not CPU bound. 
    | CPU Bound | I/O bound |
    |---|---|
    | Arithmetic operation | HTTP Req |
    | Parsing | Database Access  |
    | String manipulation | Persistant Connections |

## Event Loop

* Event loop is the hart of async programming.  
* It manages async tasks using a __Event Queue__.
* There are multiple ways to hand tasks to the event loop. However Python 3.5+ supports __`async/await`__ keyword natively (best practice). Allows _writing async code that reads synchonously_.
* __Syntax__
    * __Typical function__:
        ```
        def func_1(val):
            # do something 
            result = blocking_func() # cpu bound
            return result

        def func_2(val):
            # do something 
            result = func1() # function chaining 
            return result
        
        ```
    * __Async function__:
        ```
        async def func_1(val):
            #do something 
            result = await non_blocking_func() # IO bound
            return result

        async def func_2(val):
            #do something 
            result = await func_1() # async func can only chain async funcs
            return result
        ```

## Rule of async in Python 

1. __Async code does not run itself__
    * __Example 1__: Async functions have to be handed over to the Event Loop to run. They can't be called like regular python functions. 
        ```
        aysnc def func_1(args): # define async function
            #something 
            await func_2()

        func_1()  # warning: func_1 never awaited. 
        ```
    * __Example 2__: The correct way, handing over the async function `func_1()` to an event loop offered by `asyncio`. This is not the only way but most preferred one. 
        ```
        import asyncio  # provides event loop

        aysnc def func_1(args): # define async function
            #something 
            await func_2()

        asyncio.run(func_1())  # handing over to the event loop. 
        ```
2. __Only async code can be awaited__
    * __Example__: A function can only `await` if it's defined as `async`.
        ```
        def func_1(args):
            #something
            await func2()   # error: await outside async function
        ```
3. __Awaiting a function does not magically make it async (the logic needs to be IO bound)__: In practice the callable APIs needs to be studied first, if it's a blockig API then find a non-blocking alternative (e.g., `aiohttp` in oppose to `request`). 

## Python async toolbox

Lets start with a simple synchronous code. 


```python
import time 
from datetime import datetime
import click  # print with style (req pip install)

def sleep_and_print(t): 
    """
    takes a time t in sec, sleeps for t and returns t. 
    """
    print(f'[{datetime.now()}]starting {t} sleep')
    time.sleep(t)  # sleeping for t sec.
    print(f'[{datetime.now()}]finished {t} sleep')
    return t

# caller 
start = datetime.now()
print([sleep_and_print(3), sleep_and_print(6)]) # should take 3+6=9 sec
click.secho(f'Time taken: {datetime.now()-start}',bold=True, bg='blue', fg='white')

```

    [2023-03-03 02:52:43.361876]starting 3 sleep
    [2023-03-03 02:52:46.362953]finished 3 sleep
    [2023-03-03 02:52:46.364107]starting 6 sleep
    [2023-03-03 02:52:52.364655]finished 6 sleep
    [3, 6]
    [37m[44m[1mTime taken: 0:00:09.003383[0m
    


```python
## Dont Run this cell!! 
## Jupyter notebook can't run async codes 
## check program 2 in the directory 

import asyncio
from datetime import datetime
import click  # print with style (req pip install)

async def sleep_and_print(t):  # define async function that can later await
    """
    takes a time t in sec, sleeps for t asynchonously and returns t. 
    """
    print(f'starting {t} sleep')
    asyncio.sleep(t)  # non-blocking alternative to time.sleep 
    print(f'finished {t} sleep')
    return t

async def caller():
    result = await asyncio.gather(sleep_and_print(3), sleep_and_print(6)) # takes multiple co-routines and run them concurrently 

start = datetime.now()
asyncio.run(caller()) # should take max(3,6)=6 sec
click.secho(f'{datetime.now()-start}',bold=True, bg='blue', fg='white')
```


```python

```
