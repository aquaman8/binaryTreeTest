def parent(i):
    return i//2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def swap(A, i1, i2):
    temp = A[i1]
    A[i1] = A[i2]
    A[i2] = temp

def max_heapify(A,i,heapSize):
    l = left(i)
    r = right(i)
    
    largest = i
    if l < heapSize and A[l] > A[i]:
        largest = l
    if r < heapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        #print("swap:" + str(A[i]) + " and " + str(A[largest]) + " left: " + str(A[l]) + " size: " + str(heapSize)  )
        swap(A, i, largest)
        max_heapify(A,largest,heapSize)

def buildMaxHeap(A):
    n = len(A)
    i = n // 2
    
    while i > 0:
        max_heapify(A,i,n)
        i=i-1

def heap_sort(A):
    buildMaxHeap(A)
    print(A)
    currentHeapIndex = i = len(A)-1
    
    while i > 0:
        swap(A,1,i)
        max_heapify(A,1,currentHeapIndex)
        currentHeapIndex -= 1
        print(A)
        i = i-1

def heap_maxium(A):
    return A[1]

def heap_extract_max(A, heapSize):
    max = A[1]
    A[1] = A[heapSize]
    heapSize = heapSize - 1
    max_heapify(A,1,heapSize)
    return max
    
def heap_increase_key(A,i,key):
    if key < A[i]:
        print("new key is smaller than current key")
        return
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        swap(A,i,parent(i))
        i = parent(i)

def max_heap_insert(A,key,currentHeapIndex):
    currentHeapIndex = currentHeapIndex+1
    A[currentHeapIndex] = -9999999
    heap_increase_key(A,currentHeapIndex, key)



def d_ary_parent(i,d):
    return (i-2)//d + 1

def d_ary_increase_key(A,i,key,d):
    if key < A[i]:
        print("new key is smaller than current key")
        return
    A[i] = key
    while i > 1 and A[d_ary_parent(i,d)] < A[i]:
        swap(A,i,d_ary_parent(i,d))
        i = parent(i)

def d_ary_insert(A,key,currentHeapIndex,d):
    currentHeapIndex = currentHeapIndex + 1
    A[currentHeapIndex] = -999999999
    d_ary_increase_key(A,key,currentHeapIndex,d)
    

A = [9999,4,1,3,2,16,9,10,14,8,7]
heap_sort(A)
print(A)

    