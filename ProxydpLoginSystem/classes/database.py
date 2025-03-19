from abc import ABC, abstractmethod
import psycopg2

# Abstract Classes
class  AbstractDatabase(ABC):
    @abstractmethod
	def connect(self):
		pass
		
	@abstractmethod
	def close(self):
		pass
        
class AbstractCursor(ABC):
    @abstractmethod
    def execute_query(self):
        pass
        
    @abstractmethod
    def create_table(self, name:str, fields:list):
        pass
        
# Interfaces
class I_Cursor(ABC):
    @abstractmethod
    def create_cursor(self):
        pass
       
# Classes
class RelationalDatabase(AbstractDatabase):
    def __init__(self, database:str, host:str, user:str, password:str, port:str='5432'):
        self.__database = database
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__conn = None
    
    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        
    def close(self):
        self.conn.close()
    
    def commit(self):
        self.conn.commit()
        
class Cursor(AbstractCursor, I_Cursor):
    def __init__(database:RelationalDatabase):
        self.__database = database
        self.__cursor = None
    
    @property
    def database(self) -> object:
        return self.__database
   
    @property
    def cursor(self) -> object | None:
        return self.__cursor
    @cursor.set
    def cursor(self, value:object):
        self.cursor = value:
    
    def create_cursor(self):
        self.cursor = self.database.conn.cursor()
        
    def create_table(self, name:str, fields:list):
        self.database.connect()
        fields_str = ", ".join(fields)
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {name} (
            {fields_str}
        )
        """)
        self.database.commit()
        self.database.close()
        
    def execute_query(self, query:str):
        try:
            self.database.connect()
            self.cursor.execute(query)
            self.database.commit()
            self.database.close()
        except Exception as e:
            raise Exception(f'Unexpected Error: {e}')