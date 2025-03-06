import threading
import time
import random

# Shared list - NOT thread safe
shared_list = []

def add_items(thread_id, count):
    """Add items to the shared list"""
    for i in range(count):
        # Get current length
        current_length = len(shared_list)
        # Simulate some processing time to increase chances of race condition
        time.sleep(0.001)
        # Append a new item
        shared_list.append(f"Thread {thread_id} - Item {i}")
        # Print progress occasionally
        if i % 10 == 0:
            print(f"Thread {thread_id} added item {i}")

def remove_items(thread_id, count):
    """Remove items from the shared list"""
    for i in range(count):
        if shared_list:  # Check if list is not empty
            # Simulate some processing time
            time.sleep(0.002)
            try:
                # Try to remove the last item
                item = shared_list.pop()
                # Print progress occasionally
                if i % 10 == 0:
                    print(f"Thread {thread_id} removed item: {item}")
            except IndexError:
                # This can happen if the list becomes empty between the check and pop
                print(f"Thread {thread_id} - List was empty!")

# Create and start threads
threads = []

# Add two threads that add items
for i in range(2):
    t = threading.Thread(target=add_items, args=(i, 50))
    threads.append(t)
    t.start()

# Add two threads that remove items
for i in range(2):
    t = threading.Thread(target=remove_items, args=(i+2, 40))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Final list length: {len(shared_list)}")
print(f"Expected length: {2*50 - 2*40} = 20")