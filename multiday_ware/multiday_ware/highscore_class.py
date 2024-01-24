# highscore_class.py in multiday (folder)
"""
Title: Highscore Class
Author: Jude and Judy
Date: 2023-12-22
"""
class Highscore():
    def __init__(self):
        self.__FILENAME = "highscores.txt"
        self.__SCORE = 0
        self.__NAME = ""
        self.__SCORES = []

    def getFileName(self):
        return self.__FILENAME

    def menu(self):
        """
        user chooses an operation
        :return: int
        """
        print("""
    1. View Scores
    2. Add New Score
    3. Exit
        """)
        CHOICE = input("> ")
        if CHOICE.isnumeric:
            CHOICE = int(CHOICE)
        else:
            print("Please enter a number.")
            return self.menu()
        if 0 < CHOICE < 4:
            return CHOICE
        else:
            print("Please enter a number from the list.")
            return self.menu()

    def checkInt(self):
        """
        Verifies the number is an integer
        :param NUMBER: (str)
        :return: (int)
        """
        if self.__SCORE.isnumeric():
            return int(self.__SCORE)
        else:
            print("That is not a number")
            NEW_NUM = input("Please enter a valid number : ")
            return self.checkInt(NEW_NUM)

    def getFileRead(self):
        """
        Open the score file and create one if it doesn't exist yet.
        :return: (Object)
        """
        try:
            FILE = open(self.__FILENAME, "x")
            START_SCORE = []
            for i in range(10):
                START_SCORE.append("AAA 0")
            START_SCORE_TEXT = ",".join(START_SCORE)
            FILE.write(START_SCORE_TEXT)
            FILE.close()
        except FileExistsError:
            pass

        FILE = open(self.__FILENAME)
        return FILE

    def getName(self):
        """
        Asks the user for their name
        :return: NAME (string)
        """
        self.__NAME = input("Name: ")
        self.__NAME = self.__NAME.upper()
        if len(self.__NAME) > 3:
            self.__NAME = self.__NAME[:3]
        return self.__NAME

    ## ---Processing--- ##
    def readFile(self, FILE_OBJECT):
        """
        reading the contents of the file.
        :param FILE_OBJECT:  (object)
        :return: SCORE_ARRAY (list)
        """
        TEXT = FILE_OBJECT.read()
        FILE_OBJECT.close()
        SCORE_ARRAY = TEXT.split(",")
        return SCORE_ARRAY

    def checkNewScore(self, SCORE_ARRAY):
        """
        checks whether the new score is a high score
        :param SCORE: (int)
        :param SCORE_ARRAY: (list)
        :return: bool
        """
        SCORE_ARRAY_2D = []
        # Creates a 2D array with the scores set as integers
        for i in range(len(SCORE_ARRAY)):
            SCORE_ARRAY_2D.append(SCORE_ARRAY[i].split())
            SCORE_ARRAY_2D[-1][1] = int(SCORE_ARRAY_2D[-1][1])

        for i in range(len(SCORE_ARRAY_2D)):
            if self.__SCORE >= SCORE_ARRAY_2D[i][1]:
                return True
        return False



    def updateHighScore(self, SCORE_ARRAY):
        """
        Updates the score list with the new score
        :param SCORE: (int)
        :param NAME: (str)
        :param SCORE_ARRAY: (list)
        :return: (list)
        """
        SCORE_ARRAY_2D = []
        # Creates a 2D array with the scores set as integers
        for i in range(len(SCORE_ARRAY)):
            SCORE_ARRAY_2D.append(SCORE_ARRAY[i].split())
            SCORE_ARRAY_2D[-1][1] = int(SCORE_ARRAY_2D[-1][1])

        for i in range(len(SCORE_ARRAY)):
            if self.__SCORE > SCORE_ARRAY_2D[i][1]:
                SCORE_ARRAY.insert(i, f"{self.__NAME.upper()} {self.__SCORE}")
                SCORE_ARRAY.pop()
                return SCORE_ARRAY


    ## ---Outputs--- ##
    def viewScores(self):
        """
        Displays the scores nicely
        :param SCORES: (List)
        :return:
        """
        print("High Scores")
        for i in range(len(self.__SCORES)):
            print(f"{i+1}. {self.__SCORES[i]} ")

    def writeFile(self, SCORE_ARRAY):
        """
        Writes the changes to the file
        :param SCORE_ARRAY: (list)
        :return:
        """
        FILE = open(self.__FILENAME, "w")
        SCORE_TEXT = ",".join(SCORE_ARRAY)
        FILE.write(SCORE_TEXT)
        FILE.close()
        #print("Score Successfully Saved.")

    def setScore(self, SCORE):
        self.__SCORE = SCORE


    def setName(self, NAME):
        self.__NAME = NAME
        print(f"{self.__NAME}")

    def setScores(self):
        FILE = self.getFileRead()
        self.__SCORES = self.readFile(FILE)
        return self.__SCORES

    def getScores(self):
        return self.__SCORES

    def getScore(self):
        return self.__SCORE

    ### - - - MAIN CODE - - - ###
if __name__ == "__main__":
    HIGHSCORE = Highscore()
    FILE = HIGHSCORE.getFileRead()
    HIGHSCORE.setScores()
    while True:
        CHOICE = HIGHSCORE.menu()
        if CHOICE == 1:
            HIGHSCORE.viewScores()
        elif CHOICE == 2:
            #HIGHSCORE.setScore(HIGHSCORE.getScore())
            if HIGHSCORE.checkNewScore(HIGHSCORE.getScores()):
                print("New Highscore!")
                NAME = HIGHSCORE.getName()
                SCORES = HIGHSCORE.updateHighScore(HIGHSCORE.getScores())
                HIGHSCORE.writeFile(HIGHSCORE.getScores())
            else:
                print("Score is not good enough, victory is on the horizon.")
        elif CHOICE == 3:
            exit()

