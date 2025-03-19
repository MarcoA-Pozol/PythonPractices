import threading # For multythreading processes
from . endpoints import get_all_customers, get_all_employees

# Multithreading
threads = [] # List of threads

# Threads instantiation
thread1 = threading.Thread(target=asyncio.run(get_all_employees()), args=(None,))
threads.append(thread1)
thread1.start()

thread2 = threading.Thread(target=asyncio.run(get_all_customers()), args=(None,))
threads.append(thread2)
thread2.start()

# Joining all threads (The programm will not continue until all threads have finished their process)
[thread.join() for thread in threads]