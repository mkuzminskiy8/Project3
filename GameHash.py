from data import Game
import math

# Node class holding the game and a pointer to the next node
class Node:
    def __init__(self, game):
        self.game = game
        self.next = None

    def get_game(self):
        return self.game

# Linked List object with a pointer to the head and the Linked Lists similarity score
class LinkedList:
    def __init__(self, score):
        self.head = None
        self.score = score

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

# Hash Table object that will be used to hold Linked Lists of games based on the similarity score
class HashTable:
    def __init__(self):
        self.table = [None] * 5

    def hash_function(self, score):
        return int(math.ceil(score * 4))

    def insert(self, game, score):
        index = self.hash_function(score)
        if self.table[index] is None:
            new_list = LinkedList(score)
            new_list.insert_end(game)
            self.table[index] = new_list

        else:
            if self.table[index].score == score:
                self.table[index].insert_end(game)
            else:
                index = len(self.table) - 1
                new_list = LinkedList(score)
                new_list.insert_end(game)
                self.table.append(new_list)

    def print_out(self):

        for items in self.table:
            if items is not None:
                while items.head is not None:
                    print(items.head.get_game())
                    print()
                    items.head = items.head.next
