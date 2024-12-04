#Michael Buch
from data import Game
#Alternatively, I'll be using an array and each element shall be its own linked list
#This means that each element's index, through it's hashing, will be its similarity score
#This way, the element can, in its own way, be psuedo-ordered.
#I'm considering this because I have to do the retrieve these 


#Notice - the similarity score is better the closer it is to 1
#In doing so, its better to go BACKWARDS through the Array and forwards through the 


#TODO: Make a node class which is just the Game objects and have them point to another GameObject

class Nodes(Game):
    pass

#TODO: Keep pointers to the head and the tail.
class LinkedList:
    pass

class GameSetMATCH:
    TheHashTable = []

    def HashThat(SimScore):
        #The problem here is that somehow I have to make it so that 0.6 does not map to the same bucket as 0.7. 
        #I could multiply by 10 which would boost these to 6 and 7 respectively, but what about 0.73
        #Here's the thing. If I am using seperate chaining, which I am, doing the times 10 thing above, I can map these games *relative* (not exactly) to their similarity in the hash table.
        #That is 0.001 x 10 = 0.01 and 0.002 x 10 will both map to bucket 0 at arr[0]
        return int(SimScore * 10)
    
    def reduce(HashedSimScore):
        return HashedSimScore % TheHashTable.size()
    
    




