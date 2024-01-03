#!/usr/bin/python3
""" Base Caching with unlimited items """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ a class with unlimited caches """
    def __init__(self):
        """ initialization """
        super().__init__()

    def put(self, key, item):
        """ add an item to the cache """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ get an item from the cache """
        result = self.cache_data.get(key, None)
        if result is None:
            return None
        else:
            return result
