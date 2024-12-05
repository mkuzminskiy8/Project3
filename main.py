
import time
import GeneralistFunctions
if __name__=='__main__':
    infinitum = 1
    while infinitum != 0:
        GameToSelect = input("What game have you just finished? Alternatively, type \"DoneForNow\" to end: ")
        if GameToSelect == "DoneForNow":
            break
        else:
            Num_Games = int(input("How many game recommendations do you want? " ))
            Choice = input("How do we want to do this? you may type either \"heap\" or \"hash table\": ")
            print()
            TimeStart = time.perf_counter()
            #Insert code here
            if Choice == "heap":
                if GeneralistFunctions.WorkWithHeap(GameToSelect, Num_Games) != None:
                    TimeEnd = time.perf_counter()
                    print(f"That took {round(TimeEnd - TimeStart, 2)} long with your decision to go with {Choice}")
            elif Choice == "hash table":
                if GeneralistFunctions.WorkWithSet(GameToSelect, Num_Games) != None:
                    TimeEnd = time.perf_counter()
                    print(f"That took {round(TimeEnd - TimeStart, 2)} long with your decision to go with {Choice}")




