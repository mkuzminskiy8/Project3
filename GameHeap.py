from data import Game


# The following code is largely adapated from GeeksForGeek's page on building a heap from an array
# More specifically, it was contributed by one Princi Singh
# The methods I can claim credit for is the extractMax function and the percolate function.
# I also altered his printHeap function.


# arr is the array
# N is the size of the array in case there are more data members
def heapify(SourceGame, arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # If left child is larger than root
    if l < N and SourceGame.similarity_score(arr[l]) > SourceGame.similarity_score(arr[largest]):
        largest = l

    # If right child is larger than largest so far
    if r < N and SourceGame.similarity_score(arr[r]) > SourceGame.similarity_score(arr[largest]):
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(SourceGame, arr, N, largest)  # Recursively heapify the affected sub-tree

    return arr


# Function to build a Max-Heap from the given array


def buildHeap(SourceGame, arr, N):
    # Index of last non-leaf node
    startIdx = N // 2 - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(SourceGame, arr, N, i)
    return arr


# A utility function to print the array
# representation of Heap

def extractMax(SourceGame, arr, N):
    ParentIndex = 0
    PoppedElement = arr[0]
    arr[0] = arr[-1]  # should be N - 1
    # NOTICE: arr = arr[0:-1] is now expressely forbidden. For some reason, and I don't know why,
    # It breaks the code. It might think its instantiating a new array somewhere else in the memory space
    arr.pop(len(arr) - 1)
    Percolate(SourceGame, arr, N - 1, ParentIndex)
    return PoppedElement


# Take the element from end, so long as parent is less than children, swap places with the larger child.
def Percolate(SourceGame, arr, N, ParentIndex):
    LargerChild = None
    LargerChildIndex = None

    if ((2 * ParentIndex) + 2 < N):

        if SourceGame.similarity_score(arr[(2 * ParentIndex) + 1]) > SourceGame.similarity_score(
                arr[(2 * ParentIndex) + 2]):  # .SimScore > arr[(2*ParentIndex)+2].SimScore:
            LargerChild = arr[(2 * ParentIndex) + 1]
            LargerChildIndex = (2 * ParentIndex) + 1
        else:
            LargerChild = arr[(2 * ParentIndex) + 2]
            LargerChildIndex = (2 * ParentIndex) + 2
        if (SourceGame.similarity_score(arr[ParentIndex]) < SourceGame.similarity_score(LargerChild)):
            arr[LargerChildIndex] = arr[ParentIndex]
            arr[ParentIndex] = LargerChild
            Percolate(SourceGame, arr, N, LargerChildIndex)
        else:
            return
    elif (2 * ParentIndex) + 1 < N:
        if SourceGame.similarity_score(arr[ParentIndex]) < SourceGame.similarity_score(arr[(2 * ParentIndex) + 1]):
            LargerChild = arr[(2 * ParentIndex) + 1]
            LargerChildIndex = (2 * ParentIndex) + 1
            arr[(2 * ParentIndex) + 1] = arr[ParentIndex]
            arr[ParentIndex] = LargerChild
        else:
            return


def printHeap(SourceGame, arr, N):
    print("Here's the list of games you should try:")
    while (N != 0):
        CurrentMax = extractMax(SourceGame, arr, N)
        print(CurrentMax)  # .id + " with a similarity score of " + arr[i].SimScore, end=" ")
        print()
        N = N - 1



