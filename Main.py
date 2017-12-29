import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.alive = False


class Board:
    def __init__(self, height, width):
        # Set board height
        self.height = height

        # Set board width
        self.width = width

        #Create board of cells
        self.board = [[Cell(h, w) for h in range(width)] for w in range(height)]


    def evalCell(self, row, col):
        aliveCount = 0
        for c in [col-1, col, col+1]:
            if (col==0 and c == -1):
                c = self.width-1

            if (col == self.width-1 and c == self.width):
                c = 0

            for r in [row -1, row, row+1]:

                if (row == 0 and r == -1):
                    r = self.height - 1

                if (row == self.height-1 and r == self.height):
                    r = 0


                if self.board[r][c].alive == True:
                    aliveCount += 1
                    print("Alive found at %s,%s" % (r, c))

        return aliveCount


    def setAlive(self, row, col):
        self.board[row][col].alive = True

if __name__ == '__main__':
    maxR = 100
    maxC = 100
    b = Board(100,100)

    b.setAlive(99,0)
    print(b.evalCell(0,0))

    X = b

    fig, ax = plt.subplots()
    ax.imshow(X.board, interpolation='none')

    numrows, numcols = X.height, X.width


    def format_coord(x, y):
        col = int(x + 0.5)
        row = int(y + 0.5)
        if col >= 0 and col < numcols and row >= 0 and row < numrows:
            z = X.board[row][col]
            return 'x=%1.4f, y=%1.4f, z=%1.4f' % (x, y, z)
        else:
            return 'x=%1.4f, y=%1.4f' % (x, y)

    ax.format_coord = format_coord
    plt.show()