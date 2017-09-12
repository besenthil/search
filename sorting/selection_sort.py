def selection_sort(arr):
    count=0
    for i in range(len(arr)-1):
        minimum = arr[i]
        index = i
        for j in range(i+1,len(arr)):
            if arr[j] < minimum :
                minimum = arr[j]
                index = j
            count+=1
        arr[i],arr[index] = arr[index],arr[i]
        #print (arr)
    print (arr,len(arr),count)

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11,-2,10,78,23,79,2,12,12,12,12]
    selection_sort(arr)
