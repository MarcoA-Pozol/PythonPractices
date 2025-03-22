import sqlite3
from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @execute_query
    def execute_query(self) -> None:
        pass
       
class AbstractCursor(ABC):
    @abstractmethod
    def execute_select_query(table_name:str, fields:list[str]) -> list:
        pass

class Database(AbstractDatabase):
	def ___init__(self, database_name:str) -> None:
		self.conn = sqlite3.connect(database_name)
		self.cursor = self.conn.cursor()
	
	def execute_query(self, query:str) -> None:
		"""
			Executes a query of any type.
		"""
		self.cursor.execute(query)
        
class Cursor(AbstractCursor):
    def __init__(self, database_object:Database):
        self.__database = database_object
        self.__cursor = self.__database.cursor()
    
    # Props setter and getter methods
    @property
    def database(self) -> Database:
        return self.__database
    
    @property
    def cursor(self):
        return self.__cursor
    
    # Methods
    def execute_select_query(self, table_name:str, fields:list[str]) -> list:
        """
            Receives a table name and a group of fields to execute a simple SELECT query to an specified database table and returns the queryset in list format.
        """
        try:
            data = self.cursor.execute(f"""SELECT {field for field in fields}.join(', ') FROM {table_name};""").fetchone()
            return data
        except Exception as e:
            print(e)
            raise e