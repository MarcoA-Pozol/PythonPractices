from abc import ABC, abstractmethod
from . database import RelationalDatabase, Cursor

# Abstract classes
class AbstractUserAuthenticator(ABC):
    @abstractmethod
    def register(self):
        pass
        
    @abstractmethod
    def login(self):
        pass 
    
    @abstractmethod
    def logout(self):
        pass

class AbstractUser(ABC):
    @abstractmethod
    def suscribe_to_course(self, course_name:str):
        pass
        
       
# Interfaces
class I_SaveInstance(ABC):
    @abstractmethod
    def save_on_db(self, cursor:Cursor, table_name:str):
        pass

class I_DataValidation(ABC):
    @abstractmethod
    def validate_init_data(self):
        pass
        
class I_DataRetriever(ABC):
    @abstractmethod
    def obtain_list_from_dictionary(self, dictionary:dict, table_name:str) -> list:
        pass
    
    @abstractmethod
    def obtain_list_from_db(self, cursor:Cursor, table_name:str, fields:list[str] | str) -> list:
        pass
        
    @abstractmethod
    def obtain_list_from_queryset(self, database_name:str, query:str) -> list:
        pass
    
# Classes
class QueryExecutor(I_DataRetriever):
    def __init__(self):
        pass
    
    def obtain_list_from_dictionary(self, dictionary:dict, table_name:str) -> list:
        result_list = dictionary[table_name]
        return result_list
        
    def obtain_list_from_db(cursor:Cursor, table_name:str, fields:list[str] | str) -> list:
        cursor = cursor
        if isInstance(fields, list):
            fields_str = ', '.join(fields)
        elif isInstance(fields, str):
            fields_str = fields
        else:
            raise ValueError(f'Fields value must be a str or list[str] type.')
        query = f"SELECT {fields} from {table_name}"
        # [Implement] Query execution by cursor logic.
        result = cursor.execute_query(query=query)       
        return result
    
    def obtain_list_from_queryset() -> list:
        # [Implement] Db connection  logic.
        # [Implement] Cursor creation logic.
        pass
        
        

class User(AbstractUser, AbstractUserAuthenticator, I_DataValidation, I_SaveInstance):
    """
        User who is going to to actions, ones once is authenticated and ones while not.
    """
    def __init__(self, username:str, email:str, password:str):
        # User
        self.__username = username
        self.__password = password
        self.__email = email
        self.__is_premium_user = False
        # Permissions 
        self.__authenticated = False
        self.__validated = False
        self.__registered = False
     
        if validate_init_data(username, email, password) == True:
            self.__validated = True
        else:
            self.__validated = False
            raise ValueError(f'Invalid init data for this object: {self}')
            
    
    @property
    def username(self) -> str:
        return self.__username
    @username.set
    def username(self, value:str):
        if not isInstance(value, str):
            raise ValueError('The provided username is not a correct type.')
        if len(value) < 6:
            raise ValueError('Username must contain at at least 6 characters.')
        if len(value) > 20:
            raise ValueError('Username cannot contain more than 20 characters.')
        self.__username = value
         
    @property
    def password(self) -> str:
        return self.__password
    @password.set
    def password(self, value:str):
        # [Implement] Enable a connection with a common passwords API obtaining them as a dataset and transforming it to a list of common passwords.
        common_passwords = ['123456789', 'secretpassword', 'mach1029', 'mydogname', 'gayifyouguess', 'thepassword', 'username', 'password', '987654321']
        
        if not isInstance(value, str):
            raise ValueError('The provided password is not a correct type.')        
        if len(value) < 6:
            raise ValueError('Password must contain at at least 8 characters.')
        if len(value) > 16:
            raise ValueError('Password cannot contain more than 16 characters.')
        if value in common_passwords:
            raise ValueError('The provided password is in a common passwords list, use a different one for better security.')
        # [Implement] Add a validation to check if value is like i for i in common_passwords list.
        self.__password = value
    
    @property
    def email(self) -> str:
        return self.__email
    @email.set
    def email(self, value:str):
        if not isInstance(value, str):
            raise ValueError('The provided email is not a correct type.')
        if not value.have('@') and not value.have('.')
            raise ValueError('This is not a valid email format.')
        self.__email = value
        
    def register(self) -> bool:
        if self.__registered == False:
            print(f'Welcome {self.username}, your account was created successfully!')
        else:
            print(f'The provided username or email are in use for an existing account.')
        return self.__registered
            
    def login(self) -> bool:
        if self.__authenticated == True:
            print(f'Hi {self.__username}! You are currently online :)')
        else:
            print('Impossible to login, the provided password or username are incorrect.')
        return self.__authenticated
        
    def logout(self) -> bool:
        if self.__authenticated:
            print('It was impossible to close session.')
        else:
            print('We hope to see you soon.')
        return self.__authenticated
        
    def suscribe_to_course(self, course_name:str) -> str:
        # [Implement] Extend the logic for this method, receiving a Course object 
        # to check if the user can pay for or not in the case the course costs.
        if self.__authenticated == True:
            result = f'{self.username}: You have been successfully suscribed to this course: {course_name}, start learning now!'
        else:
            result = 'You are offline, please sign in to have access to the advanced features.')
        return result
        
    def validate_init_data(username:str, email:str, password:str) -> bool:
        try:
            self.username = username
            self.email = email
            self.password = password
            
            return True
        except Exception as elif:
            raise e
            return False
    
        
            
