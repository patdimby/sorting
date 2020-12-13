def countSort(input, k):
    '''Linear short.
        Worst-case performance O(n+k), where k is 
        the range of the non-negative key values.
        Worst-case space complexity	{\displaystyle O(n+k)}O(n+k)
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
