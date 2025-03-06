
'''
using concurrent collection
'''
import threading
import queue
import time

# Thread-safe queue
q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced {i}")
        time.sleep(0.1)

def consumer():
    while not q.empty():
        item = q.get()
        print(f"Consumed {item}")
        time.sleep(0.2)
        q.task_done()

# Creating producer and consumer threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

# Starting threads
t1.start()
time.sleep(0.5)  # Allow producer to add some items before consumer starts
t2.start()

# Waiting for threads to complete
t1.join()
t2.join()