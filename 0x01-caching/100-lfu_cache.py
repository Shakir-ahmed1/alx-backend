#!/usr/bin/python3
""" LFU caching implementation """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """ initialization """
        super().__init__()
        self.queue = []
        self.usage = []

    def put(self, key, item):
        """ add an item to the cache """
        if key is None or item is None:
            return
        else:
            size = len(self.cache_data)
            count = 0
            if size + 1 > BaseCaching.MAX_ITEMS and key not in self.cache_data:
                min_freq = min(self.usage)
                least_freq_index = self.usage.index(min_freq)
                popped = self.queue.pop(least_freq_index)
                self.usage.pop(least_freq_index)
                del self.cache_data[popped]
                print(f"DISCARD: {popped}")
                count += 1
            if key in self.queue:
                index = self.queue.index(key)
                count = 1 + self.usage.pop(index)
                self.queue.remove(key)
            self.queue.append(key)
            self.usage.append(count)
            self.cache_data[key] = item

    def get(self, key):
        """ get an item from cache """
        result = self.cache_data.get(key, None)
        if result is None:
            return None
        else:
            count = 1
            if key in self.queue:
                index = self.queue.index(key)
                count = 1 + self.usage.pop(index)

                self.queue.remove(key)
            self.queue.append(key)
            self.usage.append(count)
            return result
