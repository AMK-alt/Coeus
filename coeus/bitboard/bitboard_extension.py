from coeus.bitboard.bitboard import BitBoard
from bitarray.util import ba2int

class BitboardExtension(BitBoard):

    def __init__(self):
        super()

    @property
    def whitePawns(self):
        return ba2int(self.__whitePawns)

    @property
    def whiteRooks(self):
        return ba2int(self.__whiteRooks)


    @property
    def whiteKnights(self):
        return ba2int(self.__whiteKnights)

    @property
    def whiteBishops(self):
        return ba2int(self.__whiteBishops)

    @property
    def whiteQueens(self):
        return ba2int(self.__whiteQueens)

    @property
    def whiteKing(self):
        return ba2int(self.__whiteKing)

    @property
    def blackPawns(self):
        return ba2int(self.__blackPawns)

    @property
    def blackRooks(self):
        return ba2int(self.__blackRooks)

    @property
    def blackKnights(self):
        return ba2int(self.__blackKnights)

    @property
    def blackBishops(self):
        return ba2int(self.__blackBishops)

    @property
    def blackQueens(self):
        return ba2int(self.__blackQueens)

    @property
    def blackKing(self):
        return ba2int(self.__blackKing)

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
