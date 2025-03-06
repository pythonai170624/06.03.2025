import multiprocessing
import time

def worker(lock, shared_list, value):
    """Function that modifies a shared resource with a lock."""
    with lock:  # Ensure only one process enters this section at a time
        print(f"Process {multiprocessing.current_process().name} is working...")
        time.sleep(1)  # Simulate some work
        shared_list.append(value)
        print(f"Process {multiprocessing.current_process().name} added {value}")

if __name__ == "__main__":
    lock = multiprocessing.Lock()  # Create a lock
    manager = multiprocessing.Manager()  # Use a manager for shared state
    shared_list = manager.list()  # Shared list

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(lock, shared_list, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()  # Wait for all processes to finish

    print("Final shared list:", list(shared_list))
