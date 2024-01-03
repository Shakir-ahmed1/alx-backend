#!/usr/bin/python3
""" implemntation of cache with FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """ a FIFO caching implemenatation class """
    def __init__(self):
        """ Initailization """
        super().__init__()
        self.keys_holder = []
    
    def put(self, key, item):
        """ add an item to the cache """
        if key is None or item is None:
            return
        else:
            self.keys_holder.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped = self.keys_holder.pop(0)
                del self.cache_data[popped]
                print(f"DISCARD: {popped}")

    def get(self, key):
        """ get an item with a key """
        result = self.cache_data.get(key, None)
        if result is None:
            return None
        else:
            return result
