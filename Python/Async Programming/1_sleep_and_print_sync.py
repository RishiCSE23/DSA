import time 
from datetime import datetime
import click  # print with style (req pip install)

def sleep_and_print(t): 
    """
    takes a time t in sec, sleeps for t and returns t. 
    """
    print(f'starting {t} sleep')
    time.sleep(t)  # sleeping for t sec.
    print(f'finished {t} sleep')
    return t

start = datetime.now()
print([sleep_and_print(3), sleep_and_print(6)]) # should take 3+6=9 sec
click.secho(f'{datetime.now()-start}',bold=True, bg='blue', fg='white')