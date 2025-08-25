import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["orders","products","customers","reviews","cancels"]

def my_func(i):

    wait = 3
    time.sleep(wait)
    print(f"I am {i}. I took {wait} seconds")



with ThreadPoolExecutor(max_workers=len(tables) ) as executor:
        # futures = executor.map(my_func,tables)
        for i in tables:
              future = executor.submit(my_func,i)


# for i in tables:
#     my_func(i)