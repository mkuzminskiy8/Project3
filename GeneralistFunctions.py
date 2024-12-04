#Michael Buch
#Much less of a GraphImplementation Module and much more of a "Generalist functions" module.
import data
import GameHeap
import GameSet

#Cesar did me a favor and went ahead and made the node class.
#Each node contains the following: a name data aspect, and the genres the game has.
#Additionally, each game has the ability to reach out and pull games of a similar genre.
#Thus, I can use this ability to help create a minimum spanning tree of games similar to the source game.
#Ergo, It would probably be more useful for me to make the algorithms which will first create a tree of all games similar to this game, and THEN generate a MST from that tree.


def makeSourceVertex(name):
    return data.get_game(name) #The game object the user searched for

def getSimilarGamesToSource(self, SourceGame):
    SimilarGamesToSource = []
    data = SourceGame.get_similar_games(9223372036854775807)
    for g in data:
        SimilarGamesToSource.append(data.easy_read(g))
    return SimilarGamesToSource

def WorkWithHeap(name):
    SourceVertex = GeneralistFunctions.makeSourceVertex(name)
    SimilarGamesToSource = GameHeap.getSimilarGamesToSource(SourceVertex)
    SimilarGamesToSource = GameHeap.buildHeap(SourceVertex, SimilarGamesToSource, len(SimilarGamesToSource)) #should heapify the list. 
    GameHeap.printHeap(SimilarGamesToSource, SimilarGamesToSource.size)

#def SetifyGames(arr):
    #pass
    
#def WorkWithSet(name):
    #makeSourceVertex(name)
    #getSimilarGamesToSource()
    #SetifyGames(arr)
    #printSet() #FIXME: Correct the arguments here.



    
    