class UserAuthenticationProxy(AbstractUserAuthenticator):
    """
        User authentication proxy that receives the AbstractUser object to work as an intermediare of it to authenticate it giving access or not.
    """
    users_table = False # Users table has been created or not.
    total_users = 0 # Total number of users that were created on database.
    
    def __init__(self, user: User, query_executor: QueryExecutor, cursor:Cursor):
        self.__user = user
        self.__query_executor = query_executor
        self.__cursor = cursor
        try:
            if self.check_user_exists():
                pass
            else:
                self.save_on_db(cursor=self.__cursor, table_name='Users')
        except Exception as e:
            raise Exception(f'Unexpected Error: {e}')
    
    # Real User Actions
    def login(self):
        self.authenticate_user()
        self.__user.login()  

    def register(self):
        self.save_on_db()
        self.__user.register()
    
    def logout(self):
        self.close_session()
        self.__user.logout()
    
    # Proxy Actions
    def check_user_exists(self) -> bool:
        raw_fields = 'username'
        users_list = self.__query_executor.obtain_list_from_db(cursor=self.__cursor, table_name='Users', fields=raw_fields)
        user = [user for user in users_list if user['username'] == self.__user.username]
        if len(user) == 1:
            result = True
        elif len(user) < 1:
            result False
        else:
            raise ValueError('There is a problem related to more than one username that matches with the provided one in the database.')
        return result
    
    @static_method
    def create_users_table(cursor:Cursor):
        if users_table == False:
            TABLE_NAME = 'Users'
            FIELDS = ['id SERIAL PRIMARY KEY', 'username VARCHAR(60) NOT NULL', 'email VARCHAR(120) NOT NULL', 'password VARCHAR(20)', 'is_premium_user BOOLEAN NOT NULL']
            fields_str = ', '.join(FIELDS)
            cursor.create_table(name=TABLE_NAME, fields=fields_str)
            users_table = True
            
    def save_on_db(self, cursor:Cursor, table_name:str) -> bool | str:
        """
            Saves the current User object on the DB as an User row.
        """
        if self.__user.__registered:
            pass
        else:
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
    
    def authenticate_user(self):
        if check_user_exists():
            usernames_list = self.__query_executor.obtain_list_from_db(cursor=self.__cursor, table_name='Users', fields='username')
            passwords_list = self.__query_executor.obtain_list_from_db(cursor=self.__cursor, table_name='Users', fields='password')
            
            try:
                if usernames_list.index(self.__user.username) == passwords_list.index(self.__user.password):
                    self.__user.__authenticated == True:
                else:
                    raise ValueError('Incorrect password.')
            except Exception as e:
                raise Exception(f'Authentication error: {e}')
        else:
            self.__user.__authenticated == False
            raise ValueError('This user does not exist.')
    
    def close_session(self):
        if self.__user.__authenticated == False:
            pass
        else:
            self.__user.__authenticated = False
    
        
class UserProxy(AbstractUser):
    def __init__(self, user:User):
        self.__user = user
    
    def suscribe_to_course(self, course_name:str):
        self.__user.suscribe_to_course(course_name=course_name)