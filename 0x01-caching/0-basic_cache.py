#!/usr/bin/env python3
"""first module Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """this class contains a {} for in/out data.
    """
    def put(self, key, item):
        """this function will add items to cach.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """this function will return items from cach.
        """
        return self.cache_data.get(key, None)
