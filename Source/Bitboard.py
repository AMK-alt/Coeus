from bitarray import bitarray
from bitarray.util import ba2int
from bitarray.util import int2ba
import random

class BitBoard:
    __zeroVariable    = bitarray(64, endian='little')
    __zeroVariable.setall(False)
    __whitePawns      = bitarray(64, endian='little')
    __whitePawns.setall(False)
    __whiteRooks      = bitarray(64, endian='little')
    __whiteRooks.setall(False)
    __whiteKnights    = bitarray(64, endian='little')
    __whiteKnights.setall(False)
    __whiteBishops    = bitarray(64, endian='little')
    __whiteBishops.setall(False)
    __whiteQueens     = bitarray(64, endian='little')
    __whiteQueens.setall(False)
    __whiteKing       = bitarray(64, endian='little')
    __whiteKing.setall(False)
    __blackPawns      = bitarray(64, endian='little')
    __blackPawns.setall(False)
    __blackRooks      = bitarray(64, endian='little')
    __blackRooks.setall(False)
    __blackKnights    = bitarray(64, endian='little')
    __blackKnights.setall(False)
    __blackBishops    = bitarray(64, endian='little')
    __blackBishops.setall(False)
    __blackQueens     = bitarray(64, endian='little')
    __blackQueens.setall(False)
    __blackKing       = bitarray(64, endian='little')
    __blackKing.setall(False)
    __whitePieces     = bitarray(64, endian='little')
    __whitePieces.setall(False)
    __blackPieces     = bitarray(64, endian='little')
    __blackPieces.setall(False)
    __allPieces       = bitarray(64, endian='little')
    __allPieces.setall(False)

    def __init__(self, typeOfGame):
        if typeOfGame == 'Classic':
            self.__initialiseBitboard()
        else:
            self.__initialiseBitboardChess960()

    def __initialiseBitboard(self):
        self.__whitePawns       = int2ba((ba2int(self.__whitePawns) | 255) << 8, 64)
        self.__whiteRooks       = int2ba((ba2int(self.__whiteRooks) | 129), 64)
        self.__whiteKnights     = int2ba((ba2int(self.__whiteKnights) | 66), 64)
        self.__whiteBishops     = int2ba((ba2int(self.__whiteKnights) | 36), 64)
        self.__whiteQueens      = int2ba((ba2int(self.__whiteKnights) | 8), 64)
        self.__whiteKing        = int2ba((ba2int(self.__whiteKnights) | 16), 64)
        self.__blackPawns       = int2ba(ba2int(self.__whitePawns) << 40, 64)
        self.__blackRooks       = int2ba(ba2int(self.__whiteRooks) << 56, 64)
        self.__blackKnights     = int2ba(ba2int(self.__whiteKnights) << 56, 64)
        self.__blackBishops     = int2ba(ba2int(self.__whiteBishops) << 56, 64)
        self.__blackQueens      = int2ba(ba2int(self.__whiteQueens) << 56, 64)
        self.__blackKing        = int2ba(ba2int(self.__whiteKing) << 56, 64)

        self.__whitePieces = int2ba(ba2int(self.__whitePawns) | ba2int(self.__whiteRooks) | ba2int(self.__whiteKnights)
                                    | ba2int(self.__whiteBishops) | ba2int(self.__whiteQueens)
                                    | ba2int(self.__whiteKing))

        self.__blackPieces = int2ba(ba2int(self.__blackPawns) | ba2int(self.__blackRooks) | ba2int(self.__blackKnights)
                                    | ba2int(self.__blackBishops) | ba2int(self.__blackQueens)
                                    | ba2int(self.__blackKing))

        self.__allPieces = int2ba(ba2int(self.__whitePieces) | ba2int(self.__blackPieces))

    def __initialiseBitboardChess960(self):
        self.__whitePawns      = int2ba((ba2int(self.__whitePawns) | 255) << 8, 64)

        positionList = list(range(0, 8))

        randNumber = random.choice(positionList)

        #self.__whiteBishops[randNumber] = True
        self.__whiteBishops =  int2ba(ba2int(self.__whiteBishops) | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        lastPosition = randNumber

        positionList.remove(randNumber)

        while randNumber % 2 == lastPosition % 2:
            randNumber = random.choice(positionList)
        else:
            #self.__whiteBishops[randNumber] = True
            self.__whiteBishops =  int2ba(ba2int(self.__whiteBishops)
                                          | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteRooks[randNumber] = True
        self.__whiteRooks = int2ba(ba2int(self.__whiteRooks)
                                   | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        lastPosition = randNumber

        positionList.remove(randNumber)

        while randNumber <= lastPosition+1 and randNumber >= lastPosition-1:
            randNumber = random.choice(positionList)
        else:
            #self.__whiteRooks[randNumber] = True
            self.__whiteRooks = int2ba(ba2int(self.__whiteRooks)
                                       | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        rookLastPosition = randNumber

        positionList.remove(randNumber)
        
        if lastPosition < rookLastPosition:
            while randNumber <= lastPosition or randNumber >= rookLastPosition:
                randNumber = random.choice(positionList)
        else:
            while randNumber >= lastPosition or randNumber <= rookLastPosition:
                randNumber = random.choice(positionList)

        #self.__whiteKing[randNumber] = True
        self.__whiteKing = int2ba(ba2int(self.__whiteKing)
                                   | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteKnights[randNumber] = True
        self.__whiteKnights = int2ba(ba2int(self.__whiteKnights)
                                  | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteKnights[randNumber] = True
        self.__whiteKnights = int2ba(ba2int(self.__whiteKnights)
                                     | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteQueens[randNumber] = True
        self.__whiteQueens = int2ba(ba2int(self.__whiteQueens)
                                     | ((ba2int(self.__zeroVariable) | 1) << randNumber), 64)

        self.__blackPawns   = int2ba(ba2int(self.__whitePawns) << 40, 64)
        self.__blackRooks   = int2ba(ba2int(self.__whiteRooks)    << 56, 64)
        self.__blackBishops = int2ba(ba2int(self.__whiteBishops)  << 56, 64)
        self.__blackKnights = int2ba(ba2int(self.__whiteKnights)  << 56, 64)
        self.__blackQueens  = int2ba(ba2int(self.__whiteQueens)   << 56, 64)
        self.__blackKing    = int2ba(ba2int(self.__whiteKing)     << 56, 64)

        self.__whitePieces = int2ba(ba2int(self.__whitePawns) | ba2int(self.__whiteRooks) | ba2int(self.__whiteKnights)
                                    | ba2int(self.__whiteBishops) | ba2int(self.__whiteQueens)
                                    | ba2int(self.__whiteKing), 64)

        self.__blackPieces = int2ba(ba2int(self.__blackPawns) | ba2int(self.__blackRooks) | ba2int(self.__blackKnights)
                                    | ba2int(self.__blackBishops) | ba2int(self.__blackQueens)
                                    | ba2int(self.__blackKing), 64)

        self.__allPieces = int2ba(ba2int(self.__whitePieces) | ba2int(self.__blackPieces))

    def checkBoardIntegrity(self):
        return not (ba2int(self.__whitePawns)     & ba2int(self.__whiteRooks)   & ba2int(self.__whiteKnights)
                    & ba2int(self.__whiteBishops) & ba2int(self.__whiteQueens)  & ba2int(self.__whiteKing)
                    & ba2int(self.__blackPawns)   & ba2int(self.__blackRooks)   & ba2int(self.__blackKnights)
                    & ba2int(self.__blackBishops) & ba2int(self.__blackQueens)  & ba2int(self.__blackKing))

    def showBoard(self):
        for i in range(len(self.__allPieces.tolist())):
            if i % 8 == 0:
                print()
            if self.__allPieces[i] is False:
                print('_', end='  ')
            else:
                if self.__allPieces[i] == self.__whitePawns[i]:
                    print(u'\u2659', end=' ')
                elif self.__allPieces[i] == self.__whiteRooks[i]:
                    print(u'\u2656', end=' ')
                elif self.__allPieces[i] == self.__whiteKnights[i]:
                    print(u'\u2658', end=' ')
                elif self.__allPieces[i] == self.__whiteBishops[i]:
                    print(u'\u2657', end=' ')
                elif self.__allPieces[i] == self.__whiteQueens[i]:
                    print(u'\u2655', end=' ')
                elif self.__allPieces[i] == self.__whiteKing[i]:
                    print(u'\u2654', end=' ')
                elif self.__allPieces[i] ==self. __blackPawns[i]:
                    print(u'\u265F', end=' ')
                elif self.__allPieces[i] == self.__blackRooks[i]:
                    print(u'\u265C', end=' ')
                elif self.__allPieces[i] == self.__blackKnights[i]:
                    print(u'\u265E', end=' ')
                elif self.__allPieces[i] == self.__blackBishops[i]:
                    print(u'\u265D', end=' ')
                elif self.__allPieces[i] == self.__blackQueens[i]:
                    print(u'\u265B', end=' ')
                elif self.__allPieces[i] == self.__blackKing[i]:
                    print(u'\u265A', end=' ')
