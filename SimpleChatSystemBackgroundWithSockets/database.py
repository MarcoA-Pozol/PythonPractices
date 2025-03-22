import sqlite3
from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @execute_query
    def execute_query(self) -> None:
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
		
database_object = Database(database_name='ChatDatabase.db')
