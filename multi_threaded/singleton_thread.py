import threading
from datetime import datetime

class TimerSingleton:
    __instance = None  # Singleton instance
    __lock = threading.Lock()

    def __init__(self):
        raise RuntimeError("Cannot create objects in Singleton")

    @classmethod
    def get_instance(cls):

        if cls.__instance is None:
            with cls.__lock: ############# critical section #################
                if cls.__instance is None:  # Second check (inside lock)
                    cls.__instance = object.__new__(cls)
                    cls.__instance.__start_time = datetime.now()  # Set instance-specific data
            ############################## end of critical section ##########
        return cls.__instance

    def get_time(self):
        return datetime.now() - self.__start_time


def AI():
    # df.append
    pass

# Function to test multithreading with Singleton
def test_singleton():
    instance = TimerSingleton.get_instance()
    print(f"Instance ID: {id(instance)}, Elapsed Time: {instance.get_time()}")

# Creating multiple threads
threads = []
for _ in range(5):
    t = threading.Thread(target=test_singleton)
    threads.append(t)
    t.start()

# Waiting for all threads to complete
for t in threads:
    t.join()

print("All threads finished execution")
