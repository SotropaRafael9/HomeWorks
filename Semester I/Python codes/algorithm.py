from random import random


def Generate_Numbers_Random(ListLength):
    # Șotropa Rafael
    LastElement = int(0)
    for i in range (0, ListLength-1):
        LastElement = random.randint(LastElement,100)
        list.append(LastElement)
    return list
def Exponential_Search(list, LeftBound, RightBound, x):
    index = 0
    if RightBound > LeftBound and list[LeftBound] == x:
        return LeftBound
    else:
        if LeftBound < RightBound and list[RightBound] == x:
            pass

def BinariSort(Left, Right, x, List):
    Middle = (Right + Left) / 2
    if x == List[Middle]:
        return Middle
    else:
        if x < list[Middle]:
            BinariSort(Left, Middle - 1, x, List)
    BinariSort(Left, Middle + 1, x, List)







    
    


