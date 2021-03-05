def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def swap(A, i1, i2):
    temp = A[i1]
    A[i1] = A[i2]
    A[i2] = temp

def min_heapify(A,i,heapSize):
    l = left(i)
    r = right(i)
    
    smallest = i
    if l < heapSize and A[l] > A[i]:
        smallest = l
    if r < heapSize and A[r] > A[smallest]:
        smallest = r
    if smallest != i:
        swap(A, i, smallest)
        min_heapify(A,smallest,heapSize)

def buildMaxHeap(A):
    n = len(A)
    i = n // 2
    while i > 0:
        min_heapify(A,i,n)
        i=i-1

def heap_sort(A):
    buildMaxHeap(A)
    print(A)
    currentHeapIndex = i = len(A)-1
    
    while i > 0:
        swap(A,1,i)
        min_heapify(A,1,currentHeapIndex)
        currentHeapIndex -= 1
        print(A)
        i = i-1

def heap_minimum(A):
    return A[1]

def heap_extract_min(A, heapSize):
    if heapSize < 1:
        return
    min = A[1]
    A[1] = A[heapSize]
    heapSize = heapSize - 1
    min_heapify(A,1,heapSize)
    return min
    
def heap_decrease_key(A,i,key):
    if key > A[i]:
        print("new key is larger than current key")
        return
    A[i] = key
    while i > 1 and A[parent(i)] > A[i]:
        swap(A,i,parent(i))
        i = parent(i)

def min_heap_insert(A,key,heapSize):
    heapSize = heapSize+1
    A[heapSize] = 99999999
    heap_decrease_key(A,heapSize, key)


def d_ary_child(i,j,d):
    return d*i - d + j + 1

def d_ary_max_heapify(A, i, heapSize, d):
    largest = i
    # pick largest child if possible:
    j = 1
    while j >= d:
        if d_ary_child(i,j,d) < heapSize and A[d_ary_child(i,j,d)] > A[largest]:
            largest = d_ary_child(i,j,d)
    if largest != i:
        swap(A,i,largest)
        d_ary_max_heapify(A,largest,heapSize,d)
    return


def d_ary_extract_max(A, heapSize, d):
    max = A[1]
    A[1] = A[heapSize]
    heapSize = heapSize - 1
    d_ary_max_heapify(A,1,heapSize,d)
    return max

    

A = [9999,4,1,3,2,16,9,10,14,8,7]
heap_sort(A)
print(A)

    