from bitarray import bitarray
from bitarray.util import ba2int
from bitarray.util import int2ba
import random

class BitBoard:
    __whitePawns      = bitarray(64)
    __whitePawns.setall(False)
    __whiteRooks      = bitarray(64)
    __whiteRooks.setall(False)
    __whiteKnights    = bitarray(64)
    __whiteKnights.setall(False)
    __whiteBishops    = bitarray(64)
    __whiteBishops.setall(False)
    __whiteQueens     = bitarray(64)
    __whiteQueens.setall(False)
    __whiteKing       = bitarray(64)
    __whiteKing.setall(False)
    __blackPawns      = bitarray(64)
    __blackPawns.setall(False)
    __blackRooks      = bitarray(64)
    __blackRooks.setall(False)
    __blackKnights    = bitarray(64)
    __blackKnights.setall(False)
    __blackBishops    = bitarray(64)
    __blackBishops.setall(False)
    __blackQueens     = bitarray(64)
    __blackQueens.setall(False)
    __blackKing       = bitarray(64)
    __blackKing.setall(False)
    __whitePieces     = bitarray(64)
    __whitePieces.setall(False)
    __blackPieces     = bitarray(64)
    __blackPieces.setall(False)
    __allPieces       = bitarray(64)
    __allPieces.setall(False)

    def __init__(self, typeOfGame):
        if typeOfGame == 'Classic':
            self.initialiseBitboard()
        else:
            self.initialiseBitboardChess960()

    def initialiseBitboard(self):
        self.__whitePawns      = bitarray('0000000000000000000000000000000000000000000000001111111100000000')
        self.__whiteRooks      = bitarray('0000000000000000000000000000000000000000000000000000000010000001')
        self.__whiteKnights    = bitarray('0000000000000000000000000000000000000000000000000000000001000010')
        self.__whiteBishops    = bitarray('0000000000000000000000000000000000000000000000000000000000100100')
        self.__whiteQueens     = bitarray('0000000000000000000000000000000000000000000000000000000000001000')
        self.__whiteKing       = bitarray('0000000000000000000000000000000000000000000000000000000000010000')
        self.__blackPawns      = bitarray('0000000011111111000000000000000000000000000000000000000000000000')
        self.__blackRooks      = bitarray('1000000100000000000000000000000000000000000000000000000000000000')
        self.__blackKnights    = bitarray('0100001000000000000000000000000000000000000000000000000000000000')
        self.__blackBishops    = bitarray('0010010000000000000000000000000000000000000000000000000000000000')
        self.__blackQueens     = bitarray('0000100000000000000000000000000000000000000000000000000000000000')
        self.__blackKing       = bitarray('0001000000000000000000000000000000000000000000000000000000000000')

        self.__whitePieces = int2ba(ba2int(self.__whitePawns) | ba2int(self.__whiteRooks) | ba2int(self.__whiteKnights) | ba2int(self.__whiteBishops)
                             | ba2int(self.__whiteQueens) | ba2int(self.__whiteKing))

        self.__blackPieces = int2ba(ba2int(self.__blackPawns) | ba2int(self.__blackRooks) | ba2int(self.__blackKnights) | ba2int(self.__blackBishops)
                             | ba2int(self.__blackQueens) | ba2int(self.__blackKing))

        self.__allPieces = int2ba(ba2int(self.__whitePieces) | ba2int(self.__blackPieces))

    def initialiseBitboardChess960(self):
        self.__whitePawns      = int2ba((ba2int(self.__whitePawns) | 255) << 8, 64)
        self.__blackPawns      = int2ba((ba2int(self.__blackPawns) | 255) << 48, 64)

        positionList = list(range(0, 7))

        randNumber = random.choice(positionList)

        self.__whiteBishops[randNumber] = True

        lastPosition = positionList.pop(randNumber)

        while randNumber % 2 == lastPosition % 2:
            randNumber = random.choice(positionList)
        else:
            self.__whiteBishops[randNumber] = True

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        self.__whiteRooks[randNumber] = True

        lastPosition = positionList.pop(randNumber)

        while randNumber <= lastPosition+1 or randNumber >= lastPosition-1:
            randNumber = random.choice(positionList)
        else:
            self.__whiteRooks[randNumber] = True

        rookLastPosition = positionList.pop(randNumber)

        while randNumber > lastPosition and randNumber < rookLastPosition:
            randNumber = random.choice(positionList)
        else:
            self.__whiteKing[randNumber] = True

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        self.__whiteKnights[randNumber] = True

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        self.__whiteKnights[randNumber] = True

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        self.__whiteQueens[randNumber] = True

        self.__blackRooks     = int2ba(ba2int(self.__whiteRooks)    << 56)
        self.__blackBishops   = int2ba(ba2int(self.__whiteBishops)  << 56)
        self.__blackKnights   = int2ba(ba2int(self.__whiteKnights)  << 56)
        self.__blackQueens    = int2ba(ba2int(self.__whiteQueens)   << 56)
        self.__blackKing      = int2ba(ba2int(self.__whiteKing)     << 56)


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
