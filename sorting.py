#!/usr/bin/python
# -*- coding: utf-8 -*-

# quick sort is not stable sort

''' Stable sorting algorithms maintain the relative order of records with equal keys (i.e. values). 
That is, a sorting algorithm is stable if whenever there are two records R and S with the same key 
and with R appearing before S in the original list, R will appear before S in the sorted list. '''


def quickSort(A, low, high):
    '''Quick short.
    Worst-case performance:
        O(n2)
    Best case performance:
        O(n log n) (simple partition)
        or O(n) (three-way partition and equal keys)
    Average performance....O(n log n)
   
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
            (A[i], A[j]) = (A[j], A[i])
            i = i + 1
    (A[i], A[high]) = (A[high], A[i])
    return i


def hoare_partition(A, low, high):
    ''' Worst-case space complexity:
        O(log n) auxiliary (Hoare 1962)
    '''

    pivot = A[int((high + low) / 2)]
    i = low - 1
    j = high + 1
    if j >= len(A):
        j = len(A) - 1
    while A[i] < pivot:
        i = i + 1
    while A[j] > pivot and j > 0:
        j = j - 1
    if i >= j:
        return j
    (A[i], A[j]) = (A[j], A[i])


def countSort(input, k):
    '''Linear short member.
    Worst-case performance O(n+k), where k is the range of the non-negative key values.
    Worst-case space complexity O(n+k).
    '''

    # k must be greater than max value of array input
    # and greater than length of array

    if k < max([len(input), max(input)]):
        k = max([len(input), max(input)]) + 1

    # set arrays

    count = [0] * (k + 1)
    output = [0] * len(input)

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
        (count[i], total) = (total, count[i] + total)

    # it loops over the items again in the third loop,
    # moving each item into its sorted position in the output array.

    for x in input:
        output[count[x]] = x
        count[x] += 1
    return output


def insertionSort(A):
    '''Insertion sort.
    Worst-case performance:
        O(n2) comparisons and swaps
    Best-case performance:
        O(n) comparisons, O(1) swaps
    Average performance:
        O(n2) comparisons and swaps
    Worst-case space complexity:
        O(n) total, O(1) auxiliary    '''

    i = 0
    while i < len(A):
        j = i
        while j > 0 and A[j] < A[j - 1]:

            # if value as inferior to precedent, swap element

            (A[j], A[j - 1]) = (A[j - 1], A[j])
            j = j - 1
        i = i + 1
    return A


def mergeSort(arr):
    '''
Worst-case performance....O(nlog n)
Best-case performance....O(nlog n) typical, O(n) natural variant
Average performance....Theta (n\log n)
Worst-case space complexity O(n) total with O(n) auxiliary
    
    '''

    if len(arr) > 1:

         # Finding the mid of the array

        mid = len(arr) // 2

        # Dividing the array elements

        lefthalf = arr[:mid]

        # into 2 halves

        righthalf = arr[mid:]

        # Sorting the first half

        mergeSort(lefthalf)

        # Sorting the second half

        mergeSort(righthalf)
        i = j = k = 0

        # Copy data to temp arrays lefthalf[] and righthalf[]

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        # Checking if any element was left

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1


def selectionSort(a):
    '''Selection sort.
    Worst-case performance:
        O(n2) comparisons, O(n) swaps    
    Best-case performance:
        O(n2) comparisons, O(1) swaps
    Average performance:
        O(n2)  comparisons, O(n) swaps    
    Worst-case space complexity:
        O(1) auxiliary    '''

    # a[0] to a[aLength-1] is the array to sort

    (i, j) = (0, 0)
    aLength = len(a)  # initialise to a's length

    # advance the position through the entire array
    #  (could do i < aLength-1 because single element is also min element)

    for i in range(aLength - 1):

        # find the min element in the unsorted a[i .. aLength-1]
        # assume the min is the first element.

        jMin = i

        # test against elements after i to find the smallest

        for j in (i + 1, aLength - 1):

        #   if this element is less, then it is the new minimum

            if a[j] < a[jMin]:

                # found new minimum; remember its index.

                jMin = j
        if jMin != i:
            (a[i], a[jMin]) = (a[jMin], a[i])
    return a
