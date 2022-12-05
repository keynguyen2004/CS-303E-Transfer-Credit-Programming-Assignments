"""
Leetcode Problem #: 146
Leetcode Problem: LRU Cache
Difficulty: Medium

we can remove an item from the dictionary, and re-add 
it whenever we use the 'get' function and python will 
keep it ordered exactly as we needed. Likewise when we 
need to delete LRU from the dictionary, we can delete 
the first item and don't even need to know or keep track 
of the keys to delete the first item.
"""


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.arr = []


    def get(self, key):
        if key in self.cache:
            self.arr.remove(key)
            self.arr.append(key)
            return self.cache[key]
        else:
            return -1


    def put(self, key, value):
        if key not in self.cache:
            if len(self.arr) >= self.capacity:
                val = self.arr.pop(0)
                self.cache.pop(val)
                self.arr.append(key)
                self.cache[key] = value
            else:
                self.arr.append(key)
                self.cache[key] = value
        else:
            self.arr.remove(key)
            self.arr.append(key)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)