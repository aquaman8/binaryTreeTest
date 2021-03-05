class BinaryHeap:
    def __init__(self):
        self.heapArr = []
        self.currentIndex = 0

    def swap(self,i1,i2):
        tmp = self.heapArr[i1]
        self.heapArr[i1] = self.heapArr[i2]
        self.heapArr[i2] = tmp

    def reHeapUp(self, i):
        inserted_value = self.heapArr[i]
        index_of_parents = i//2
        index_of_child = i
        while index_of_child != 0:
            if self.heapArr[index_of_parents] > self.heapArr[index_of_child]:
                if inserted_value == 1:
                    print(str(self.heapArr[index_of_parents]) + " and " + str(self.heapArr[index_of_child]))
                self.swap(index_of_parents, index_of_child)
            index_of_parents = index_of_parents//2
            index_of_child = index_of_child//2
            
    def insert(self,x):
        self.heapArr.append(x)
        if self.currentIndex != 0:
            self.reHeapUp(self.currentIndex)
        self.currentIndex = self.currentIndex+1


    def print(self):
        print(self.heapArr)        


# main
b = BinaryHeap()       
b.insert(9)
b.insert(3)
b.insert(22)
b.insert(1)


b.print()