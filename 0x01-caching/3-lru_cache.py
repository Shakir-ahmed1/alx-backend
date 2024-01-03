#!/usr/bin/python3
""" implemntation of cache with LRU caching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching implimentation class """
    def __init__(self):
        """ initialization """
        super().__init__()
        self.stack = []
    
    def put(self, key, item):
        """ add an item to the cache """
        if key is None or item is None:
            return
        else:
            size = len(self.cache_data)
            if size + 1 > BaseCaching.MAX_ITEMS and key not in self.cache_data:
                
                popped = self.stack.pop()
                while popped not in self.cache_data:
                    popped = self.stack.pop()
                del self.cache_data[popped]
                print(f"DISCARD: {popped}")

            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ gets an item from the cache """
        result = self.cache_data.get(key, None)
        if result is None:
            return None
        else:
            self.stack.append(key)
            return result

