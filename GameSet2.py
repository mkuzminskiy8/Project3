from data import Game

class Node(Game):
    def __init__(self, Game):
        self.Game = Game
        self.next = None

class LinkedList(Game):
    def __init__(self, Game):
        self.head = None
        self.score = 1

    #Code borrowed from https://www.datacamp.com/tutorial/python-linked-lists mostly as a refresher on how Python works
    def insert_end(self, Game):
        new = Node(Game)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def get_score(self):
        return self.score

class HashTable(LinkedList):
    def __init__(self, LinkedList):
        self.Table = []
        self.LinkedList = LinkedList

    def hash_function(self, LinkedList):
        scorehash = LinkedList.get_score()

