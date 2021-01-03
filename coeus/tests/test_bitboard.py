import coeus.bitboard.bitboard as b

import coeus.bitboard.show_bitboard as sb

a= b.BitBoard('Classic')

sb.show_board(a)

sb.show_board_console(a)

a= b.BitBoard('')

sb.show_board(a)

sb.show_board_console(a)

