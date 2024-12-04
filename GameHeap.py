#from data import Game
#The following code is largely adapated from GeeksForGeek's page on building a heap from an array
#More specifically, it was contributed by one Princi Singh
#The methods I can claim credit for is the extractMax function and the percolate function.
#I also altered his printHeap function. 
 

#arr is the array
#N is the size of the array in case there are more data members 
def heapify(arr, N, i):
 
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
    # If left child is larger than root
    if l < N and arr[l] > arr[largest]:
        largest = l
 
    # If right child is larger than largest so far
    if r < N and arr[r] > arr[largest]:
        largest = r
 
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)# Recursively heapify the affected sub-tree
 
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
    arr[0] = arr[-1] #should be N - 1
    #NOTICE: arr = arr[0:-1] is now expressely forbidden. For some reason, and I don't know why, 
    #It breaks the code. 
    arr.pop(len(arr)-1)
    Percolate(arr, N-1, ParentIndex)
    return PoppedElement
 

#Take the element from end, so long as parent is less than children, swap places with the larger child.
def Percolate(arr, N, ParentIndex):
    
    
    
    LargerChild = None
    LargerChildIndex = None
    #print("This is the array in view of the program here:")
    
    
    #FIXME: 4 and 3 are gone. 
    if((2*ParentIndex)+2 < N): 
        #print("The Right Child is in bounds path:")
        if arr[(2*ParentIndex)+1] > arr[(2*ParentIndex)+2]: #.SimScore > arr[(2*ParentIndex)+2].SimScore:
            #print("Larger child is now set to", arr[(2*ParentIndex)+1], ", the left child.")
            LargerChild = arr[(2*ParentIndex)+1]
            LargerChildIndex = (2*ParentIndex)+1
        else:
            #print("Larger child is now set to", arr[(2*ParentIndex)+2], ", the right child")
            LargerChild = arr[(2*ParentIndex)+2]
            LargerChildIndex = (2*ParentIndex)+2
            #print("The Right Child is in bounds path:")
        if(arr[ParentIndex] < LargerChild): #.SimScore < LargerChild.SimScore):
            #print(arr[ParentIndex], "is found to be less than", LargerChild, ", so we're swapping", arr[ParentIndex], "with", LargerChild)
            arr[LargerChildIndex] = arr[ParentIndex]
            arr[ParentIndex] = LargerChild
            Percolate(arr, N, LargerChildIndex)
        else:
            #print(arr[ParentIndex], "was not found to be less than", LargerChild, ", so no swaps shall occur")
            return
    elif (2*ParentIndex)+1 < N:
        #print("The Left Child is in bounds but not the Right Child path:")
        if  arr[ParentIndex] < arr[(2*ParentIndex)+1]:
            #print(arr[ParentIndex], "is found to be less than the Left Child,", arr[(2*ParentIndex)+1], ", so we're swapping ", arr[ParentIndex], "with", arr[(2*ParentIndex)+1])
            LargerChild = arr[(2*ParentIndex)+1]
            LargerChildIndex = (2*ParentIndex)+1
            arr[(2*ParentIndex)+1] = arr[ParentIndex]
            arr[ParentIndex] = LargerChild
        else:
            #print("The left child was not found to be larger than the parent. No swaps shall occur.")
            return
    #print("Neither the left child nor the right child is in bounds, so this is a leaf node. This is the heap after all this")
    #for i in range(N):
    #    print(arr[i], end=" ")
    #print()
    


 
def printHeap(arr, N):
    print("Here's the list of games you should try:")
    while(N != 0):
        CurrentMax = extractMax(arr, N)
        print(CurrentMax)#.id + " with a similarity score of " + arr[i].SimScore, end=" ")
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
    #arr = [1, 3, 5, 4, 6, 13,
    #       10, 9, 8, 15, 17]
 
    #N = len(arr)
    
    
    
 
    #buildHeap(arr, N)
    #printHeap(arr, N)
 
    # Final Heap:
    #             17
    #           /    \
    #         15      13
    #        /  \     / \
    #       9     6  5   10
    #      / \   / \
    #     4   8 3   1
 
# This code is contributed by Princi Singh
    
        



