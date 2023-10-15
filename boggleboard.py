"""
Extends the Board class with specific features required for Boggle
"""

from graphics import *
from brandom import *
from boggleletter import BoggleLetter
from board import Board

class BoggleBoard(Board):
    """Boggle Board class implements the functionality of a Boggle board.
    It inherits from the Board class and extends it by creating a grid
    of BoggleLetters, shaken appropriately to randomize play."""

    __slots__ = ['_grid', "_cubes"]

    def __init__(self, win):
        super().__init__(win, rows=4, cols=4)

        self._cubes =  [[ "A", "A", "C", "I", "O", "T" ],
                        [ "T", "Y", "A", "B", "I", "L" ],
                        [ "J", "M", "O", "Qu", "A", "B"],
                        [ "A", "C", "D", "E", "M", "P" ],
                        [ "A", "C", "E", "L", "S", "R" ],
                        [ "A", "D", "E", "N", "V", "Z" ],
                        [ "A", "H", "M", "O", "R", "S" ],
                        [ "B", "F", "I", "O", "R", "X" ],
                        [ "D", "E", "N", "O", "S", "W" ],
                        [ "D", "K", "N", "O", "T", "U" ],
                        [ "E", "E", "F", "H", "I", "Y" ],
                        [ "E", "G", "I", "N", "T", "V" ],
                        [ "E", "G", "K", "L", "U", "Y" ],
                        [ "E", "H", "I", "N", "P", "S" ],
                        [ "E", "L", "P", "S", "T", "U" ],
                        [ "G", "I", "L", "R", "U", "W" ]]

        # todo: finish __init__ 
        # sets an empty list
        self._grid = []
        # creates a list for each column
        for i in range(self._cols):
            a = []
            # goes through each cell in the column
            for j in range(self._rows):
                # adds an empty BoggleLetter to the list for the column
                a.append(BoggleLetter(self.getBoard(), i, j))
            # appends the list for the column to the list for the grid, creating a list of lists
            self._grid.append(a)
        # fills the grid with letters using shakeCubes
        self.shakeCubes()


    def getBoggleLetterAtPoint(self, point):
        """
        Return the BoggleLetter that contains the given point in the window,
        or None if the click is outside all letters.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = BoggleBoard(win)
        >>> pointIn_0_0 = Point(board.getXInset() + board.getSize() / 2, \
                                board.getYInset() + board.getSize() / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_0_0) == board._grid[0][0]
        True
        >>> pointIn_1_2 = Point(board.getXInset() + board.getSize() * 3 / 2, \
                                board.getYInset() + board.getSize() * 5 / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_1_2) == board._grid[1][2]
        True
        >>> win.close()
        """
        # if the point is in the grid returns the BoggleLetter of the cell the point was in
        if self.inGrid(point):
            (col, row) = self.getPosition(point)
            return self._grid[col][row]
        # if the point is not in the grid, returns none
        else:
            return None

    def resetColors(self):
        """
        "Unclicks" all boggle letters on the board without changing any
        other attributes.  (Change letter colors back to default values.)
        """
        # goes through each column
        for i in range(self._cols):
            # goes through each cell in the column
            for j in range(self._rows):
                # finds the letter at the coordinates of that square
                letter = self._grid[i][j]
                # resets the color of that letter to black and the fill color of the square to white
                letter.setFillColor("white")
                letter.setTextColor("black")


    def reset(self):
        """
        Clears the boggle board by clearing letters and colors,
        clears all text areas (right, lower, upper) on board
        and resets the letters on board by calling shakeCubes.
        """
        
        # resets the color of the grid to white
        self.resetColors() #Resets the colors of each BoggleLetter.
        # sets empty strings to each of the three text areas
        self.setStringToTextArea('') 
        self.setStringToLowerText('')
        self.setStringToUpperText('')
        # shakes the cubes to reset the letters on the board
        self.shakeCubes()

    def shakeCubes(self):
        """
        Shakes the boggle board and sets letters as described by the handout.
        """
        # randomizes the seed for shuffled so that the board doesn't look the same every time
        randomize()
        # shuffles self._cubes so that the letters can be in different squares of the grid
        self._cubes = shuffled(self._cubes)
        # goes through each column and then each cell within that column
        for i in range(self._cols):
            for j in range(self._rows):
                # picks a random number from 0 to 5
                a = randomInt(0, 5)
                # finds the index of the list in self._cubes that is being used for this cell
                # this way none of the lists in self._cubes are used more than once
                num = (j * 4) + i
                # finds a random letter out of that list using the random number "a"
                let1 = self._cubes[num][a]
                # puts that letter into the grid
                self._grid[i][j].setLetter(let1)            
        
 
    def __str__(self):
        """
        Returns a string representation of this BoggleBoard
        """
        board = ''
        for r in range(self._rows):
            for c in range(self._cols):
                boggleLetter = self._grid[c][r]
                color = boggleLetter.getTextColor()
                letter = boggleLetter.getLetter()
                board += '[{}:{}] '.format(letter,color)
            board += '\n'
        return board


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # # Uncomment this code when you are ready to test it!
    
    # # When you are ready to run on different boards,
    # # insert a call to randomize() here.  BUT you will
    # # find it much easier to test your code without
    # # randomizing things!
    
    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard(win)
    print(board)
    
    keepGoing = True
    while keepGoing:
        pt = win.getMouse()
        if board.inExit(pt):
            keepGoing = False
        elif board.inGrid(pt):
            (col, row) = board.getPosition(pt)
            print("{} at {}".format(board._grid[col][row], (pt.getX(), pt.getY())))
