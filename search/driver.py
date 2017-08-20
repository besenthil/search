from search.interpolation_search import interpolation_search
import timeit
from datetime import datetime

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == "__main__":
    search_array = [x for x in range(0,100000000)]
    element_to_search = 675733
    wrapped = wrapper(interpolation_search, search_array,element_to_search)
    print(timeit.timeit(wrapped,number = 1000))
    print(wrapped())