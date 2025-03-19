from abc import ABC, abstractmethod
from enum import Enum

# Abstract Classes
class AbstractLesson(ABC):
	@abstractmethod
	def retrieve_lesson_data(self) -> dict:
		pass

# Interfaces
class I_SaveInstance(ABC):
    @abstractmethod
    def save_on_db(self, cursor:Cursor, table_name:str):
        pass

# Validation Classes
class V_Difficulty(Enum):
        EASY = 'Easy'
        MEDIUM = 'Medium'
        HARD = 'Hard'
        
# Classes
class Lesson(AbstractLesson, I_SaveInstance):
    def __init__(self, title:str, description:str, content:str|object|None, difficulty:str):
        if not isinstance(difficulty, V_Difficulty):
            raise ValueError('Difficulty attribute must be a valid V_Difficulty type ("Easy", "Medium", "Hard").')
        self.__title = title
        self.__description = description
        self.__content = content
        self.__difficulty = difficulty
    
    @property
    def title() -> str:
        return self.__title
    
    @property
    def description() -> str:
        return self.__description
        
    @property
    def content() -> str | object | None:
        return self.__content
    
    @property
    def difficulty() -> str:
        return self.__difficulty
    
    def retrieve_lesson_data(self) -> dict:
        lesson = {
            'title':self.title,
            'description':self.description,
            'content':self.content,
            'difficulty':self.difficulty
        }
        return lesson
        
    
    def save_on_db(self, cursor:Cursor, table_name:str) -> bool | str:
        """
            Saves the current Lesson object on the DB as a Lesson row.
        """
        try:
            # Create Users table if not exist
            cursor = cursor
            create_users_table(cursor=cursor)
            # Data
            fields = ['username', 'email', 'password', 'is_premium_user']
            values = [self.username, self.email, self.password, self.__is_premium_user]
            fields_str = ', '.join(fields)
            values_str = ', '.join(values)
            # Query Execution
            query = f"INSERT INTO {table_name} ({fields_str}) VALUES ({values_str});"
            cursor.execute_query(query=query)
            total_users = total_users + 1 # Increment the total users when a new user is saved on the database.
            self.__user.__registered = True
        except:
            self.__user.__registered = False
            
        # [Implement] Fix this method accordingly to this class-
