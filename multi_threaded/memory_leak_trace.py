'''
A comprehensive example to monitor memory usage in a program:
'''

import gc
import tracemalloc
import sys

print('=' * 100)
# Start tracking memory allocations
tracemalloc.start()


def allocate_memory():
    # Create some objects
    lists = []
    for i in range(100):
        lists.append([j for j in range(10000)])

    # Take a snapshot after allocation
    snapshot1 = tracemalloc.take_snapshot()
    print(f"Memory blocks after allocation: {snapshot1.statistics('lineno')[0]}")

    # Delete some objects
    for i in range(50):
        del lists[0]

    # Force garbage collection
    gc.collect()

    # Take another snapshot
    snapshot2 = tracemalloc.take_snapshot()
    print(f"Memory blocks after partial deallocation: {snapshot2.statistics('lineno')[0]}")

    # Compare snapshots
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    print("Memory usage changes:")
    for stat in top_stats[:3]:
        print(stat)


# Run the test
allocate_memory()

# Stop tracking
tracemalloc.stop()