#!/usr/bin/env python3
"""MRU Caching
"""
from base_caching import BaseCaching

from collections import OrderedDict


class MRUCache(BaseCaching):
    """this class contains a {} for in/out data with MRU algo.
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
                dt_value, _ = self.cache_data.popitem(False)
                print("DISCARD:", dt_value)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """this function will return items from cach.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
