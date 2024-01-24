# menu.py

"""
Title: Menu
Author: Jude and Judy
Date-Created: 2023-12-11
"""
import random

import pygame
import pygame_gui
from highscore_class import Highscore
from general_classes.box import Box
from general_classes.color import Color
from general_classes.window import Window
from general_classes.text import Text
from game1_main import MiniGame1
from game2_main import MiniGame2
from game3_engine import MiniGame3
from general_classes.image_sprite import ImageSprite
# Menu will have a start option and maybe a view highscores, upon start will load a random order / some scaleability with difficulty?

class Menu():

    def __init__(self):
        self.__WINDOW = Window("Multiday Ware", 800, 600, 30)
        self.__MANAGER = pygame_gui.UIManager((800, 600))
        self.__TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((265, 300), (255, 50)), manager=self.__MANAGER, object_id="main_text_entry", visible=False)
        pygame.display.set_mode((800, 600), pygame.SHOWN)

        self.__PLAYER_NAME = "AAA"

        self.__CLOCK = pygame.time.Clock()

        self.__SCORE = 0

        self.__GAME1 = 0
        self.__GAME2 = 0
        self.__GAME3 = 0


        self.__CHOICE = 1
        self.__TESTFONT = "a_fonts/Retro Gaming.ttf"
        self.__SCORE_TEXT = Text(f"YOUR SCORE: {self.__SCORE}", self.__TESTFONT, 20)

        self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__SCORE_TEXT.getWidth() // 2, self.__WINDOW.getHeight() // 2 + 150)

        self.__START = Text("START", self.__TESTFONT, 25)
        self.__EXIT = Text("EXIT", self.__TESTFONT, 25)
        self.__HIGHSCORE_TEXT = Text("HIGHSCORE", self.__TESTFONT, 25)

        self.__START.setPOS(self.__WINDOW.getWidth() // 2 - self.__START.getWidth() // 2,
                            self.__WINDOW.getHeight() // 2)
        self.__HIGHSCORE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__HIGHSCORE_TEXT.getWidth() // 2,
                                     self.__WINDOW.getHeight() // 2 + 50)
        self.__EXIT.setPOS(self.__WINDOW.getWidth() // 2 - self.__EXIT.getWidth() // 2,
                           self.__WINDOW.getHeight() // 2 + 100)

        #HIGHSCORES
        self.__HIGHSCORE = Highscore()
        #self.__FILE = self.__HIGHSCORE.getFileRead()
        self.__HIGHSCORE.setScores()

        self.__LOST_TEXT = Text(f"You didn't beat the High Score: {self.__HIGHSCORE.getScores()[9]}. Play again!",
                                self.__TESTFONT, 10)
        self.__LOST_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__LOST_TEXT.getWidth() // 2,
                                self.__WINDOW.getHeight() // 2 + 200)

        self.__LOGO = ImageSprite("a_media/Untitled(1).png")
        self.__LOGO.setPOS(self.__WINDOW.getWidth()//2 - self.__LOGO.getWidth()//2, -70)


        self.__TITLE_TEXT = Text("Menu", self.__TESTFONT, 40)
        self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2,
                                 240)

        self.__LIVES = 3

        self.__GAME1 = MiniGame1()
        self.__GAME2 = MiniGame2()
        self.__GAME3 = MiniGame3()

        self.__GAME_OVER_TEXT = Text("Game Over", self.__TESTFONT, 40)
        self.__GAME_OVER_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__GAME_OVER_TEXT.getWidth() // 2,
                                 250)
        self.__GAME_OVER = False

        #self.__ENTER_NAME_TEXT = Text("Enter Your Name:", self.__TESTFONT, 30)
        #self.__ENTER_NAME_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__ENTER_NAME_TEXT.getWidth() // 2, 300)

        #self.__ENTER_NAME_BOX = Box(200, 50)
        #self.__ENTER_NAME_BOX.setColor(Color.BLACK)
        #self.__ENTER_NAME_BOX.setPOS(self.__WINDOW.getWidth() // 2 - self.__ENTER_NAME_BOX.getWidth() // 2, 350)



        self.__PREV_GAME = 0

        self.__GAME_NUM = 0
        self.__MULTIPLIER = 0

        self.__ENTERED = False


        ## VIEW HIGHSCORES
        self.__HIGHSCORE_TITLE = Text("Top Players", self.__TESTFONT, 40)
        self.__HIGHSCORE_TITLE.setPOS(self.__WINDOW.getWidth() // 2 - self.__HIGHSCORE_TITLE.getWidth() // 2,
                                 50)
        self.__VIEWHS = False

        self.__ENTER_NAME_TEXT = Text("enter your name ", self.__TESTFONT, 20)
        self.__ENTER_NAME_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__ENTER_NAME_TEXT.getWidth() //2, 350)
        self.__NEW_HIGH_SCORE_TEXT = Text(f"NEW HIGHSCORE! YOUR SCORE: {self.__SCORE}", self.__TESTFONT, 30)

    def getScore(self):
        return self.__SCORE

    def getWin(self, GAME, LIVES, POINTS):
        GAME.__init__()

        if GAME == self.__GAME1:
            self.__PREV_GAME = 1
        if GAME == self.__GAME2:
            self.__PREV_GAME = 2
        if GAME == self.__GAME3:
            GAME.startUp()
            self.__PREV_GAME = 3

        self.__GAME_NUM += 1

        print(f"Game number: {self.__GAME_NUM}")
        if self.__GAME_NUM == 4 or self.__GAME_NUM == 8 or self.__GAME_NUM == 12:
            self.__MULTIPLIER += 1
            print(f"multiplier: {self.__MULTIPLIER}")

        WIN = GAME.run(LIVES, POINTS, self.__MULTIPLIER)

        if WIN:
            return True
        else: # lose the game
            return False

    def runGame(self):
        if self.__LIVES > 0:
            print(f"Points: {self.__SCORE}")
            print(f"Lives: {self.__LIVES}")
            RANDOM = random.randint(1, 3)
            while RANDOM == self.__PREV_GAME:
                RANDOM = random.randint(1, 3)
                print(f"repeated game {self.__PREV_GAME}, new game is {RANDOM}")
                if RANDOM != self.__PREV_GAME:
                    break

            if RANDOM == 1:
                if self.getWin(self.__GAME1, self.__LIVES, self.__SCORE) is True:
                    self.__SCORE += 1
                    self.runGame()
                else:
                    self.__LIVES -= 1
                    self.runGame()

            elif RANDOM == 2:
                if self.getWin(self.__GAME2, self.__LIVES, self.__SCORE) is True:
                    self.__SCORE += 1
                    self.runGame()
                else:
                    self.__LIVES -= 1
                    self.runGame()

            elif RANDOM == 3:
                if self.getWin(self.__GAME3, self.__LIVES, self.__SCORE) is True:
                    self.__SCORE += 1
                    self.runGame()
                else:
                    self.__LIVES -= 1
                    self.runGame()


        else:
            self.__GAME_OVER = True

    def start(self):

        TIME = 0
        while True:
            self.__UI_REFRESH_RATE = self.__CLOCK.tick(60)/100
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.__MANAGER.process_events(event)
                # text will change brightness when selected
                if self.__CHOICE == 1:
                    self.__START.changeAlpha(255)
                    self.__EXIT.changeAlpha(150)
                    self.__HIGHSCORE_TEXT.changeAlpha(150)
                elif self.__CHOICE == 2:
                    self.__START.changeAlpha(150)
                    self.__EXIT.changeAlpha(150)
                    self.__HIGHSCORE_TEXT.changeAlpha(255)
                else:
                    self.__START.changeAlpha(150)
                    self.__EXIT.changeAlpha(255)
                    self.__HIGHSCORE_TEXT.changeAlpha(150)
                PRESSED_KEYS = pygame.key.get_pressed()
                # used to move too many when tapped
                if TIME == 0:
                    if PRESSED_KEYS[pygame.K_d] == 1 or PRESSED_KEYS[pygame.K_s] == 1:
                        self.__CHOICE += 1
                        TIME = 3
                    elif PRESSED_KEYS[pygame.K_a] == 1 or PRESSED_KEYS[pygame.K_w] == 1:
                        self.__CHOICE -= 1
                        TIME = 3
                # small clock to stop flashy menu
                if TIME > 0:
                    TIME -= 1

                if self.__CHOICE > 3:
                    self.__CHOICE = 1
                if self.__CHOICE < 0:
                    self.__CHOICE = 3
                # space bar = confirm
                if PRESSED_KEYS[pygame.K_SPACE] == 1:
                    if self.__CHOICE == 1:
                        if self.__LIVES > 0:
                            self.runGame()
                        """else:
                            self.__GAME_OVER = True"""
                    elif self.__CHOICE == 2:
                        self.__VIEWHS = True

                    elif self.__CHOICE == 3:
                        print("Good Bye.")
                        exit()

                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry":
                    self.__PLAYER_NAME = event.text
                    print(f"entered name: {self.__PLAYER_NAME}")
                    self.__ENTERED = True

            self._updateWindowFrame()



    def _updateWindowFrame(self):
        self.__WINDOW.clearScreen()
        if self.__GAME_OVER == False:
            #
            # put background here
            #
            self.__WINDOW.getSurface().blit(self.__LOGO.getSurface(), self.__LOGO.getPOS())

            # self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__START.getSurface(), self.__START.getPOS())
            self.__WINDOW.getSurface().blit(self.__HIGHSCORE_TEXT.getSurface(), self.__HIGHSCORE_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__EXIT.getSurface(), self.__EXIT.getPOS())

        else: #game over
            self.__HIGHSCORE.setScore(self.__SCORE)
            if self.__HIGHSCORE.checkNewScore(self.__HIGHSCORE.getScores()):
                self.__NEW_HIGH_SCORE_TEXT = Text(f"NEW HIGHSCORE! YOUR SCORE: {self.__SCORE}", self.__TESTFONT, 30)
                self.__NEW_HIGH_SCORE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__NEW_HIGH_SCORE_TEXT.getWidth() // 2, 200)

                self.__WINDOW.getSurface().blit(self.__GAME_OVER_TEXT.getSurface(), self.__GAME_OVER_TEXT.getPOS())
                self.__WINDOW.getSurface().blit(self.__ENTER_NAME_TEXT.getSurface(), self.__ENTER_NAME_TEXT.getPOS())
                self.__WINDOW.getSurface().blit(self.__NEW_HIGH_SCORE_TEXT.getSurface(), self.__NEW_HIGH_SCORE_TEXT.getPOS())


                self.__TEXT_INPUT.show()
                if self.__ENTERED:
                    self.__HIGHSCORE.setName(self.__PLAYER_NAME)
                    self.__TEXT_INPUT.hide()
                    self.__HIGHSCORE.updateHighScore(self.__HIGHSCORE.getScores())
                    self.__HIGHSCORE.writeFile(self.__HIGHSCORE.getScores())
                    self.__TEXT_INPUT.hide()
                    self.__init__() # to restart the game and go back to the menu
            else: # Smaller score
                self.__TEXT_INPUT.hide()
                self.__SCORE_TEXT = Text(f"YOUR SCORE: {self.__SCORE}", self.__TESTFONT, 20)
                self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__SCORE_TEXT.getWidth() // 2,
                                         self.__WINDOW.getHeight() // 2 + 10)
                self.__LOST_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__LOST_TEXT.getWidth() // 2,
                                        self.__WINDOW.getHeight() // 2 + 60)

                for i in range(150):
                    self.__WINDOW.clearScreen()
                    self.__WINDOW.getSurface().blit(self.__GAME_OVER_TEXT.getSurface(), self.__GAME_OVER_TEXT.getPOS())
                    self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())
                    self.__WINDOW.getSurface().blit(self.__LOST_TEXT.getSurface(), self.__LOST_TEXT.getPOS())
                    self.__WINDOW.updateFrame()
                self.__init__()  # to restart the game and go back to the menu

        if self.__VIEWHS == True:
            for i in range(100):
                self.__WINDOW.clearScreen()
                self.__WINDOW.getSurface().blit(self.__HIGHSCORE_TITLE.getSurface(), self.__HIGHSCORE_TITLE.getPOS())

                NUM = 2
                for i in range(len(self.__HIGHSCORE.getScores())):
                    NUM += 1
                    self.__WINDOW.getSurface().blit(pygame.font.Font(self.__TESTFONT, 30).render(f"{self.__HIGHSCORE.getScores()[i]}", True, Color.WHITE), (350, 40*NUM))
                self.__WINDOW.updateFrame()
            self.__init__()  # to restart the game and go back to the menu

        #MANAGER
        self.__MANAGER.update(self.__UI_REFRESH_RATE)
        self.__MANAGER.draw_ui(self.__WINDOW.getSurface())

        self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    MENU = Menu()
    MENU.start()


# Jude's Ideas   for car game make a bunch of yellow boxes (small) that jump at a random velocity and direction
# near the wheels to mimic sparks that might be there. (or something)
# add more people in game 3 (anybody we want)



