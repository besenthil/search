import collections
from PIL import Image

from datetime import datetime

class LRUCache(object):
    def __init__(self,capacity):

        if capacity <=0 :
            return Exception("Capacity cant be less than or equal to 0")

        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def set_cache(self,key,value):
        # if cache exceeds capacity threshold
        # and insert the new key
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


    def get_cache(self,key):
        try:
            # If item is found remove from queue and add it at the right
            value = self.cache.pop(key)
            self.cache[key] = value
        except KeyError as e:
            # If item not found, return -1
            value = -1

        return value


if __name__ == "__main__":

    lru = LRUCache(10)
    for i in range(1,7):
        print (datetime.now())
        lru.set_cache(i,Image.open('/home/senthil/Pictures/'+str(i)+'.jpg'))
        print (datetime.now())
        #print(lru.cache)

    for i in range(1,8):
        image = lru.get_cache(i)
        if image != -1:
            #print (datetime.now())
            image.show()
            #print (datetime.now())
        else:
            #print ("miss")
            #print (datetime.now())
            lru.set_cache(i,Image.open('/home/senthil/Pictures/'+str(i)+'.jpg'))
            image = lru.get_cache(i)
            image.show()
            #print (datetime.now())
