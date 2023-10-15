"""Implements the logic of the game of boggle."""

from graphics import GraphWin
from boggleboard import BoggleBoard
from boggleletter import BoggleLetter
from brandom import randomize

class BoggleGame:

    __slots__ = [ "_validWords", "_board", "_foundWords", "_selectedLetters" ]

    def __init__(self, win):
        """
        Create a new Boggle Game and load in our lexicon.
        """
        # set up the set of valid words we can match
        self._validWords = self.__readLexicon()

        # initializes the attributes of BoggleGame
        self._board = BoggleBoard(win)
        self._foundWords = []
        self._selectedLetters = []

    def __readLexicon(self, lexiconName='bogwords.txt'):
        """
        A helper method to read the lexicon and return it as a set.
        """
        validWords = set()
        with open(lexiconName) as f:
          for line in f:
            validWords.add(line.strip().upper())

        return validWords

    def doOneClick(self, point):
        """
        Implements the logic for processing one click.
        Returns True if play should continue, and False if the game is over.
        """
        # These steps are one way to think about the design, although
        # you are free to do things differently if you prefer.

        # step 1: check for exit button and return False if clicked

        if (self._board.inExit(point)):
            return False

        # step 2: check for reset button and reset
        if (self._board.inReset(point)):
            self._board.reset()

        # step 3: check if click is on a cell in the grid

        # checks if the click is in the grid
        elif self._board.inGrid(point):
            # finds the BoggleLetter of the square the click was in
            letter = self._board.getBoggleLetterAtPoint(point)
            # finds the index of the previous letter clicked
            recentLetter = len(self._selectedLetters) - 1
          # if this is the first letter in a word being constructed,
          # add letter and display it on lower text of board
            # checks if there are no other letters already selected
            if self._selectedLetters == []:
                # adds the letter to selectedLetters and to the the lower text area
                self._selectedLetters.append(letter)
                self._board.setStringToLowerText(letter.getLetter())
                # makes the selected square blue
                letter.setFillColor("Light Blue")
                letter.setTextColor("Dark Blue")

          # else if adding a letter to a non-empty word, make sure it's adjacent
          # and update state
            # checks if the selected letter is the same as the previous letter selected
            elif letter == self._selectedLetters[recentLetter]:
                # sets an empty list to hold the letters in the word
                tempToCombine = []
                # adds the text of each selected letter to tempToCombine
                for let in self._selectedLetters:
                    tempToCombine.append(let.getLetter())
                # checks if the word is a valid word that has not already been found
                if ('').join(tempToCombine) in self._validWords and ('').join(tempToCombine) not in self._foundWords:
                    # finds all the words in the text area already
                    a = self._board.getStringFromTextArea()
                    # adds the word to foundWords
                    self._foundWords.append(('').join(tempToCombine))
                    # adds the word to the text area along with all the words already there
                    self._board.setStringToTextArea(a + '\n' + ('').join(tempToCombine))
                    # finds the current score
                    prevScore = self._board.getStringFromUpperText()
                    # sets the score equal to 0 if the upper text area is blank
                    if prevScore == "":
                        prevScore = 0
                    # makes prevScore an int so it can later be added to the score from the current word
                    else:
                        prevScore = int(prevScore)
                    # finds the length of the current word
                    numLets = len(tempToCombine)
                    # finds the score of the current word using Boggle scoring rules
                    if numLets < 3:
                        score = 0
                    elif numLets < 5:
                        score = 1
                    elif numLets == 5:
                        score = 2
                    elif numLets == 6:
                        score = 3
                    elif numLets == 7:
                        score = 4
                    else:
                        score = 11
                    # adds the score from this word to the previous score and puts the new score in the upper text area
                    self._board.setStringToUpperText(str(prevScore + score))
                # resets the colors of the board
                self._board.resetColors()
                # empties the lower text area
                self._board.setStringToLowerText('')
                # empties selectedLetters
                self._selectedLetters = []
                
            # checks if the letter has already been selected
            # if so, the board, lower text area, and selectedLetters are all reset in order to start finding a new word
            elif letter in self._selectedLetters:
                self._board.resetColors()
                self._board.setStringToLowerText('')
                self._selectedLetters = []

            # checks if the letter is adjacent to the previous letter
            elif letter.isAdjacent(self._selectedLetters[recentLetter]):
                # in this case, the letter is added to selectedLetters
                self._selectedLetters.append(letter)
                # makes a new string of the letters selected so far
                selected = self._board.getStringFromLowerText() + letter.getLetter()
                # sets the lower text area to show that string
                self._board.setStringToLowerText(selected)
                # changes the color of the letter just clicked to blue
                letter.setFillColor("Light Blue")
                letter.setTextColor("Dark Blue")
                # finds the number of selected letters
                numLets = len(self._selectedLetters)
                # changes the color of the previous letter to green
                self._selectedLetters[numLets - 2].setFillColor("Light Green")
                self._selectedLetters[numLets - 2].setTextColor("Dark Green")
           
                
          # else if clicked anywhere else, reset the state to an empty word.
            else:
                self._selectedLetters = []
                self._board.resetColors()
                self._board.setStringToLowerText('')
        # return True to indicate we want to keep 
        return True

if __name__ == '__main__':

    # When you are ready to run on different boards,
    # insert a call to randomize() here.  BUT you will
    # find it much easier to test your code without
    # randomizing things!

    win = GraphWin("Boggle", 400, 400)
    game = BoggleGame(win)
    keepGoing = True
    while keepGoing:
        point = win.getMouse()
        keepGoing = game.doOneClick(point)
