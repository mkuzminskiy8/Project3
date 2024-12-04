
import time
import GeneralistFunctions
if __name__=='__main__':
    infinitum = 1
    while infinitum != 0:
        GameToSelect = input("What game have you just finished? Alternatively, type \"DoneForNow\" to end: ")
        if GameToSelect == "DoneForNow":
            break
        else:
            Choice = input("How do we want to do this? you may type either \"heap\" or \"set\"")
            TimeStart = time.time()
            #Insert code here
            if Choice == "heap":
                GraphImplementation.WorkWithHeap(GameToSelect)
            elif Choice == "set":
                GraphImplementation.WorkWithSet(GameToSelect)

            TimeEnd = time.time()

            print("That took " + (TimeEnd - TimeStart) + " long with your decision to go with " + Choice) 
            pass #when ready, make this game object by searching for the game in the data base. 
