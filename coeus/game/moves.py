from coeus.game.game_state import GameState
from bitarray.util import ba2int

class Moves():

    #def __init__(self):
    RANK_1 = 255  # 2**8 - 2**0
    RANK_2 = 65280  # 2**16 - 2**8
    RANK_7 = 71776119061217280  # 2**56 - 2**48
    RANK_8 = 18374686479671623680  # 2**64 - 2**56 == (2**63 + 2**62  + 2**61 + 2**60 + 2**59 + 2**58 + 2**57 + 2**56)
    FILE_A = 72340172838076673
    FILE_H = 9259542123273814144

    def getWhitePawnsLegalMoves(self, board):
        whitePawnsCurrentState = board.whitePawns
        whiteCurrentState = board.whitePieces
        blackCurrentState = board.blackPieces

        quietMovesPawnPush = 0
        tacticalMovesCaptures = 0

        currentWhitePawnStateInt = ba2int(whitePawnsCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrentState)

        #Pawn push 1 & 2 moves forward
        quietMovesPawnPush  |= (currentWhitePawnStateInt << 8 | currentWhitePawnStateInt << 16)\
                               & ~self.RANK_8 & ~currentBlackStateInt & ~currentWhiteStateInt

        tacticalMovesCaptures |= (currentWhitePawnStateInt << 7 | currentWhitePawnStateInt << 9) \
                                 & ~self.FILE_A & ~self.RANK_8 & currentBlackStateInt

        if(currentWhitePawnStateInt&self.RANK_8):
            self.whitePawnPromotion(self, currentWhitePawnStateInt&self.RANK_8)

        #tacticalMovesEnPassant =

        return (quietMovesPawnPush, tacticalMovesCaptures)

    def getBlackPawnsLegalMoves(self, board):
        blackPawnsCurrentState = board.blackPawns
        blackCurrentState = board.blackPieces
        whiteCurrenState = board.whitePieces

        quietMovesPawnPush = 0
        tacticalMovesCaptures = 0

        currentBlackPawnStateInt = ba2int(blackPawnsCurrentState)
        currentBlackStateInt = ba2int(blackCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrenState)

        quietMovesPawnPush |= (currentBlackPawnStateInt >> 8 | currentBlackPawnStateInt >> 16)\
                              & ~self.RANK_8 & ~currentBlackStateInt & ~currentWhiteStateInt

        tacticalMovesCaptures |= (currentBlackPawnStateInt >> 7 | currentBlackPawnStateInt >> 9)\
                                 & ~self.FILE_A & ~self.RANK_8 & currentWhiteStateInt

        if (currentBlackPawnStateInt & self.RANK_8):
            self.blackPawnPromotion(self, currentBlackPawnStateInt & self.RANK_8)

        # tacticalMovesEnPassant =

        return (quietMovesPawnPush, tacticalMovesCaptures)

    def getWhiteRookLegalMoves(self, board):
        whiteRookCurrentState = board.whiteRooks
        whiteCurrentState = board.whitePieces
        blackCurrenState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0

        currentWhiteRookStateInt = ba2int(whiteRookCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrenState)

        possiblePositions = currentWhiteRookStateInt

        while((possiblePositions&self.RANK_8) == 0):
            possiblePositions = possiblePositions<<8
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentWhiteRookStateInt

        while((possiblePositions&self.FILE_H) == 0):
            possiblePositions = possiblePositions << 1
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentWhiteRookStateInt

        while((possiblePositions&self.RANK_1) == 0):
            possiblePositions = possiblePositions >> 8
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentWhiteRookStateInt

        while((possiblePositions&self.FILE_A)==0):
            possiblePositions = possiblePositions >> 1
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentWhiteRookStateInt

        while ((possiblePositions & self.RANK_8)==0):
            possiblePositions = possiblePositions << 8
            tacticalMovesCaptures |= possiblePositions & currentBlackStateInt

        possiblePositions = currentWhiteRookStateInt

        while ((possiblePositions & self.FILE_H)==0):
            possiblePositions = possiblePositions << 1
            tacticalMovesCaptures |= possiblePositions & currentBlackStateInt

        possiblePositions = currentWhiteRookStateInt

        while ((possiblePositions & self.RANK_1)==0):
            possiblePositions = possiblePositions >> 8
            tacticalMovesCaptures |= possiblePositions & currentBlackStateInt

        possiblePositions = currentWhiteRookStateInt

        while ((possiblePositions & self.FILE_A)==0):
            possiblePositions = possiblePositions >> 1
            tacticalMovesCaptures |= possiblePositions & currentBlackStateInt

        return (quietMovesPush, tacticalMovesCaptures)

    def getBlackRookLegalMoves(self, board):
        blackRookCurrentState = board.blackRooks
        whiteCurrentState = board.whitePieces
        blackCurrentState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0

        currentBlackRookStateInt = ba2int(blackRookCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrentState)

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.RANK_1)==0):
            possiblePositions |=  possiblePositions >> 8
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.FILE_A)==0):
            possiblePositions |= (possiblePositions >> 1)
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.RANK_8)==0):
            possiblePositions |= (possiblePositions << 8)
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.FILE_H)==0):
            possiblePositions |= (possiblePositions << 1)
            quietMovesPush |= possiblePositions & ~currentWhiteStateInt & ~currentBlackStateInt

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.RANK_1)==0):
            possiblePositions |= (possiblePositions >> 8)
            tacticalMovesCaptures |= possiblePositions & currentWhiteStateInt

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.FILE_A)==0):
            possiblePositions |= (possiblePositions >> 1)
            tacticalMovesCaptures |= possiblePositions & currentWhiteStateInt

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.RANK_8)==0):
            possiblePositions |= (possiblePositions << 8)
            tacticalMovesCaptures |= possiblePositions & currentWhiteStateInt

        possiblePositions = currentBlackRookStateInt

        while ((possiblePositions & self.FILE_H)==0):
            possiblePositions |= (possiblePositions << 1)
            tacticalMovesCaptures |= possiblePositions & currentWhiteStateInt

        return (quietMovesPush, tacticalMovesCaptures)

    def getWhiteKnightLegalMoves(self, board):
        whiteKnightCurrentState = board.whiteKnights
        whiteCurrentState = board.whitePieces
        blackCurrentState = board.blackPieces

        quietMovesKingPush = 0
        tacticalMovesCaptures = 0

        currentWhiteKnightStateInt = ba2int(whiteKnightCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrentState)

        quietMovesKingPush |= (currentWhiteKnightStateInt << 15) | (currentWhiteKnightStateInt << 17) \
                              | (currentWhiteKnightStateInt << 6) | (currentWhiteKnightStateInt << 10) \
                              | (currentWhiteKnightStateInt >> 15) | (currentWhiteKnightStateInt >> 17) \
                              | (currentWhiteKnightStateInt >> 6) | (currentWhiteKnightStateInt >> 10) \
                              & ~currentWhiteStateInt & ~currentBlackStateInt

        tacticalMovesCaptures |= (currentWhiteKnightStateInt << 15) | (currentWhiteKnightStateInt << 17) \
                              | (currentWhiteKnightStateInt << 6) | (currentWhiteKnightStateInt << 10) \
                              | (currentWhiteKnightStateInt >> 15) | (currentWhiteKnightStateInt >> 17) \
                              | (currentWhiteKnightStateInt >> 6) | (currentWhiteKnightStateInt >> 10) \
                              & ~currentWhiteStateInt

        return (quietMovesKingPush, tacticalMovesCaptures)

    def getBlackKnightLegalMoves(self, board):
        blackKnightCurrentState = board.blackKnights
        whiteCurrentState = board.whitePieces
        blackCurrenState = board.blackPieces

        quietMovesKingPush = 0
        tacticalMovesCaptures = 0

        currentBlackKnightStateInt = ba2int(blackKnightCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrenState)

        quietMovesKingPush |= (currentBlackKnightStateInt >> 15) | (currentBlackKnightStateInt >> 17) \
                              | (currentBlackKnightStateInt >> 6) | (currentBlackKnightStateInt >> 10) \
                              | (currentBlackKnightStateInt << 15) | (currentBlackKnightStateInt << 17) \
                              | (currentBlackKnightStateInt << 6) | (currentBlackKnightStateInt << 10) \
                              & ~currentWhiteStateInt & ~currentBlackStateInt

        tacticalMovesCaptures |= (currentBlackKnightStateInt >> 15) | (currentBlackKnightStateInt > 17) \
                                 | (currentBlackKnightStateInt >> 6) | (currentBlackKnightStateInt >> 10) \
                                 | (currentBlackKnightStateInt << 15) | (currentBlackKnightStateInt << 17) \
                                 | (currentBlackKnightStateInt << 6) | (currentBlackKnightStateInt << 10) \
                                 & ~currentWhiteStateInt

        return (quietMovesKingPush, tacticalMovesCaptures)

    def getWhiteBishopLegalMoves(self, board):
        whiteBishopCurrentState = board.whiteBishop
        whiteCurrentState = board.whitePieces
        blackCurrenState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0

        currentWhiteBishopStateInt = ba2int(whiteBishopCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrenState)

        while (not (quietMovesPush&self.RANK_8) or not(currentWhiteBishopStateInt&self.FILE_H)):
            quietMovesPush |= (currentWhiteBishopStateInt<<9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_8) or not (currentWhiteBishopStateInt & self.FILE_A)):
            quietMovesPush |= (currentWhiteBishopStateInt << 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentWhiteBishopStateInt & self.FILE_H)):
            quietMovesPush |= (currentWhiteBishopStateInt >> 9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentWhiteBishopStateInt & self.FILE_A)):
            quietMovesPush |= (currentWhiteBishopStateInt >> 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (tacticalMovesCaptures&self.RANK_8) or not(currentWhiteBishopStateInt&self.FILE_H)):
            tacticalMovesCaptures |= (currentWhiteBishopStateInt<<9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_8) or not (currentWhiteBishopStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentWhiteBishopStateInt << 7) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentWhiteBishopStateInt & self.FILE_H)):
            tacticalMovesCaptures |= (currentWhiteBishopStateInt >> 9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentWhiteBishopStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentWhiteBishopStateInt >> 7) & ~currentWhiteStateInt

        return (quietMovesPush, tacticalMovesCaptures)

    def getBlackBishopLegalMoves(self, board):
        blackBishopCurrentState = board.blackBishop
        whiteCurrentState = board.whitePieces
        blackCurrenState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0

        currentBlackBishopStateInt = ba2int(blackBishopCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrenState)

        while (not (quietMovesPush&self.RANK_8) or not(currentBlackBishopStateInt&self.FILE_H)):
            quietMovesPush |= (currentBlackBishopStateInt >> 9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_8) or not (currentBlackBishopStateInt & self.FILE_A)):
            quietMovesPush |= (currentBlackBishopStateInt >> 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentBlackBishopStateInt & self.FILE_H)):
            quietMovesPush |= (currentBlackBishopStateInt << 9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentBlackBishopStateInt & self.FILE_A)):
            quietMovesPush |= (currentBlackBishopStateInt << 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (tacticalMovesCaptures&self.RANK_8) or not(currentBlackBishopStateInt&self.FILE_H)):
            tacticalMovesCaptures |= (currentBlackBishopStateInt >> 9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_8) or not (currentBlackBishopStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentBlackBishopStateInt >> 7) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentBlackBishopStateInt & self.FILE_H)):
            tacticalMovesCaptures |= (currentBlackBishopStateInt << 9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentBlackBishopStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentBlackBishopStateInt << 7) & ~currentWhiteStateInt

        return (quietMovesPush, tacticalMovesCaptures)

    def getWhiteQueensLegalMoves(self, board):
        whiteQueenCurrentState = board.whiteQueens
        blackCurrentState = board.whitePieces
        whiteCurrentState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0

        currentWhiteQueenStateInt = ba2int(whiteQueenCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrentState)

        while (not (quietMovesPush & self.RANK_8)):
            quietMovesPush |= (currentWhiteQueenStateInt << 8) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_8) or not (currentWhiteQueenStateInt & self.FILE_H)):
            quietMovesPush |= (currentWhiteQueenStateInt << 9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.FILE_H)):
            quietMovesPush |= (currentWhiteQueenStateInt << 1) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_8) or not (currentWhiteQueenStateInt & self.FILE_A)):
            quietMovesPush |= (currentWhiteQueenStateInt << 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1)):
            quietMovesPush |= (currentWhiteQueenStateInt >> 8) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentWhiteQueenStateInt & self.FILE_H)):
            quietMovesPush |= (currentWhiteQueenStateInt >> 9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.FILE_A)):
            quietMovesPush |= (currentWhiteQueenStateInt >> 1) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentWhiteQueenStateInt & self.FILE_A)):
            quietMovesPush |= (currentWhiteQueenStateInt >> 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (tacticalMovesCaptures & self.RANK_8)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt << 8) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures&self.RANK_8) or not(currentWhiteQueenStateInt&self.FILE_H)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt<<9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.FILE_H)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt << 1) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_8) or not (currentWhiteQueenStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt << 7) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt >> 8) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentWhiteQueenStateInt & self.FILE_H)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt >> 9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.FILE_A)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt >> 1) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentWhiteQueenStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentWhiteQueenStateInt >> 7) & ~currentWhiteStateInt

        return (quietMovesPush, tacticalMovesCaptures)

    def getBlackQueensLegalMoves(self, board):
        blackQueensCurrentState = board.blackQueens
        blackCurrentState = board.whitePieces
        whiteCurrentState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0

        currentBlackQueensStateInt = ba2int(blackQueensCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrentState)

        while (not (quietMovesPush & self.RANK_8)):
            quietMovesPush |= (currentBlackQueensStateInt >> 8) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_8) or not (currentBlackQueensStateInt & self.FILE_H)):
            quietMovesPush |= (currentBlackQueensStateInt >> 9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.FILE_H)):
            quietMovesPush |= (currentBlackQueensStateInt >> 1) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_8) or not (currentBlackQueensStateInt & self.FILE_A)):
            quietMovesPush |= (currentBlackQueensStateInt >> 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1)):
            quietMovesPush |= (currentBlackQueensStateInt << 8) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentBlackQueensStateInt & self.FILE_H)):
            quietMovesPush |= (currentBlackQueensStateInt << 9) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.FILE_A)):
            quietMovesPush |= (currentBlackQueensStateInt << 1) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (quietMovesPush & self.RANK_1) or not (currentBlackQueensStateInt & self.FILE_A)):
            quietMovesPush |= (currentBlackQueensStateInt << 7) & ~currentWhiteStateInt & ~currentBlackStateInt

        while (not (tacticalMovesCaptures & self.RANK_8)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt >> 8) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_8) or not (currentBlackQueensStateInt & self.FILE_H)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt >> 9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.FILE_H)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt >> 1) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_8) or not (currentBlackQueensStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt >> 7) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt << 8) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentBlackQueensStateInt & self.FILE_H)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt << 9) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.FILE_A)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt << 1) & ~currentWhiteStateInt

        while (not (tacticalMovesCaptures & self.RANK_1) or not (currentBlackQueensStateInt & self.FILE_A)):
            tacticalMovesCaptures |= (currentBlackQueensStateInt << 7) & ~currentWhiteStateInt

        return (quietMovesPush, tacticalMovesCaptures)

    def getWhiteKingLegalMoves(self, board):
        whiteKingCurrentState = board.whiteKing
        whiteRooksCurrentState = board.whiteRooks
        whiteCurrentState = board.whitePieces
        blackCurrenState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0
        tacticalMovesCastling = 0

        currentWhiteKingStateInt = ba2int(whiteKingCurrentState)
        currentWhiteRooksStateInt = ba2int(whiteRooksCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrenState)

        quietMovesPush = ((currentWhiteKingStateInt << 8) & ~self.RANK_8 & ~currentWhiteStateInt \
                              & ~currentBlackStateInt) \
                             | ((currentWhiteKingStateInt << 9) & ~self.RANK_8 & ~self.FILE_H
                                & ~currentWhiteStateInt & ~currentBlackStateInt) \
                             | ((currentWhiteKingStateInt << 7) & ~self.RANK_8 & ~self.FILE_A
                                & ~currentWhiteStateInt & ~currentBlackStateInt) \
                             | ((currentWhiteKingStateInt << 1)  & ~self.FILE_H & ~currentWhiteStateInt\
                              & ~currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 1)  & ~self.FILE_A & ~currentWhiteStateInt \
                              & ~currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 8) & ~self.RANK_1 & ~currentWhiteStateInt \
                              & ~currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 9) & ~self.RANK_1 & ~self.FILE_H \
                              & ~currentWhiteStateInt & ~currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 7) & ~self.RANK_1 & ~self.FILE_A \
                              & ~currentWhiteStateInt & ~currentBlackStateInt)

        tacticalMovesCaptures = ((currentWhiteKingStateInt << 8) & ~self.RANK_8 & ~currentWhiteStateInt \
                              & currentBlackStateInt) \
                             | ((currentWhiteKingStateInt << 9) & ~self.RANK_8 & ~self.FILE_H
                                & ~currentWhiteStateInt & currentBlackStateInt) \
                             | ((currentWhiteKingStateInt << 7) & ~self.RANK_8 & ~self.FILE_A
                                & ~currentWhiteStateInt & currentBlackStateInt) \
                             | ((currentWhiteKingStateInt << 1)  & ~self.FILE_H & ~currentWhiteStateInt\
                              & currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 1)  & ~self.FILE_A & ~currentWhiteStateInt \
                              & currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 8) & ~self.RANK_1 & ~currentWhiteStateInt \
                              & currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 9) & ~self.RANK_1 & ~self.FILE_H \
                              & ~currentWhiteStateInt & currentBlackStateInt) \
                             | ((currentWhiteKingStateInt >> 7) & ~self.RANK_1 & ~self.FILE_A \
                              & ~currentWhiteStateInt & currentBlackStateInt)

        if(not (super().whiteKingWasMoved and super().whiteRookWasMoved)):
            if((currentWhiteKingStateInt | currentWhiteRooksStateInt) == 96):
                tacticalMovesCastling |= (currentWhiteKingStateInt << 2) | (currentWhiteRooksStateInt >> 2)

        return (quietMovesPush, tacticalMovesCaptures, tacticalMovesCastling)

    def getBlackKingLegalMoves(self, board):
        blackKingCurrentState = board.blackKing
        blackRookCurrentState = board.blackRook
        blackCurrentState = board.whitePieces
        whiteCurrentState = board.blackPieces

        quietMovesPush = 0
        tacticalMovesCaptures = 0
        tacticalMovesCastling = 0

        currentBlackKingStateInt = ba2int(blackKingCurrentState)
        currentBlackRookStateInt = ba2int(blackRookCurrentState)
        currentWhiteStateInt = ba2int(whiteCurrentState)
        currentBlackStateInt = ba2int(blackCurrentState)

        quietMovesPush = ((currentBlackKingStateInt >> 8) & ~self.RANK_8 & ~currentWhiteStateInt \
                          & ~currentBlackStateInt) \
                         | ((currentBlackKingStateInt >> 9) & ~self.RANK_8 & ~self.FILE_H
                            & ~currentWhiteStateInt & ~currentBlackStateInt) \
                         | ((currentBlackKingStateInt >> 7) & ~self.RANK_8 & ~self.FILE_A
                            & ~currentWhiteStateInt & ~currentBlackStateInt) \
                         | ((currentBlackKingStateInt >> 1) & ~self.FILE_H & ~currentWhiteStateInt \
                            & ~currentBlackStateInt) \
                         | ((currentBlackKingStateInt << 1) & ~self.FILE_A & ~currentWhiteStateInt \
                            & ~currentBlackStateInt) \
                         | ((currentBlackKingStateInt << 8) & ~self.RANK_1 & ~currentWhiteStateInt \
                            & ~currentBlackStateInt) \
                         | ((currentBlackKingStateInt << 9) & ~self.RANK_1 & ~self.FILE_H \
                            & ~currentWhiteStateInt & ~currentBlackStateInt) \
                         | ((currentBlackKingStateInt << 7) & ~self.RANK_1 & ~self.FILE_A \
                            & ~currentWhiteStateInt & ~currentBlackStateInt)

        tacticalMovesCaptures = ((currentBlackKingStateInt >> 8) & ~self.RANK_8 & ~currentWhiteStateInt \
                                 & currentBlackStateInt) \
                                | ((currentBlackKingStateInt >> 9) & ~self.RANK_8 & ~self.FILE_H
                                   & ~currentWhiteStateInt & currentBlackStateInt) \
                                | ((currentBlackKingStateInt >> 7) & ~self.RANK_8 & ~self.FILE_A
                                   & ~currentWhiteStateInt & currentBlackStateInt) \
                                | ((currentBlackKingStateInt >> 1) & ~self.FILE_H & ~currentWhiteStateInt \
                                   & currentBlackStateInt) \
                                | ((currentBlackKingStateInt << 1) & ~self.FILE_A & ~currentWhiteStateInt \
                                   & currentBlackStateInt) \
                                | ((currentBlackKingStateInt << 8) & ~self.RANK_1 & ~currentWhiteStateInt \
                                   & currentBlackStateInt) \
                                | ((currentBlackKingStateInt << 9) & ~self.RANK_1 & ~self.FILE_H \
                                   & ~currentWhiteStateInt & currentBlackStateInt) \
                                | ((currentBlackKingStateInt << 7) & ~self.RANK_1 & ~self.FILE_A \
                                   & ~currentWhiteStateInt & currentBlackStateInt)

        if(not (super().blackKingWasMoved and super().blackRookWasMoved)):
            if((currentBlackKingStateInt | currentBlackRookStateInt) == 96):
                tacticalMovesCastling |= (currentBlackKingStateInt << 2) | (currentBlackRookStateInt >> 2)

        return (quietMovesPush, tacticalMovesCaptures, tacticalMovesCastling)

    def whitePawnPromotion(self, bit, promotionType=0):
        if(promotionType == 0):
            super.whiteQueens |= bit
            super.whitePawns ^= bit
        elif(promotionType == 1):
            super.whiteKnights |= bit
            super.whitePawns ^= bit
        elif (promotionType == 2):
            super.whiteRooks |= bit
            super.whitePawns ^= bit
        else:
            super.whiteBishop |= bit
            super.whitePawns ^= bit

    def blackPawnPromotion(self, bit, promotionType=0):
        if(promotionType == 0):
            super.blackQueens |= bit
            super.blackPawns ^= bit
        elif(promotionType == 1):
            super.blackKnights |= bit
            super.blackPawns ^= bit
        elif (promotionType == 2):
            super.blackRooks |= bit
            super.blackPawns ^= bit
        else:
            super.blackBishop |= bit
            super.blackPawns ^= bit

    def whiteCheck(self, board):
        return ba2int(board.whiteKing) & self.getBlackPawnsLegalMoves(board) & self.getBlackBishopLegalMoves(board) \
               & self.getBlackRookLegalMoves(board) & self.getBlackKnightLegalMoves(board) \
               & self.getBlackQueensLegalMoves(board) & self.getBlackKingLegalMoves(board)

    def blackCheck(self, board):
        return ba2int(board.blackKing) & self.getWhitePawnsLegalMoves(board) & self.getWhiteBishopLegalMoves(board) \
               & self.getWhiteRookLegalMoves(board) & self.getWhiteKnightLegalMoves(board) \
               & self.getWhiteQueensLegalMoves(board) & self.getWhiteKingLegalMoves(board)
