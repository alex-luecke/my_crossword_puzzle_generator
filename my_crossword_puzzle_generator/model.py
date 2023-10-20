
class CrossWordPuzzle:
    def __init__(self):
        """Initialize a new crossword puzzle"""
        self.grid_size = 20
        self.words = []
        
    def getWords(self, filename):
        """Input a file with a list of words for the puzzle"""
        self.words = ['testword']
        self.max_length = len(self.words[0])
        
    def buildGrid(self):
        """Create a grid big enough for the words"""
        grid_size = self.max_length + len(self.words)
        self.grid = [[[' ']*grid_size]*grid_size]
        
    def addWords(self):
        """Add the words to the grid"""
        pass
        
    def fillGrid(self):
        """Fill in the blank spaces on the grid with random letters"""
        pass
        
    def randomLetter(self):
        """Generate a random letter with weights for common letters"""
        pass
        
    def printGrid(self):
        """Print out the current grid"""
        for row in self.grid:
            for letter in row:
                print(letter)
                print(' ')
            print('\n')
            
    def buildPuzzle(self):
        """Call the needed functions to build the crossword puzzle"""
        self.getWords('none.txt')
        self.buildGrid()
        self.addWords()
        self.fillGrid()
        self.printGrid()
        