import weakref


class Cache:
    def __init__(self):
        self._cache = {}

    def add_item(self, key, value):
        self._cache[key] = value

    def get_item(self, key):
        return self._cache.get(key)


# Problem: This cache retains all objects, causing a memory leak
cache = Cache()


class BigData:
    def __init__(self, name, data):
        self.name = name
        self.data = data


# Create and cache a lot of big objects
for i in range(1000):
    big_obj = BigData(f"data{i}", [0] * 100000)
    cache.add_item(f"key{i}", big_obj)


del big_obj
################# .............

#### solution


# Solution: Use a weak reference dictionary
class ImprovedCache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def add_item(self, key, value):
        self._cache[key] = value

    def get_item(self, key):
        return self._cache.get(key)


# Now objects will be garbage collected when no other references exist
better_cache = ImprovedCache()

for i in range(1000):
    big_obj = BigData(f"data{i}", [0] * 100000)
    better_cache.add_item(f"key{i}", big_obj)
    # When big_obj goes out of scope, it can be garbage collected

del big_obj