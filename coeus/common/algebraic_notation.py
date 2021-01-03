import math

"""

rank = [0, 1, 2, 3, 4, 5, 6, 7]

file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def getAlgebraicNotation(square):
    algebraicNotation = ''

    if(not isinstance(square, int)):
        raise TypeError("Type " + str(type(square).__name__) + " received while "
                        + str(int.__name__) + " expected")
    elif(square > 63 or square < 0):
        raise ValueError("This is not a valid square")
    else:
        algebraicNotation =  file[(square%8)-1] + str(rank[int(math.ceil(square/8))])

    return algebraicNotation
"""
file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

rank = [0, 1, 2, 3, 4, 5, 6, 7]

pieces = {
    'whitePawns': '',
    'whiteRooks': 'R',
    'whiteKnights': 'N',
    'whiteBishops': 'B',
    'whiteQueens': 'Q',
    'whiteKing': 'K',
    'blackPawns': '',
    'blackRooks': 'R',
    'blackKnights': 'N',
    'blackBishops': 'B',
    'blackQueens': 'Q',
    'blackKing': 'K',
}

identification = {
    0: 'a1',
    1: 'b1',
    2: 'c1',
    3: 'd1',
    4: 'e1',
    5: 'f1',
    6: 'g1',
    7: 'h1',
    8: 'a2',
    9: 'b2',
    10: 'c2',
    11: 'd2',
    12: 'e2',
    13: 'f2',
    14: 'g2',
    15: 'h2',
    16: 'a3',
    17: 'b3',
    18: 'c3',
    19: 'd3',
    20: 'e3',
    21: 'f3',
    22: 'g3',
    23: 'h3',
    24: 'a4',
    25: 'b4',
    26: 'c4',
    27: 'd4',
    28: 'e4',
    29: 'f4',
    30: 'g4',
    31: 'h4',
    32: 'a5',
    33: 'b5',
    34: 'c5',
    35: 'd5',
    36: 'e5',
    37: 'f5',
    38: 'g5',
    39: 'h5',
    40: 'a6',
    41: 'b6',
    42: 'c6',
    43: 'd6',
    44: 'e6',
    45: 'f6',
    46: 'g6',
    47: 'h6',
    48: 'a7',
    49: 'b7',
    50: 'c7',
    51: 'd7',
    52: 'e7',
    53: 'f7',
    54: 'g7',
    55: 'h7',
    56: 'a8',
    57: 'b8',
    58: 'c8',
    59: 'd8',
    60: 'e8',
    61: 'f8',
    62: 'g8',
    63: 'h8'
}

"""
def getSquareNumber(algebraicNotation):
    return list(identification.keys())[list(identification.values()).index(algebraicNotation)]
"""

squareNumber = {
    'a1': 0,
    'b1': 1,
    'c1': 2,
    'd1': 3,
    'e1': 4,
    'f1': 5,
    'g1': 6,
    'h1': 7,
    'a2': 8,
    'b2': 9,
    'c2': 10,
    'd2': 11,
    'e2': 12,
    'f2': 13,
    'g2': 14,
    'h2': 15,
    'a3': 16,
    'b3': 17,
    'c3': 18,
    'd3': 19,
    'e3': 20,
    'f3': 21,
    'g3': 22,
    'h3': 23,
    'a4': 24,
    'b4': 25,
    'c4': 26,
    'd4': 27,
    'e4': 28,
    'f4': 29,
    'g4': 30,
    'h4': 31,
    'a5': 32,
    'b5': 33,
    'c5': 34,
    'd5': 35,
    'e5': 36,
    'f5': 37,
    'g5': 38,
    'h5': 39,
    'a6': 40,
    'b6': 41,
    'c6': 42,
    'd6': 43,
    'e6': 44,
    'f6': 45,
    'g6': 46,
    'h6': 47,
    'a7': 48,
    'b7': 49,
    'c7': 50,
    'd7': 51,
    'e7': 52,
    'f7': 53,
    'g7': 54,
    'h7': 55,
    'a8': 56,
    'b8': 57,
    'c8': 58,
    'd8': 59,
    'e8': 60,
    'f8': 61,
    'g8': 62,
    'h8': 63
}


def getAlgebraicNotation(square):
    if (not isinstance(square, int)):
        raise TypeError("Type " + str(type(square).__name__) + " received while "
                        + str(int.__name__) + " expected")
    elif (square > 63 or square < 0):
        raise ValueError("This is not a valid square")
    else:
        return identification[square]


def getSquareNumber(algebraicNotation):
    if (not isinstance(algebraicNotation, str)):
        raise TypeError("Type " + str(type(algebraicNotation).__name__) + " received while "
                        + str(str.__name__) + " expected")
    else:
        return squareNumber[algebraicNotation]


def moveNotation(sourcesSquare, destinationSquare, typeOfpiece, typeOfMove, disambiguatingMovesType1
                 , disambiguatingMovesType2, disambiguatingMovesType3, castling, promotingTo, check):
    move = ''

    if check == 1:
        move += '+'

    if check == 2:
        return 'X'

    if castling == 0:
        move += pieces[typeOfpiece]

        if (disambiguatingMovesType1 == 1):
            move += file[int(sourcesSquare % 8)]

        if (disambiguatingMovesType2 == 1):
            move += str(int(math.ceil(sourcesSquare / 8)))

        if (disambiguatingMovesType3 == 1):
            move += getAlgebraicNotation(sourcesSquare)

        if (typeOfMove == 'capture'):
            if (typeOfpiece == 'whitePawns' or typeOfpiece == 'blackPawns'):
                move += file[int(destinationSquare % 8)]
            move += 'x'

        move += getAlgebraicNotation(destinationSquare)

        if (typeOfMove == 'promotion'):
            move += '=' + pieces[promotingTo]

    elif (castling == 1):
        move = 'O-O'
    else:
        move = 'O-O-O'

    return move
