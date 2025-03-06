import threading
import time

# Shared collection (list)
shared_list = []
lock = threading.Lock()

def append_numbers():
    for i in range(500):
        with lock:
            shared_list.append(i)
        time.sleep(0.001)  # Simulating some processing time

# Creating two threads
t1 = threading.Thread(target=append_numbers)
t2 = threading.Thread(target=append_numbers)

# Starting the threads
t1.start()
t2.start()

# Waiting for both threads to finish
t1.join()
t2.join()

# Printing the final list
print("Final shared_list:", shared_list)