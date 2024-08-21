#!/usr/bin/env python3
"""LFU Caching
"""
from base_caching import BaseCaching

from collections import OrderedDict


class LFUCache(BaseCaching):
    """this class contains a {} for in/out data with LFU algo.
    """
    def __init__(self):
        """init function.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def were_db(self, dt_value):
        """function to storing the data using LFU algo.
        """
        loc = []
        frequency = 0
        pre = 0
        nw = 0
        for x, search_loc in enumerate(self.keys_freq):
            if search_loc[0] == dt_value:
                frequency = search_loc[1] + 1
                pre = x
                break
            elif len(loc) == 0:
                loc.append(x)
            elif search_loc[1] < self.keys_freq[loc[-1]][1]:
                loc.append(x)
        loc.reverse()
        for pos in loc:
            if self.keys_freq[pos][1] > frequency:
                break
            nw = pos
        self.keys_freq.pop(pre)
        self.keys_freq.insert(nw, [dt_value, frequency])

    def put(self, key, item):
        """this function will add items to cach.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for x, search_loc in enumerate(self.keys_freq):
                if search_loc[1] == 0:
                    ins_index = x
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.were_db(key)

    def get(self, key):
        """this function will return items from cach.
        """
        if key is not None and key in self.cache_data:
            self.were_db(key)
        return self.cache_data.get(key, None)
