''' Stable sorting algorithms maintain the relative order of records with equal keys (i.e. values). 
That is, a sorting algorithm is stable if whenever there are two records R and S with the same key 
and with R appearing before S in the original list, R will appear before S in the sorted list. '''

# quick sort is not stable sort
def quickSort(A, low, high):
    '''Quick short.
    Worst-case performance:
        O(n2)
    Best case performance:
        O(n log n) (simple partition)
        or O(n) (three-way partition and equal keys)
    Average performance	O(n log n)
   
    '''
    if low < high:
        pivot = lomuto_partition(A, low, high)
        quickSort(A, low, pivot - 1)
        quickSort(A, pivot + 1, high)

def lomuto_partition(A, low, high):
    '''Worst-case space complexity:
    O(n) auxiliary (naive)'''
    pivot = A[high]
    i = low
    for j in range(low, high):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    A[i], A[high] = A[high], A[i]
    return i

def hoare_partition(A, low, high):
    ''' Worst-case space complexity:
        O(log n) auxiliary (Hoare 1962)
    '''
    pivot = A[int((high + low) / 2)]
    i = low - 1
    j = high + 1
    if j == len(A):
        j = j - 1
    while A[i] < pivot:
        i = i + 1
    while A[j] > pivot: 
        j = j - 1
    if i >= j:
        return j
    A[i], A[j] = A[j], A[i]

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
