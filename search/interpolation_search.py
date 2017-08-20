def interpolation_search(search_array,element_to_search):

    low = 0
    high = len(search_array)-1


    while(element_to_search >= search_array[low] and
                      element_to_search <= search_array[high] and low <= high):

        current_array_index = low + \
                              int((element_to_search - search_array[low]) *\
                                  ((high - low)\
                              / (search_array[high] - search_array[low]))\
                )

        if element_to_search == search_array[current_array_index]:
            return current_array_index

        if element_to_search > search_array[current_array_index]:
            low = current_array_index + 1
        else:
            high = current_array_index - 1

    return -1






