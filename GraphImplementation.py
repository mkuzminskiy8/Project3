#Michael Buch
from data import Game

#Cesar did me a favor and went ahead and made the node class.
#Each node contains the following: a name data aspect, and the genres the game has.
#Additionally, each game has the ability to reach out and pull games of a similar genre.
#Thus, I can use this ability to help create a minimum spanning tree of games similar to the source game.
#Ergo, It would probably be more useful for me to make the algorithms which will first create a tree of all games similar to this game, and THEN generate a MST from that tree.

class GameInspector(Game):
    pass