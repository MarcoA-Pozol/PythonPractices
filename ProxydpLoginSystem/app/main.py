from . classes import User, UserProxy, AbstractUser, QueryExecutor
import time

# Main thread methods
def execute_authentication_process(user_proxy:AbstractUser):
    try:
        user_proxy.login()
    except Exception as e:
        raise Exception(f'There was an issue during authenticating the user: {e}')

# Instantiation        
query_executor_object = QueryExecutor()
user_object = User(name='ClicheHacker', password='secretkey', email='theaddress@domain.org')
user_proxy_object = UserProxy(user=user_object, query_executor=query_executor_object)

# Programm execution
print('\nInit', init_time = time.time())

execute_authentication_process(user_proxy=user_proxy_object)

print(end_time = time.time() - init_time, 'End\n')


"""
    THIS ENTIRE CONTENT / CODE MUST CHANGE BECAUSE OF CHANGES ON THE CLASSES ANDABSTRACTIONS MADE BY.
"""