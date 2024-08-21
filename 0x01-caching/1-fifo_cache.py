#!/usr/bin/env python3
"""FIFO caching
"""
from base_caching import BaseCaching

from collections import OrderedDict

class FIFOCache(BaseCaching):
    """this class contains a {} for in/out data with fifo algo
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
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """this function will return items from cach.
        """
        return self.cache_data.get(key, None)
