
def binary_search(search_array,element_to_search):

    low = 0
    high = len(search_array)-1


    while element_to_search >= search_array[low] and \
          element_to_search <= search_array[high] and low <= high :

        current_array_index = int((low + high) /2)

        if search_array[current_array_index] == element_to_search:
            return current_array_index

        if search_array[current_array_index] < element_to_search:
            low = current_array_index + 1
        else:
            high = current_array_index-1


    return -1