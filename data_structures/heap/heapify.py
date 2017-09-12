from random import randint

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2


    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    #One by one extract elements
    #for i in range(n-1, 0, -1):
    #    arr[i], arr[0] = arr[0], arr[i]   # swap
    #    heapify(arr, i, 0)

def get_minimum(arr):
    return arr[0]

def sort(arr):
    arr1=sorted(arr)
    return arr1

from timeit import timeit

orig_arr = [randint(0,4545) for _ in range(0,100000000)]
arr=list(orig_arr)

print (timeit(lambda:heapSort(arr), number=1))
#print (timeit(lambda:get_minimum(arr), number=1))
arr.append(56656)
print (timeit(lambda:heapSort(arr), number=1))
print (get_minimum(arr))

print (timeit(lambda:sort(orig_arr), number=1))
#for i in range(n):
#    print ("%d" %arr[i]),
