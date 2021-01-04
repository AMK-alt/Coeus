from bitarray import bitarray
from bitarray.util import ba2int
from bitarray.util import int2ba
import random

class BitBoard:
    def __init__(self, typeOfGame):
        self.__nullBitArray = bitarray(64, endian='little')
        self.__nullBitArray.setall(False)
        self.__whitePawns = bitarray(64, endian='little')
        self.__whitePawns.setall(False)
        self.__whiteRooks = bitarray(64, endian='little')
        self.__whiteRooks.setall(False)
        self.__whiteKnights = bitarray(64, endian='little')
        self.__whiteKnights.setall(False)
        self.__whiteBishops = bitarray(64, endian='little')
        self.__whiteBishops.setall(False)
        self.__whiteQueens = bitarray(64, endian='little')
        self.__whiteQueens.setall(False)
        self.__whiteKing = bitarray(64, endian='little')
        self.__whiteKing.setall(False)
        self.__blackPawns = bitarray(64, endian='little')
        self.__blackPawns.setall(False)
        self.__blackRooks = bitarray(64, endian='little')
        self.__blackRooks.setall(False)
        self.__blackKnights = bitarray(64, endian='little')
        self.__blackKnights.setall(False)
        self.__blackBishops = bitarray(64, endian='little')
        self.__blackBishops.setall(False)
        self.__blackQueens = bitarray(64, endian='little')
        self.__blackQueens.setall(False)
        self.__blackKing = bitarray(64, endian='little')
        self.__blackKing.setall(False)
        self.__whitePieces = bitarray(64, endian='little')
        self.__whitePieces.setall(False)
        self.__blackPieces = bitarray(64, endian='little')
        self.__blackPieces.setall(False)
        self.__allPieces = bitarray(64, endian='little')
        self.__allPieces.setall(False)

        if typeOfGame == 'Classic':
            self.__initialiseBitboard()
        elif typeOfGame == '960':
            self.__initialiseBitboardChess960()

    @property
    def whitePawns(self):
        return self.__whitePawns

    @whitePawns.setter
    def whitePawns(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__whitePawns = newValue

    @property
    def whiteRooks(self):
        return self.__whiteRooks

    @whiteRooks.setter
    def whiteRooks(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__whiteRooks = newValue

    @property
    def whiteKnights(self):
        return self.__whiteKnights

    @whiteKnights.setter
    def whiteKnights(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__whiteKnights = newValue

    @property
    def whiteBishops(self):
        return self.__whiteBishops

    @whiteBishops.setter
    def whiteBishops(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__whiteBishops = newValue

    @property
    def whiteQueens(self):
        return self.__whiteQueens

    @whiteQueens.setter
    def whiteQueens(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__whiteQueens = newValue

    @property
    def whiteKing(self):
        return self.__whiteKing

    @whiteKing.setter
    def whiteKing(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__whiteKing = newValue

    @property
    def blackPawns(self):
        return self.__blackPawns

    @blackPawns.setter
    def blackPawns(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__blackPawns = newValue

    @property
    def blackRooks(self):
        return self.__blackRooks

    @blackRooks.setter
    def blackRooks(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__blackRooks = newValue

    @property
    def blackKnights(self):
        return self.__blackKnights

    @blackKnights.setter
    def blackKnights(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__blackKnights = newValue

    @property
    def blackBishops(self):
        return self.__blackBishops

    @blackBishops.setter
    def blackBishops(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__blackBishops = newValue

    @property
    def blackQueens(self):
        return self.__blackQueens

    @blackQueens.setter
    def blackQueens(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__blackQueens = newValue

    @property
    def blackKing(self):
        return self.__blackKing

    @blackKing.setter
    def blackKing(self, newValue):
        if(not isinstance(newValue, bitarray)):
            raise TypeError("Type " + str(type(newValue).__name__) + " received while "
                            + str(bitarray.__name__) + " expected")
        elif(newValue.length() != 64):
            raise ValueError("The length of the bitarray is " + newValue.legth() + " instaed of 64")
        elif(newValue.endian() == 'big'):
            raise ValueError("The bit endianness is " + newValue.endian() + " instaed of little")
        else:
            self.__blackKing = newValue

    @property
    def whitePieces(self):
        return int2ba(ba2int(self.whitePawns) | ba2int(self.whiteRooks) | ba2int(self.whiteKnights)
                                    | ba2int(self.whiteBishops) | ba2int(self.whiteQueens)
                                    | ba2int(self.whiteKing), 64, endian='little')

    @property
    def blackPieces(self):
        return int2ba(ba2int(self.blackPawns) | ba2int(self.blackRooks) | ba2int(self.blackKnights)
                                    | ba2int(self.blackBishops) | ba2int(self.blackQueens)
                                    | ba2int(self.blackKing), 64, endian='little')

    @property
    def allPieces(self):
        return int2ba(ba2int(self.whitePieces) | ba2int(self.blackPieces), 64, endian='little')

    def __initialiseBitboard(self):
        self.whitePawns       = int2ba((ba2int(self.whitePawns) | 255) << 8, 64, endian='little')
        self.whiteRooks       = int2ba((ba2int(self.whiteRooks) | 129), 64, endian='little')
        self.whiteKnights     = int2ba((ba2int(self.whiteKnights) | 66), 64, endian='little')
        self.whiteBishops     = int2ba((ba2int(self.whiteBishops) | 36), 64, endian='little')
        self.whiteQueens      = int2ba((ba2int(self.whiteQueens) | 8), 64, endian='little')
        self.whiteKing        = int2ba((ba2int(self.whiteKing) | 16), 64, endian='little')
        self.blackPawns       = int2ba(ba2int(self.whitePawns) << 40, 64, endian='little')
        self.blackRooks       = int2ba(ba2int(self.whiteRooks) << 56, 64, endian='little')
        self.blackKnights     = int2ba(ba2int(self.whiteKnights) << 56, 64, endian='little')
        self.blackBishops     = int2ba(ba2int(self.whiteBishops) << 56, 64, endian='little')
        self.blackQueens      = int2ba(ba2int(self.whiteQueens) << 56, 64, endian='little')
        self.blackKing        = int2ba(ba2int(self.whiteKing) << 56, 64, endian='little')

    def __initialiseBitboardChess960(self):
        self.whitePawns = int2ba((ba2int(self.whitePawns) | 255) << 8, 64, endian='little')

        positionList = list(range(0, 8))

        randNumber = random.choice(positionList)

        #self.__whiteBishops[randNumber] = True
        self.whiteBishops =  int2ba(ba2int(self.whiteBishops) | ((ba2int(self.__nullBitArray) | 1) << randNumber)
                                    , 64, endian='little')

        lastPosition = randNumber

        positionList.remove(randNumber)

        while randNumber % 2 == lastPosition % 2:
            randNumber = random.choice(positionList)
        else:
            #self.__whiteBishops[randNumber] = True
            self.whiteBishops =  int2ba(ba2int(self.whiteBishops)
                                          | ((ba2int(self.__nullBitArray) | 1) << randNumber), 64, endian='little')

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteRooks[randNumber] = True
        self.whiteRooks = int2ba(ba2int(self.whiteRooks)
                                   | ((ba2int(self.__nullBitArray) | 1) << randNumber), 64, endian='little')

        lastPosition = randNumber

        positionList.remove(randNumber)

        while randNumber <= lastPosition+1 and randNumber >= lastPosition-1:
            randNumber = random.choice(positionList)
        else:
            #self.__whiteRooks[randNumber] = True
            self.whiteRooks = int2ba(ba2int(self.whiteRooks)
                                       | ((ba2int(self.__nullBitArray) | 1) << randNumber), 64, endian='little')

        rookLastPosition = randNumber

        positionList.remove(randNumber)
        
        if lastPosition < rookLastPosition:
            while randNumber <= lastPosition or randNumber >= rookLastPosition:
                randNumber = random.choice(positionList)
        else:
            while randNumber >= lastPosition or randNumber <= rookLastPosition:
                randNumber = random.choice(positionList)

        #self.__whiteKing[randNumber] = True
        self.whiteKing = int2ba(ba2int(self.whiteKing)
                                   | ((ba2int(self.__nullBitArray) | 1) << randNumber), 64, endian='little')

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteKnights[randNumber] = True
        self.whiteKnights = int2ba(ba2int(self.whiteKnights)
                                  | ((ba2int(self.__nullBitArray) | 1) << randNumber), 64, endian='little')

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteKnights[randNumber] = True
        self.whiteKnights = int2ba(ba2int(self.whiteKnights)
                                     | ((ba2int(self.__nullBitArray) | 1) << randNumber), 64, endian='little')

        positionList.remove(randNumber)

        randNumber = random.choice(positionList)

        #self.__whiteQueens[randNumber] = True
        self.whiteQueens = int2ba(ba2int(self.whiteQueens)
                                     | ((ba2int(self.__nullBitArray) | 1) << randNumber), 64, endian='little')

        self.blackPawns   = int2ba(ba2int(self.whitePawns) << 40, 64, endian='little')
        self.blackRooks   = int2ba(ba2int(self.whiteRooks)    << 56, 64, endian='little')
        self.blackBishops = int2ba(ba2int(self.whiteBishops)  << 56, 64, endian='little')
        self.blackKnights = int2ba(ba2int(self.whiteKnights)  << 56, 64, endian='little')
        self.blackQueens  = int2ba(ba2int(self.whiteQueens)   << 56, 64, endian='little')
        self.blackKing    = int2ba(ba2int(self.whiteKing)     << 56, 64, endian='little')

    def checkBoardIntegrity(self):
        return not (ba2int(self.whitePawns)     & ba2int(self.whiteRooks)   & ba2int(self.whiteKnights)
                    & ba2int(self.whiteBishops) & ba2int(self.whiteQueens)  & ba2int(self.whiteKing)
                    & ba2int(self.blackPawns)   & ba2int(self.blackRooks)   & ba2int(self.blackKnights)
                    & ba2int(self.blackBishops) & ba2int(self.blackQueens)  & ba2int(self.blackKing))
