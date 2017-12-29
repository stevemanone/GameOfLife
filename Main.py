class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.alive = 0


class Board:
    def __init__(self, height, width):
        # Set board height
        self.height = height

        # Set board width
        self.width = width

        #Create board of cells
        self.board = [[Cell(h, w) for h in range(width)] for w in range(height)]

        # To review is a list of squares to review, which encompass the 'alive' cells
        # as as their surrounding cells.
        self.toReview = []


    def __str__(self):
        retStr = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                retStr += self.board[row][col].alive

            retStr += "\n"

    def surroundCells(self, row, col):
        assert(row <= self.height-1 and col <= self.width -1), "Row needs to be between 0 and " \
                                                             "%i and Col needs to be between 0 and " \
                                                             "%i" % (self.height, self.width)
        ret = []
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

                ret.append((r,c))

        return (ret)

    def checkSurroundCell(self,row, col):
        alive = 0
        for (r,c) in self.surroundCells(row,col):
            if self.board[r][c].alive:
                alive += 1
                print(alive,r,c)
        return alive

    def setAlive(self, row, col):
        self.board[row][col].alive = 1

if __name__ == '__main__':
    b = Board(100,100)

    a = b.surroundCells(10,10)

    b.setAlive(5,5)
    b.setAlive(6,6)
    b.setAlive(4,5)
    b.checkSurroundCell(5, 5)

    print(list(a))