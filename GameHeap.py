from data import Game
#The following code is largely adapated from GeeksForGeek's page on building a heap from an array
#More specifically, it was contributed by one Princi Singh
 

 #arr is the array
 #N is the size of the array in case there are more data members 
def heapify(arr, N, i):
 
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
    # If left child is larger than root
    if l < N and arr[l].simScore > arr[largest]:
        largest = l
 
    # If right child is larger than largest so far
    if r < N and arr[r] > arr[largest]:
        largest = r
 
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        # Recursively heapify the affected sub-tree
        heapify(arr, N, largest)
 
# Function to build a Max-Heap from the given array
 
 
def buildHeap(arr, N):
 
    # Index of last non-leaf node
    startIdx = N // 2 - 1
 
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr, N, i)
 
# A utility function to print the array
# representation of Heap

def extractMax(arr, N):
    ParentIndex = 0
    PoppedElement = arr[0]
    arr[0] = arr[N]
    Percolate(arr, N-1, ParentIndex)
    return PoppedElement
 

#Take the element from end, so long as parent is less than children, swap places with the larger child.
def Percolate(arr, N, ParentIndex):
    LargerChild
    LargerChildIndex


    if((2*ParentIndex)+2 < N): 
        if arr[(2*ParentIndex)+1].SimScore > arr[(2*ParentIndex)+2].SimScore:
            LargerChild = arr[(2*ParentIndex)+1]
            LargerChildIndex = (2*ParentIndex)+1
        else:
            LargerChild = arr[(2*ParentIndex)+2]
            LargerChildIndex = (2*ParentIndex)+2
        if(arr[ParentIndex].SimScore < LargerChild.SimScore):
            arr[LargerChildIndex] = arr[ParentIndex]
            arr[ParentIndex] = LargerChild
            Percolate(arr, N, LargerChildIndex)
        else:
            return
    elif (2*ParentIndex)+1 < N:
        if arr[(2*ParentIndex)+1] > arr[ParentIndex]:
            LargerChild = arr[(2*ParentIndex)+1]
            LargerChildIndex = (2*ParentIndex)+1
            arr[(2*ParentIndex)+1] = arr[ParentIndex]
            arr[ParentIndex] = LargerChild
        else:
            return
            
    


 
def printHeap(arr, N):
    print("Here's the list of games you should try:")
    while(N != -1):
        CurrentMax = extractMax(Arr, N)
        print(CurrentMax.id + " with a similarity score of " + arr[i].SimScore, end=" ")
        N = N - 1
 
 
# Driver Code
#if __name__ == '__main__':
 
    # Binary Tree Representation
    # of input array
    #             1
    #           /    \
    #         3        5
    #       /  \     /  \
    #     4      6  13  10
    #    / \    / \
    #   9   8  15 17
#    arr = [1, 3, 5, 4, 6, 13,
#           10, 9, 8, 15, 17]
 
#    N = len(arr)
 
#    buildHeap(arr, N)
#    printHeap(arr, N)
 
    # Final Heap:
    #             17
    #           /    \
    #         15      13
    #        /  \     / \
    #       9     6  5   10
    #      / \   / \
    #     4   8 3   1
 
# This code is contributed by Princi Singh
    
        