from coeus.bitboard.bitboard import BitBoard
from coeus.game.moves import Moves

#b = bitarray(64, endian='little')
#b.setall(False)

#b = int2ba(18374686479671623680, 64, endian='little')

#print(b)
#print(ba2int(b))

b= BitBoard('Classic')

print(b.whitePieces)

b.showBoard()

m = Moves()

#print(m.getWhitePawnsLegalMoves(b), m.getWhitePawnsLegalMoves(b)[0])

#b.whiteRooks = int2ba(m.getWhiteRookLegalMoves(b)[0], 64, endian='little')

#b.showBoard()

#b.blackKnights = int2ba(m.getBlackKnightLegalMoves(b)[0], 64, endian='little')

#b.showBoard()

#b.whitePawns = int2ba(m.getWhitePawnsLegalMoves(b)[0], 64, endian='little')
#b.blackRooks[63] = False

#b.showBoard()

#b.blackRooks = int2ba(ba2int(b.blackRooks)>>16, 64, endian='little')

#print(ba2int(b.blackRooks))

#b.showBoard()

#b.blackRooks = int2ba(m.getBlackRookLegalMoves(b)[0], 64, endian='little')

#b.showBoard()

#print(b.blackRooks)
#print(ba2int(b.blackRooks))
#print(b.whitePieces)

#b.blackPawns = int2ba(m.getBlackPawnsLegalMoves(b)[0], 64, endian='little')

#b.showBoard()
