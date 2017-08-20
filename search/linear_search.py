
def linear_search(search_array,element_to_search):
    low = 0
    high = len(search_array) - 1

    while (low <= high):
        if search_array[low] == element_to_search:
            return low
        else:
            low = low + 1

    return -1