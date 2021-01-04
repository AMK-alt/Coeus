from bitarray import bitarray
from bitarray.util import ba2int

def check_board_integrity(board):
    return not (ba2int(board.whitePawns) & ba2int(board.whiteRooks) & ba2int(board.whiteKnights)
                    & ba2int(board.whiteBishops) & ba2int(board.whiteQueens) & ba2int(board.whiteKing)
                    & ba2int(board.blackPawns) & ba2int(board.blackRooks) & ba2int(board.blackKnights)
                    & ba2int(board.blackBishops) & ba2int(board.blackQueens) & ba2int(board.blackKing))


def rotate_board(board):
    board.whitePawns.reverse()
    board.whiteRooks.reverse()
    board.whiteKnights.reverse()
    board.whiteBishops.reverse()
    board.whiteQueens.reverse()
    board.whiteKing.reverse()
    board.blackPawns.reverse()
    board.blackRooks.reverse()
    board.blackKnights.reverse()
    board.blackBishops.reverse()
    board.blackQueens.reverse()
    board.blackKing.reverse()
