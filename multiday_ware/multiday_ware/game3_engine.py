# game3_engine.py in spotlight_minigame (folder) in multiday_ware(folder)

"""
Title: Spotlight Minigame
Author: Jude and Judy
Date-Created: 2023-12-09
"""


import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent))

from math import pi

import random

from general_classes.text import Text
from spotlight_minigame.enemy import Enemy
from spotlight_minigame.spotlight_sprite import Player
import pygame
import pygame.font
from multiday_ware.general_classes.window import Window
from multiday_ware.general_classes.box import Box
from multiday_ware.general_classes.color import Color
from multiday_ware.general_classes.image_sprite import ImageSprite


pygame.init()

class MiniGame3:

    def __init__(self):
        self.__LIVES = [ImageSprite("a_media/heart.png", 0.4), ImageSprite("a_media/heart.png", 0.4), ImageSprite("a_media/heart.png", 0.4)]

        self.__WINDOW = Window("Testing Game", 800, 600, 30)
        self.__BACKGROUND = ImageSprite("spotlight_media/spotlight_background.png")
        # self.__TEXT = Text("Catch Wario!", "a_fonts/warioware-inc.ttf", 25)

        self.__PLAYER = Player()
        self.__ENEMIES = []
        self.__ENEMIES.append(Enemy("spotlight_media/wario_running_1.png"))
        self.__ENEMIES.append(Enemy("spotlight_media/wario_running_2.png"))

        self.__GHOST = Enemy("spotlight_media/Ghost_Deceit.png")

        self.__BANANA = Enemy("spotlight_media/banana_person.png")

        # GAME ELEMENTS
        self.__PLAYER_HITBOX = Box(100, 100) # is not visible

        self.__WIN = 5 # random variable changed to 0 for loss and 1 for win
        self.__TIME_GAME = Box(800, 30)
        self.__CAUGHT = Box(700, 40)

        self.__TESTFONT = "a_fonts/Retro Gaming.ttf"
        self.__TITLE_BAR = Box(self.__WINDOW.getWidth(), self.__WINDOW.getHeight() // 10)
        self.__TITLE_BAR.setColor(Color.BLACK)
        self.__TITLE_TEXT = Text("Catch Wario!!!", self.__TESTFONT, 35)
        self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2,
                                 12)

        self.__FRAME_WIPE = Box(1000, 1600)

        for live in self.__LIVES:
            live.setPOS(-100, -100)

        self.__START_TEXT = Text("find wario!", self.__TESTFONT, 30)
        self.__START_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__START_TEXT.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__START_TEXT.getHeight()//2 - 100)
        self.__START_TEXT.changeAlpha(0)

    def frameWipe(self):
        self.__FRAME_WIPE.setPOS(0, self.__WINDOW.getHeight() - self.__FRAME_WIPE.getHeight())
        var = 0
        for i in range(10):
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__FRAME_WIPE.getSurface(), self.__FRAME_WIPE.getPOS())
            self.__WINDOW.updateFrame()
        self.__PLAYER.changeAlpha(255)
        for i in range(60):
            var += 10
            self.__FRAME_WIPE.setPOS(0, self.__WINDOW.getHeight() - self.__FRAME_WIPE.getHeight() - var)

            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            for live in self.__LIVES:
                self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())
            self.__WINDOW.getSurface().blit(self.__FRAME_WIPE.getSurface(), self.__FRAME_WIPE.getPOS())
            self.__WINDOW.updateFrame()

        for i in range(60):
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            #self.__WINDOW.getSurface().blit(self.__START_TEXT.getSurface(), self.__START_TEXT.getPOS())
            for live in self.__LIVES:
                self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())
            self.__WINDOW.getSurface().blit(self.__FRAME_WIPE.getSurface(), self.__FRAME_WIPE.getPOS())
            self.__WINDOW.updateFrame()
        #self.__START_TEXT.changeAlpha(0)

        # each game starts with screen covered by image (image.setPOS()) and then it slides away
        # ends with screen getting covered


    def frameWipeOut(self):
        self.__FRAME_WIPE.setPOS(0, 0-self.__FRAME_WIPE.getHeight())
        var = 0
        for i in range(10):
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__FRAME_WIPE.getSurface(), self.__FRAME_WIPE.getPOS())
            self.__WINDOW.updateFrame()
        self.__PLAYER.changeAlpha(255)
        for i in range(60):
            var += 10
            self.__FRAME_WIPE.setPOS(0, 0-self.__FRAME_WIPE.getHeight()+var)

            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            for live in self.__LIVES:
                self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())
            self.__WINDOW.getSurface().blit(self.__FRAME_WIPE.getSurface(), self.__FRAME_WIPE.getPOS())
            self.__WINDOW.updateFrame()
    def advFrameWipe(self):
        """
        will use pygame to draw on the screen, possibly a game like TRON (just testing right now)
        :return:
        """
        done = False
        clock = pygame.time.Clock()

        while not done:
            # This limits the while loop to a max of 60 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Draw on the screen a green line from (0, 0) to (50, 30)
            var = 0
            for i in range(60):
                var += 10
            pygame.draw.line(self.__WINDOW.getSurface(), (60, 179, 113), [0, 100], [var, 60], 7)
            pygame.draw.ellipse(self.__WINDOW.getSurface(), "red", [225, 10, 50, 20], 2)
            pygame.display.flip()
        pygame.quit()

    def introFrames(self):
        # ANIMATION THAT PLAYS BEFORE THE GAME BEGINS
        self.__PLAYER.changeAlpha(255)
        self.__PLAYER.setX(self.__WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2)
        self.__PLAYER.setY(self.__WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2)

        for i in range(60): # player (spotlight) moves left
            self.__PLAYER.setPOS(self.__PLAYER.getPOS()[0] - 5, self.__PLAYER.getPOS()[1])
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            for live in self.__LIVES:
                self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())
            self.__WINDOW.updateFrame()
        for i in range(2):
            self.__ENEMIES[i].setPOS(self.__WINDOW.getWidth() // 2 - 20, self.__WINDOW.getHeight() // 2 - self.__ENEMIES[i].getHeight())
        for i in range(30): # player moves right
            self.__PLAYER.setPOS(self.__PLAYER.getPOS()[0] + 10, self.__PLAYER.getPOS()[1])
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
            self.__WINDOW.getSurface().blit(self.__ENEMIES[0].getSurface(), self.__ENEMIES[0].getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            for live in self.__LIVES:
                self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())
            self.__WINDOW.updateFrame()
        for i in range(10): # still frames
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
            self.__WINDOW.getSurface().blit(self.__ENEMIES[0].getSurface(), self.__ENEMIES[0].getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            for live in self.__LIVES:
                self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())
            self.__WINDOW.updateFrame()

        self.__PLAYER.changeAlpha(200)
    def startUp(self):

        self.__CAUGHT.setColor(Color.YELLOW)
        self.__CAUGHT.setPOS(self.__WINDOW.getWidth() // 2 - self.__CAUGHT.getWidth() // 2, self.__WINDOW.getHeight() - self.__CAUGHT.getHeight() - 20)
        self.__PLAYER.setScale(6.05)
        self.__PLAYER.setX(self.__WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2)
        self.__PLAYER.setY(self.__WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2)

        RAND_HEIGHT = random.randint(0, self.__WINDOW.getHeight())
        RAND_WIDTH = random.randint(0, self.__WINDOW.getWidth())
        for i in range(len(self.__ENEMIES)):
            self.__ENEMIES[i].setScale(3.5)
            self.__ENEMIES[i].setX(self.__WINDOW.getWidth() // 2 - self.__ENEMIES[i].getWidth() // 2)
            self.__ENEMIES[i].setY(self.__WINDOW.getHeight() // 2 - self.__ENEMIES[i].getHeight() // 2)
            self.__ENEMIES[i].setPOS(RAND_WIDTH, RAND_HEIGHT)

        # --- DISTRACTING PEOPLE --- #
        #self.__GHOST.setSPD(3)
        self.__GHOST.setScale(1)


        #self.__BANANA.setSPD(6)
        self.__BANANA.setScale(1.3)
        self.__BANANA.setPOS(random.randint(0, self.__WINDOW.getWidth() - self.__BANANA.getWidth()),
                      random.randint(0, self.__WINDOW.getHeight() - self.__BANANA.getHeight()))


    def run(self, LIVES, SCORE, MULTIPLIER):
        self.__SCORE_TEXT = Text(f"SCORE: {SCORE}", self.__TESTFONT, 20)
        self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 20, 20)

        #print("running")
        FRAME = 1
        TIMER = 0

        # self.startUp()
        # self.advFrameWipe()  will draw lines on window... for the game
        self.frameWipe()
        # possibly at the end of each game, and then each game starts with it sliding up
        # [ game 1 (end frames) --> game 2 (start frames) ]
        self.introFrames()

        # LIVES
        if LIVES == 1:
            self.__LIVES[0].setPOS(20, 10)
        if LIVES == 2:
            self.__LIVES[0].setPOS(20, 10)
            self.__LIVES[1].setPOS(55, 10)
        if LIVES == 3:
            self.__LIVES[0].setPOS(20, 10)
            self.__LIVES[1].setPOS(55, 10)
            self.__LIVES[2].setPOS(90, 10)

        self.__GHOST.setSPD(3 + 3*MULTIPLIER)
        self.__BANANA.setSPD(6 + 3*MULTIPLIER)
        for i in range(len(self.__ENEMIES)):
            self.__ENEMIES[i].setSPD(6)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            TIME_SIZE = self.__TIME_GAME.getWidth() - 4 - MULTIPLIER # gets faster (less time) as games go on
            if TIME_SIZE > 0:
                self.__TIME_GAME = Box(TIME_SIZE, 30)
                self.__TIME_GAME.setPOS(0, 50)
            if self.__TIME_GAME.getWidth() < 20:
                self.__WIN = 0
                self.frameWipeOut()
                return False
                #print("lose")
            # timer causes loss. catching bar causes win. (by getting below a height)
            if self.__WIN == 1:
                self.frameWipeOut()
                return True


            KEYS_PRESSED = pygame.key.get_pressed()
            self.__PLAYER.SPOTLIGHTmove(KEYS_PRESSED)
            self.__PLAYER.checkBoundaries(self.__WINDOW.getWidth() + 625, self.__WINDOW.getHeight() + 675, -650, -600)
            self.__PLAYER_HITBOX.setPOS(self.__PLAYER.getPOS()[0] + 690, self.__PLAYER.getPOS()[1] + 635)

            RANDOM = int(random.randint(0, 12))
            if RANDOM == 1:
                for i in range(2):
                    self.__ENEMIES[i].changeDirY()
                    self.__ENEMIES[i].changeDirX()

            self.__GHOST.setSPD(5 * MULTIPLIER)
            self.__GHOST.bounceX(self.__WINDOW.getWidth())
            self.__GHOST.bounceY(self.__WINDOW.getHeight())

            if self.__PLAYER_HITBOX.isCollision(self.__ENEMIES[0].getWidth(), self.__ENEMIES[0].getHeight(), self.__ENEMIES[0].getPOS()) == True:
                self.__CAUGHT = Box(self.__CAUGHT.getWidth() - 5 - 3 * MULTIPLIER, self.__CAUGHT.getHeight())
                self.__CAUGHT.setColor(Color.YELLOW)  # will set the box to be smaller if it was collisioned
                self.__CAUGHT.setPOS(self.__WINDOW.getWidth() // 2 - self.__CAUGHT.getWidth() // 2,
                              self.__WINDOW.getHeight() - self.__CAUGHT.getHeight() - 20)
                if self.__CAUGHT.getWidth() < 20:
                    self.__CAUGHT.setPOS(-100, -100)
                    self.__WIN = 1

            if FRAME == 1:
                TIMER += 1
                if TIMER > 10:
                    FRAME = 2
                    TIMER = 0
                    self.__BANANA.setImageDirX(True)
            if FRAME == 2:
                TIMER += 1
                if TIMER > 10:
                    FRAME = 1
                    TIMER = 0
                    self.__BANANA.setImageDirX(False)

            for i in range(len(self.__ENEMIES)):
                self.__ENEMIES[i].bounceX(self.__WINDOW.getWidth())
                self.__ENEMIES[i].bounceY(self.__WINDOW.getHeight())
###################### FRAMES AND SOFORTH ####################
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())

            if FRAME == 1:

                self.__WINDOW.getSurface().blit(self.__ENEMIES[0].getSurface(), self.__ENEMIES[0].getPOS())
            else:

                self.__WINDOW.getSurface().blit(self.__ENEMIES[1].getSurface(), self.__ENEMIES[1].getPOS())
            self.__WINDOW.getSurface().blit(self.__GHOST.getSurface(), self.__GHOST.getPOS())

            self.__WINDOW.getSurface().blit(self.__BANANA.getSurface(), self.__BANANA.getPOS())

            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())  # should be above everything else
            self.__WINDOW.getSurface().blit(self.__CAUGHT.getSurface(), self.__CAUGHT.getPOS())
            # self.__WINDOW.getSurface().blit(self.__PLAYER_HITBOX.getSurface(), self.__PLAYER_HITBOX.getPOS())
            self.__WINDOW.getSurface().blit(self.__TIME_GAME.getSurface(), self.__TIME_GAME.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())

            for live in self.__LIVES:
                self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())

            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    GAME = MiniGame3()
    GAME.frameWipe()
    GAME.run(3, 2, 3)
