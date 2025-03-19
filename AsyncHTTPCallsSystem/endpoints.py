# Dependencies 
import time
import asyncio # For Asynchronous proccesses
import aiohttp # For Asynchronous HTTP requests management
from requests.exceptions import HTTPError
from . urls import URLS_List

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
        
asyncio.run(get_all_employees())