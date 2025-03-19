import time # For execution times monitoring
import asyncio # For Asynchronous processes
import aiohttp # For Asynchronous HTTP requests management
from requests.exceptions import HTTPError # For HTTP errors handling
from . urls import URLS_List # List of urls

async def get_all_employees():
    """
       Retrieves all the employees using async http calling. 
    """
    url = URLS_List[1]
    init_time = time.time()
    
    try:
        async with aiohttp.ClientSession() as session: # session = await aiohttp.ClientSession() : 
            async with session.get(url) as response: # response = await session.get(url)
                if response.status != 200:
                    raise HTTPError()
                data = await response.json()
                
                end_time = time.time() - init_time
                print(f'Execution time: {end_time}')
                
                return data
    except Exception as e:
        raise e
        
async def get_all_customers():
    """
       Retrieves all the customers using async http calling. 
    """
    url = URLS_List[2]
    init_time = time.time()
    
    try:
        async with aiohttp.ClientSession() as session: # session = await aiohttp.ClientSession() : 
            async with session.get(url) as response: # response = await session.get(url)
                if response.status != 200:
                    raise HTTPError()
                data = await response.json()
                
                end_time = time.time() - init_time
                print(f'Execution time: {end_time}')
                
                return data
    except Exception as e:
        raise e