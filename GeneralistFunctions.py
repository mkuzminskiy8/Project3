# Michael Buch
# Much less of a GraphImplementation Module and much more of a "Generalist functions" module.
import data
import GameHeap
import GameSet


# Cesar did me a favor and went ahead and made the node class.
# Each node contains the following: a name data aspect, and the genres the game has.
# Additionally, each game has the ability to reach out and pull games of a similar genre.
# Thus, I can use this ability to help create a list of games similar to the source game.

def makeSourceVertex(name):
    return data.get_game(name)  # The game object the user searched for


def getSimilarGamesToSource(SourceGame):
    SimilarGamesToSource = []
    jdata = SourceGame.get_similar_games(4) #9223372036854775807
    for g in jdata:
        SimilarGamesToSource.append(data.easy_read(g))
    return SimilarGamesToSource


def WorkWithHeap(name):
    if makeSourceVertex(name) == None:
        print("ERROR: GAME DOES NOT EXIST\n")
        return None
    SourceVertex = makeSourceVertex(name)
    SimilarGamesToSource = getSimilarGamesToSource(SourceVertex)
    SimilarGamesToSource = GameHeap.buildHeap(SourceVertex, SimilarGamesToSource,
                                              len(SimilarGamesToSource))  # should heapify the list.
    GameHeap.printHeap(SourceVertex, SimilarGamesToSource, len(SimilarGamesToSource))

def WorkWithSet(name):
    table = GameSet.HashTable()
    source = makeSourceVertex(name)
    similar_games = getSimilarGamesToSource(source)
    for g in similar_games:
        table.insert(g, source.similarity_score(g))
    table.print_out()




