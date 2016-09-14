import random

# Define heapBoard
def HeapBoard():
    heap_choice = [3,5,7]
    select_choice = [9,11,13]
    heap_chose = random.choice(heap_choice)
    heapBoard = []
    for i in range(heap_chose):
        heapBoard.append(random.choice(select_choice)) # [9,9,11]
    return heapBoard  # heapBoard [9,9,11]

# Make sure the input is legal
def InputCheck():
    print('Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X ')
    userType = input()
    userInput = userType.split()
    while (len(userInput) != 2):
        userInput = ErrorInfo()
    heapMinus = userInput[0]
    heapFrom = userInput[1]
    return heapMinus, heapFrom

def InputToInt(s):
    try:
        int(s)
        if (int(s) > 0):
            return True
        return False
    except ValueError:
        return False

def ErrorInfo():
    print('Player human that is an invalid move, try again')
    print("Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X ")
    userType = input()
    userInput = userType.split()
    return userInput

# Determine who is the first Player
def FirstPlayer():
    player = ['human', 'machine']
    if (random.choice(player) == 'human'):
        # first player is human
        return False
    else:
        return True

# Define human playing
def humanPlay(heapFrom, heapMinus, heapBoard):
    heapBoard[heapFrom - 1] -= heapMinus
    return heapBoard

# Define Machine playing, need more work here
def machinePlay(heapBoard):
    heapWhich = random.randint(1, heapNums) - 1
    pointLeft = heapBoard[heapWhich]
    # in case the number of elements of head is zero
    while (pointLeft == 0):
        heapWhich = random.randint(1, heapNums) - 1
        pointLeft = heapBoard[heapWhich]
    heapMinus = random.randint(1, pointLeft)
    heapBoard[heapWhich] = pointLeft - heapMinus
    return heapBoard, heapWhich, heapMinus


# Human Action
def HumanAction():
    (heapMinus, heapFrom) = InputCheck()
    while (InputToInt(heapFrom) == False or InputToInt(heapMinus) == False):
        print('Player human that is an invalid move, try again')
        heapMinus, heapFrom = InputCheck()
    heapFrom = int(heapFrom)
    heapMinus = int(heapMinus)
    while (heapMinus == 0 or heapFrom > heapNums or heapFrom < 1 or heapMinus > heapBoard[heapFrom - 1]):
        print('Player human that is an invalid move, try again')
        heapMinus, heapFrom = InputCheck()
        while (InputToInt(heapFrom) == False or InputToInt(heapMinus) == False):
            print('Player human that is an invalid move, try again')
            heapMinus, heapFrom = InputCheck()
        heapFrom = int(heapFrom)
        heapMinus = int(heapMinus)
    return heapFrom, heapMinus


# Machine Play First
def MachineFirst(heapBoard):
    while (True):
        result = machinePlay(heapBoard)
        heapBoard = result[0]
        heapWhich = result[1]
        heapMinus = result[2]
        print('Player computer took', heapMinus, 'objects from heap', (heapWhich + 1))
        printOneLine(heapBoard)
        if (all(v == 0 for v in heapBoard) == True):
            print('Player computer has won')
            break
        heapFrom, heapMinus = HumanAction()
        heapBoard = humanPlay(heapFrom, heapMinus, heapBoard)
        printOneLine(heapBoard)
        if (all(v == 0 for v in heapBoard) == True):
            print('Player human has won')
            break

# Human Play First
def HumanFirst(heapBoard):
    while (True):
        # Human Order
        heapFrom, heapMinus = HumanAction()
        heapBoard = humanPlay(heapFrom, heapMinus, heapBoard)
        printOneLine(heapBoard)
        if (all(v == 0 for v in heapBoard) == True):
            print('Player human has won')
            break
        # Machine order
        result = machinePlay(heapBoard)
        heapBoard = result[0]
        heapWhich = result[1]
        heapMinus = result[2]
        print('Player computer took', heapMinus, 'objects from heap', (heapWhich + 1))
        printOneLine(heapBoard)
        if (all(v == 0 for v in heapBoard) == True):
            print('Player computer has won')
            break

# print one line funtion
def printOneLine(heapBoard):
    i = 0
    while (i < heapNums - 1):
        print(heapBoard[i], end=' ')
        i= i+1
    print(heapBoard[i])

if __name__ == '__main__':
    # Initialize heapBoard for the game
    heapBoard = HeapBoard()
    heapNums = len(heapBoard)
    print('Created', heapNums, 'heaps of sizes', end=' ')
    printOneLine(heapBoard)
    if (FirstPlayer() == True):
        print('Player computer goes first')
        MachineFirst(heapBoard)
    else:
        print('Player human goes first')
        HumanFirst(heapBoard)