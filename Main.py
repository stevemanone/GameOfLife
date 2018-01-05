#Cell is a basic unit which contains a coordinate and a binary property, 'alive'
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.alive = 0


#Creates the board, which is a 2D array of 'cells'.
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
        self.toReview = set()

    #String representation of board
    def __str__(self):
        retStr = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                # if (str(self.board[row][col].alive))
                retStr += str(self.board[row][col].alive)


            retStr += "\n"

        return retStr

    #Returns a list of surrounding cell locations.  Cells on the edge of the plane are 'wrapped'.
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

    #Checks surrounding cells and returns the number of alive cells
    def checkSurroundCell(self,row, col):
        aliveCounter = 0

        for (r,c) in self.surroundCells(row,col):
            # print(self.board[r][c], r, c)
            if ((r,c) != (row,col)) and (self.board[r][c].alive == 1) :
                aliveCounter += 1
        # print(aliveCounter)
        return aliveCounter

    #Sets certain cell to alive
    def setAlive(self, row, col):
        self.board[row][col].alive = 1

        for (r,c) in self.surroundCells(row, col):
            # print(r,c)
            self.toReview.add((r,c))

    #Inputs cell location to kill
    def killCell(self, row, col):
        self.board[row][col].alive = 0

    # Step where actual game logic occurs, cells become 'alive' or 'dead' based on itself and the state of
    # the cells around it.
    def runStep(self):
        temp = list(self.toReview)
        toKill = []
        toAlive = []

        for (r,c) in temp:
            currentCellStatus = self.board[r][c].alive
            surroundCells = self.checkSurroundCell(r, c)
            # print(r,c,currentCellStatus,surroundCells)
            if (currentCellStatus == 1) and ((surroundCells < 2) or (surroundCells > 3)):
                toKill.append((r,c))

            elif (currentCellStatus == 0) and (surroundCells == 3):
                toAlive.append((r,c))

            if (currentCellStatus == 0) and self.checkSurroundCell(r, c) == 0:
                    self.toReview.remove((r,c))

        for (r,c) in toKill:
            self.killCell(r,c)
        for (r,c) in toAlive:
            self.setAlive(r,c)


if __name__ == '__main__':
    b = Board(20,20)
    b.setAlive(10,3)
    b.setAlive(10,5)
    b.setAlive(10, 7)

    b.setAlive(9, 5)
    b.setAlive(11, 5)


    for i in range(5):
        print(b)
        b.runStep()

