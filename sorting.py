''' Stable sorting algorithms maintain the relative order of records with equal keys (i.e. values). 
That is, a sorting algorithm is stable if whenever there are two records R and S with the same key 
and with R appearing before S in the original list, R will appear before S in the sorted list. '''


def countSort(input, k):
    '''Linear short member.
    Worst-case performance O(n+k), where k is the range of the non-negative key values.
    Worst-case space complexity O(n+k).
    '''
    # k must be greater than max value of array input
    # and greater than length of array
    count = [0] * (k + 1)
    key = output = [0] * len(input)
    # this routine count elements in array
    # element count begin at minimum of elements
    # order by ascending, like a set.
    for x in input:
        count[x] += 1
    total = 0
    #  it then performs a prefix sum computation on count to determine, 
    # for each key, the position range where the items having that key 
    # should be placed in; i.e. items of key i should be placed starting
    # in position count[i]. 
    for i in range(k):
        count[i], total = total, count[i] + total
    # it loops over the items again in the third loop, 
    # moving each item into its sorted position in the output array.
    for x in input:
        output[count[x]] = x
        count[x] += 1
    return output
