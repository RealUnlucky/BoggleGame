"""
Implements the functionality of a single letter squanre on the Boggle board.
"""

from graphics import *
from board import Board

class BoggleLetter:
    """A Boggle letter has several attributes that define it:
       *  _row, _col coordinates indicate its position in the grid (ints)
       *  _textObj denotes the Text object from the graphics module,
          which has attributes such as size, style, color, etc
          and supports methods such as getText(), setText() etc.
    """

    # add more attributes if needed!
    __slots__ = ['_col', '_row', '_textObj', '_rect' ]

    def __init__(self, board, col=-1, row=-1, letter="", color="black"):
        """
        Construct a new Boggle Letter at the given position on the board,
        and with the optional letter and color.
        """

        # needed for standalone testing (can safely ignore)
        xInset = board.getXInset()
        yInset = board.getYInset()
        size = board.getSize()
        win = board.getWin()

        # set row and column attributes
        self._col = col
        self._row = row

        # make rectangle and add to graphical window
        p1 = Point(xInset + size * col, yInset + size * row)
        p2 = Point(xInset + size * (col + 1), yInset + size * (row + 1))        
        self._rect = board._makeRect(p1, p2, "white")

        # initialize textObj attribute
        self._textObj = Text(self._rect.getCenter(), letter)
        self._textObj.setFill(color) # text color
        self._textObj.draw(win)

    def getRow(self):
        """Returns _col coordinate (int) attribute."""
        # returns the row
        return self._row

    def getCol(self):
        """Returns _col coordinate (int) attribute."""
        # return the column
        return self._col

    def setLetter(self, char):
        """
        Sets the text on the BoggleLetter to char (str) by setting the text
        of the Text object (textObj).
        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = Board(win, rows=4, cols=4)
        >>> let1 = BoggleLetter(board, 1, 1, "A")
        >>> let1.setLetter("B")
        >>> print(let1.getLetter())
        B
        >>> win.close()
        """
        # calls setText to set char as the text in textObj
        self._textObj.setText(char)

    def getLetter(self):
        """
        Returns letter (text of type str) associated with textObj attribute.
        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = Board(win, rows=4, cols=4)
        >>> let1 = BoggleLetter(board, 1, 1, "A")
        >>> print(let1.getLetter())
        A
        >>> win.close()
        """
        # calls getText to find the text currently in textObj
        return self._textObj.getText()

    def setTextColor(self, color):
        """
        Sets the color of the letters' Text object.
        """
        # calls setTextColor to set the color of textObj to color
        self._textObj.setTextColor(color)

    def getTextColor(self):
        """
        Gets the color of the letter's Text object.
        """
        # calls getTextColor to find the text color of textObj
        return self._textObj.getTextColor()

    def setFillColor(self, color):
        """
        Sets the color of the letters' Rectangle object.
        """
        # calls setFillColor to change the color of a rectangle
        return self._rect.setFillColor(color)

    def getFillColor(self):
        """
        Gets the color of the letter's Rectangle object.
        """
        # calls getFillColor to find the current color of a rectangle
        return self._rect.getFillColor()

    # test for adjacency
    def isAdjacent(self, other):
        """
        Given a BoggleLetter other, check if other is adjacent to self.
        Returns True if they are adjacent, and otherwise returns False.
        Two letters are considered adjacent if they are not the same, and
        if their row and col coordinates differ by at most 1.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = Board(win, rows=4, cols=4)
        >>> let1 = BoggleLetter(board, 1, 1, "A")
        >>> let2 = BoggleLetter(board, 1, 2, "B")
        >>> let3 = BoggleLetter(board, 3, 1, "C")
        >>> let1.isAdjacent(let2)
        True
        >>> let2.isAdjacent(let1)
        True
        >>> let3.isAdjacent(let3)
        False
        >>> let3.isAdjacent(let1)
        False
        >>> let2.isAdjacent(let3)
        False
        >>> win.close()
        """
        # returns false if the two squares have the same coordinates
        # this means that a square is not adjacent to itself
        if (other.getCol() - self._col == 0) and (other.getRow() - self._row == 0):
            return False
        # checks if the two squares row and col coordinates each have a difference of 1 or less, meaning that they are considered adjacent (counting diagonals)
        return (abs(other.getCol() - self._col) <= 1) and (abs(other.getRow() - self._row) <= 1)

    def __str__(self):
        """
        Converts a BoggleLetter to a human-readable string.
        Please do not change this method.
        """
        
        return "BoggleLetter({}, {}, '{}', '{}')".format(self._col, self._row, \
                                                self.getLetter(), self.getTextColor())

    def __repr__(self):
        """
        A handy special method that enables Python to print lists
        of BoggleLetter objects nicely.
        Please do not change this method.
        """
        return str(self)


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # # The following code is a larger test.  Uncomment the code
    # # and run it, visually inspecting the results once you
    # # are confident that the class is close to complete.
    #
    from board import Board
    win = GraphWin("Boggle", 400, 400)
    board = Board(win, rows=4, cols=4)
    #
    let1 = BoggleLetter(board, 1, 1, "A")
    let2 = BoggleLetter(board, 1, 2)
    let2.setLetter('B')
    let2.setTextColor("blue")
    let2.setFillColor("powder blue")
    let3 = BoggleLetter(board, 3, 1, "C", color="red")
    let3.setTextColor("dark green")
    let3.setFillColor("DarkSeaGreen1")
    
    # # pause for mouse click before exiting
    point = win.getMouse()
    win.close()
