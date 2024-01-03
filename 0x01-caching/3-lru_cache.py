#!/usr/bin/python3
""" implemntation of cache with LRU caching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching implimentation class """
    def __init__(self):
        """ initialization """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ add an item to the cache """
        if key is None or item is None:
            return
        else:
            size = len(self.cache_data)
            if size + 1 > BaseCaching.MAX_ITEMS and key not in self.cache_data:
                popped = self.queue.pop(0)
                while popped not in self.cache_data:
                    popped = self.queue.pop(0)
                del self.cache_data[popped]
                print(f"DISCARD: {popped}")
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get an item from the cache """
        result = self.cache_data.get(key, None)
        if result is None:
            return None
        else:
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            return result
