#!/usr/bin/env python3
"""LIFO Caching
"""
from base_caching import BaseCaching

from collections import OrderedDict

class LIFOCache(BaseCaching):
    """this class contains a {} for in/out data with lifo algo
    """
    def __init__(self):
        """init function.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """this function will add items to cach.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """this function will return items from cach.
        """
        return self.cache_data.get(key, None)
