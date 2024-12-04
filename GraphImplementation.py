#Michael Buch
#Much less of a GraphImplementation Module and much more of a "Generalist functions" module.
from data import Game
import GameHeap
import GameSet

#Cesar did me a favor and went ahead and made the node class.
#Each node contains the following: a name data aspect, and the genres the game has.
#Additionally, each game has the ability to reach out and pull games of a similar genre.
#Thus, I can use this ability to help create a minimum spanning tree of games similar to the source game.
#Ergo, It would probably be more useful for me to make the algorithms which will first create a tree of all games similar to this game, and THEN generate a MST from that tree.


class GameInspector(Game):
    SourceVertex = None

    SimilarGamesToSource = []
    def makeSourceVertex(name):
        SourceVertex = Game(name)

    def getSimilarGamesToSource(self):
        data = game.get_similar_games(9223372036854775807)
        for g in data:
            SimilarGamesToSource.append(easy_read(g))

    def HeapifyGames(arr):
        buildHeap(SimilarGamesToSource, SimilarGamesToSource.size) #should heapify the list. 

    def WorkWithHeap(name):
        makeSourceVertex(name)
        getSimilarGamesToSource()
        HeapifyGames(SimilarGamesToSource)
        printHeap(SimilarGamesToSource, SimilarGamesToSource.size)

    def SetifyGames(arr):
        pass
    
    def WorkWithSet(name):
        makeSourceVertex(name)
        getSimilarGamesToSource()
        SetifyGames(arr)
        printSet() #FIXME: Correct the arguments here.



    
    
