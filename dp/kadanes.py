from sys import maxsize


def maxsumsseq(arr):
    max_so_far = -maxsize

    max_ending_here = 0
    sub_arr=[]
    index=0

    for i in range(0,len(arr)):
        max_ending_here = max_ending_here + arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            sub_arr.extend(arr[index:i+1])
            index = i+1

        if max_ending_here < 0:
            max_ending_here=0

    return max_so_far,[x for x in sub_arr]

if __name__ == "__main__":
    print (maxsumsseq([2,3,5,-1,-9,-1,100,50,-4,-200,-1000 ]))
