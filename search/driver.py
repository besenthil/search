from search.interpolation_search import interpolation_search
from search.binary_search import binary_search
from search.linear_search import linear_search

import timeit
import random

def wrapper(func, *args, **kwargs):
    def wrapped_func():
        return func(*args, **kwargs)
    return wrapped_func


if __name__ == "__main__":
    search_array = [pow(x,1) for x in range(0,100000)]
    #search_array = [1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    search_array=sorted(search_array)
    print(search_array)
    element_to_search = 1
    wrapped = wrapper(interpolation_search, search_array,element_to_search)
    print(timeit.timeit(wrapped,number = 1000))
    print(wrapped())

    wrapped = wrapper(binary_search, search_array,element_to_search)
    print(timeit.timeit(wrapped,number = 1000))
    print(wrapped())

    wrapped = wrapper(linear_search, search_array,element_to_search)
    print(timeit.timeit(wrapped,number = 1000))
    print(wrapped())