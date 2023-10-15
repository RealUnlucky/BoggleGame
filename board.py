'''board.py: The Board class provides a basic game board interface, including
useful methods for creating and manipulating a grid of squares, methods for
converting screen coordinates to grid coordinates and vice versa, and methods
for setting and getting text to/from various locations outside of the grid.  It
also draws an exit and reset button and provides methods for checking for mouse
clicks inside of those regions.'''

from graphics import *

class Board:
    # _win: graphical window on which we will draw our board
    # _xInset: avoids drawing in corner of window
    # _yInset: avoids drawing in corner of window
    # _rows: number of rows in grid of squares
    # _cols: number of columns in grid of squares
    # _size: edge size of each square

    __slots__ = [ '_xInset', '_yInset', '_rows', '_cols', '_size', \
                  '_win', '_exitButton', '_resetButton', \
                  '_textArea', '_lowerWord', '_upperWord']

    def __init__(self, win, xInset=50, yInset=50, rows=3, cols=3, size=50):
        # update class attributes
        self._xInset = xInset; self._yInset = yInset
        self._rows = rows; self._cols = cols
        self._size = size
        self._win = win
        self.drawBoard()

    # getter methods for attributes
    def getWin(self):
        return self._win

    def getXInset(self):
        return self._xInset

    def getYInset(self):
        return self._yInset

    def getRows(self):
        return self._rows

    def getCols(self):
        return self._cols

    def getSize(self):
        return self._size

    def getBoard(self):
        return self

    def __makeTextArea(self, point, fontsize=18, color="black", text=""):
        """Creates a text area"""
        textArea = Text(point, text)
        textArea.setSize(fontsize)
        textArea.setTextColor(color)
        textArea.setStyle("normal")
        textArea.draw(self._win)
        return textArea

    def _makeRect(self, point1, point2, fillcolor="white", text=""):
        """Creates a rectangle with text in the center"""
        rect = Rectangle(point1, point2, fillcolor)
        rect.draw(self._win)
        text = Text(rect.getCenter(), text)
        text.setTextColor("black")
        text.draw(self._win)
        return rect

    def __drawTextAreas(self):
        """Draw the text areas to the right/lower/upper side of main grid"""
        # draw main text area (right of grid)
        self._textArea = self.__makeTextArea(Point(self._xInset * self._rows + self._size * 2,
                                                   self._yInset + 50), 14)
        #draw the text area below grid
        self._lowerWord = self.__makeTextArea(Point(160, 275))
        #draw the text area above grid
        self._upperWord = self.__makeTextArea(Point(160, 25), color="red")

    def __drawGrid(self):
        """Creates a row x col grid, filled with empty squares"""
        for x in range(self._cols):
            for y in range(self._rows):
                # create first point
                p1 = Point(self._xInset + self._size * x, 
                           self._yInset + self._size * y)
                # create second point
                p2 = Point(self._xInset + self._size * (x + 1), 
                           self._yInset + self._size * (y + 1))
                # create rectangle and add to graphical window
                self._makeRect(p1, p2)

                #Text(Point(self._xInset + 15 + self._size * x, \
                #           self._yInset + 15+ self._size * y), \
                #           "{},{}".format(x,y)).draw(win)

    def __drawButtons(self):
        """Create reset and exit buttons"""
        p1 = Point(50, 300); p2 = Point(130, 350)
        self._resetButton = self._makeRect(p1, p2, text="RESET")
        p3 = Point(170, 300); p4 = Point(250, 350)
        self._exitButton = self._makeRect(p3, p4, text="EXIT")        

    def drawBoard(self):
        """Create the board with the grid, text areas, and buttons"""
        self._win.setBackground("white smoke")
        self.__drawGrid()
        self.__drawTextAreas()
        self.__drawButtons()

    # convert Point to grid position (tuple)
    def getPosition(self, point):
        '''
        Converts a window location (Point) to a grid position (tuple).
        Note: Grid positions are always returned as col, row.
        '''
        pX = point.getX()
        pY = point.getY()

        if pY < self._yInset:
            row = -1
        else:
            row = int((pY - self._yInset) / self._size)

        if pX < self._xInset:
            col = -1
        else:
            col = int((pX - self._xInset) / self._size)
        return (col, row)

    # check for click inside specific rectangular region
    def __inRect(self, point, rect):
        '''
        Returns True if a Point (point) exists inside a specific
        Rectangle (rect) on screen.
        '''
        pX = point.getX()
        pY = point.getY()
        rLeft = rect.getP1().getX()
        rTop = rect.getP1().getY()
        rRight = rect.getP2().getX()
        rBottom = rect.getP2().getY()
        return pX > rLeft and pX < rRight and pY > rTop and pY < rBottom

    # check for click in grid
    def inGrid(self, point):
        '''
        Returns True if a Point (point) exists inside the grid of squares.
        '''
        ptX = point.getX()
        ptY = point.getY()
        maxY = self._size * (self._rows + 1)
        maxX = self._size * (self._cols + 1)
        return ptX <= maxX and ptY <= maxY and ptX >= self._xInset and ptY >= self._yInset

    # clicked in exit button?
    def inExit(self, point):
        '''
        Returns true if point is inside exit button (rectangle)
        '''
        return self.__inRect(point, self._exitButton)

    # clicked in reset button?
    def inReset(self, point):
        '''
        Returns true if point is inside exit button (rectangle)
        '''
        return self.__inRect(point, self._resetButton)

    # set text to text area on right
    def getStringFromTextArea(self):
        '''
        Get text from text area to right of grid.
        '''
        return self._textArea.getText()

    # set text to text area on right
    def setStringToTextArea(self, text):
        '''
        Sets text to text area to right of grid. Overwrites existing text.
        '''
        self._textArea.setText(text)

    # add text to text area below grid
    def getStringFromLowerText(self):
        '''
        Get text from text area below grid.
        '''
        return self._lowerWord.getText()


    # add text to text area below grid
    def setStringToLowerText(self, text):
        '''
        Set text to text area below grid.  Overwrites existing text.
        '''
        self._lowerWord.setText( text )

    # add text to text area above grid
    def getStringFromUpperText(self):
        '''
        Get text from text area above grid.
        '''
        return self._upperWord.getText()

    # set text to text area above grid
    def setStringToUpperText(self, text):
        '''
        Set text to text area above grid. Overwrites existing text.
        '''
        self._upperWord.setText(text)

if __name__ == "__main__":
    win = GraphWin("Board", 400, 400)

    # create new board with default values
    board = Board(win)

    # draw Board
    board.drawBoard()

    # set string above grid
    board.setStringToUpperText("Upper text")

    # set and update string below grid
    board.setStringToLowerText("Lower text")

    # set string to text area to right of grid
    board.setStringToTextArea("Text area")

    keepGoing = True
    # loop and return info about mouse clicks until exit is clicked
    while keepGoing:
        # wait for a mouse click
        point = win.getMouse()

        # calculate x and y value from point
        x,y = point.getX(), point.getY()

        # close window and exit if exit button is clicked
        if board.inExit(point):
            print("Exiting...")
            keepGoing = False

        # did we click reset?
        elif board.inReset(point):
            print("Reset button clicked")

        # are we in the grid? if so, print coor and grid position
        elif board.inGrid(point):
            print("Clicked coord {} or grid {}".format((x,y), board.getPosition(point)))

        #else just print info about mouse click
        else:
            print("Clicked coord {} which is not in grid".format((x,y)))

