import requests
from abc import ABC, abstracmethod

# Abstract Classes
class AbstractHTTPClient(ABC):
    @abstracmethod
    def execute_get_request(url:str):
        pass

# Interfaces

# Classes
class HTTPClient(AbstractHTTPClient):
    def __init__(self):
        pass
        
    def execute_get_request(url:str) -> dict:
        try:
            response = requests.get(url)
            data = response.json()
            return data
        except Exception as e:
            raise e