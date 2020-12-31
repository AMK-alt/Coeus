from coeus.bitboard.bitboard import BitBoard
#from  coeus.Moves import Moves

class GameState:

    def __init__(self, typeOfGame):
        turn = 0
        whiteKingWasMoved = 0
        whiteRookWasMoved = 0
        blackKingWasMoved = 0
        blackRookWasMoved = 0

        bitboard = BitBoard(typeOfGame)
        moves = Moves()




