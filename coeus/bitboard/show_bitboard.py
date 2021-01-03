import tkinter as tk

def show_board(self):
    root = tk.Tk()

    for i in range(8):
        text_var = tk.StringVar()
        text_var.set('%s' % str(8-i))
        tk.Label(root, textvariable=text_var, justify='center'
                 , width=2, font=('Verdana',20)).grid(row=i, column=0)

    for j in range(8):
        text_var = tk.StringVar()
        text_var.set('%s' % chr(65+j))
        tk.Label(root, textvariable=text_var, justify='center'
                 , width=2, font=('Verdana',20)).grid(row=9, column=j+1)

    for i in range(8):
        for j in range(8):
            text_var = tk.StringVar()
            cnt = i*8+j
            if self.allPieces[cnt] is False:
                text_var.set('%s' % '')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.whitePawns[cnt]:
                text_var.set('%s' % u'\u2659')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.whiteRooks[cnt]:
                text_var.set('%s' % u'\u2656')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.whiteKnights[cnt]:
                text_var.set('%s' % u'\u2658')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.whiteBishops[cnt]:
                text_var.set('%s' % u'\u2657')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.whiteQueens[cnt]:
                text_var.set('%s' % u'\u2655')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.whiteKing[cnt]:
                text_var.set('%s' % u'\u2654')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.blackPawns[cnt]:
                text_var.set('%s' % u'\u265F')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.blackRooks[cnt]:
                text_var.set('%s' % u'\u265C')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.blackKnights[cnt]:
                text_var.set('%s' % u'\u265E')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.blackBishops[cnt]:
                text_var.set('%s' % u'\u265D')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.blackQueens[cnt]:
                text_var.set('%s' % u'\u265B')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
            elif self.allPieces[cnt] == self.blackKing[cnt]:
                text_var.set('%s' % u'\u265A')
                tk.Label(root, textvariable=text_var, justify='center'
                         , width=2, font=('Verdana',20), borderwidth=2, relief="solid").grid(row=i, column=j+1)
    tk.mainloop()


def show_board_console(self):
    """Depicts the current state of the board"""
    rank = 9
    page = '\n   A BC D EF G H\n'
    for i in range(64):
        if i % 8 == 0:
            rank -= 1
            print()
            print(rank, end='  ')
        if self.allPieces[i] is False:
            print('', end='')
        else:
            if self.allPieces[i] == self.whitePawns[i]:
                print(u'\u2659', end='')
            elif self.allPieces[i] == self.whiteRooks[i]:
                print(u'\u2656', end='')
            elif self.allPieces[i] == self.whiteKnights[i]:
                print(u'\u2658', end='')
            elif self.allPieces[i] == self.whiteBishops[i]:
                print(u'\u2657', end='')
            elif self.allPieces[i] == self.whiteQueens[i]:
                print(u'\u2655', end='')
            elif self.allPieces[i] == self.whiteKing[i]:
                print(u'\u2654', end='')
            elif self.allPieces[i] ==self.blackPawns[i]:
                print(u'\u265F', end='')
            elif self.allPieces[i] == self.blackRooks[i]:
                print(u'\u265C', end='')
            elif self.allPieces[i] == self.blackKnights[i]:
                print(u'\u265E', end='')
            elif self.allPieces[i] == self.blackBishops[i]:
                print(u'\u265D', end='')
            elif self.allPieces[i] == self.blackQueens[i]:
                print(u'\u265B', end='')
            elif self.allPieces[i] == self.blackKing[i]:
                print(u'\u265A', end='')
    print(page)