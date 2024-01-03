#!/usr/bin/python3
""" implemntation of cache with MRU caching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching implimentation class """
    def __init__(self):
        """ initialization """
        super().__init__()
        self.keys_holder = []
        self.usage = []

    def put(self, key, item):
        """ add an item to the cache """
        if key is None or item is None:
            return
        else:
            size = len(self.cache_data)
            if size + 1 > BaseCaching.MAX_ITEMS and key not in self.cache_data:
                evaluate = list(map(lambda x: x + self.usage[x], range(size)))
                reversed_evaluate = evaluate[::-1]
                reversed_index = reversed_evaluate.index(max(evaluate))
                pop_idx = len(evaluate) - reversed_index - 1
                popped = self.keys_holder.pop(pop_idx)
                self.usage.pop(pop_idx)
                del self.cache_data[popped]
                print(f"DISCARD: {popped}")
            if key in self.keys_holder:
                rm_idx = self.keys_holder.index(key)
                self.keys_holder.pop(rm_idx)
                self.usage.pop(rm_idx)
            self.keys_holder.append(key)
            self.usage.append(0)
            self.cache_data[key] = item

    def get(self, key):
        """ get an item from the cache """
        result = self.cache_data.get(key, None)
        if result is None:
            return None
        else:
            self.usage[self.keys_holder.index(key)] += self.MAX_ITEMS - 1
            return result
