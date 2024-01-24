# minigame_game_engine.py in asteroid_minigame
"""
title: Minigame #1 Game Engine
author: Jude Andersen, Judy Zhu
date-created: 2023-11-30
"""

import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent))


from random import randrange

import pygame
import pygame.font

from general_classes.box import Box
from multiday_ware.general_classes.color import Color
from multiday_ware.asteroid_minigame.enemy_sprite import Enemy
from multiday_ware.general_classes.image_sprite import ImageSprite
from multiday_ware.general_classes.text import Text
from multiday_ware.general_classes.window import Window
from multiday_ware.asteroid_minigame.player_sprite import Player
from multiday_ware.general_classes.box import Box

pygame.init()

TESTFONT = "a_fonts/Retro Gaming.ttf"

class MiniGame1:
    def __init__(self):
        self.__WINDOW = Window("Dodging Cars Minigame", 800, 600, 30)
        self.__BG = ImageSprite("a_media/road_background.png")
        self.__BG.setScale(0.37)
        self.__BG.setPOS(0, self.__WINDOW.getHeight() // 10)
        self.__BG.changeAlpha(150)
        self.__TIME_GAME = Box(800, 30)
        self.__WIN = 5 # random variable changed to 0 for loss and 1 for win

        self.__PLAYER = Player()
        self.__PLAYER.setX(-170)
        self.__PLAYER.setY(self.__WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2)
        self.__PLAYER.setImageDirX(False)
        self.__TITLE_BAR = Box(self.__WINDOW.getWidth(), self.__WINDOW.getHeight() // 10)

        self.__TITLE_BAR.setColor(Color.BLACK)
        self.__TITLE_TEXT = Text("DODGING CARS MINIGAME", TESTFONT, 25)
        self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2,
                                 12)
        self.__LIVES = [ImageSprite("a_media/heart.png", 0.4), ImageSprite("a_media/heart.png", 0.4), ImageSprite("a_media/heart.png", 0.4)]
        for live in self.__LIVES:
            live.setPOS(-100, -100)




        self.__GAME_OVER = False
        self.__GAME_OVER_TEXT = Text("Game Over", TESTFONT)
        self.__GAME_OVER_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__GAME_OVER_TEXT.getWidth() // 2,
                                     self.__WINDOW.getHeight() // 2 - self.__GAME_OVER_TEXT.getHeight() // 2)

        self.__CARS = []
        for i in range(3):
            self.__CARS.append(Enemy())
            RAND = randrange(100, 300)
            self.__CARS[i].setY(RAND)
            #RANDOM = randrange(50, 400)



            #self.__CARS[-1].setAngleRatios(self.__WINDOW.getWidth()//2, self.__WINDOW.getHeight()//2)
            #self.__CARS[-1].setAngle(15)
            """self.__CARS[-1].OGY = 100
            self.__CARS[-1].setY(self.__CARS[-1].OGY)"""
            self.__CARS[i].setSPD(randrange(4, 8))
        self.__FRAME_WIPE = Box(1000, 1600)

        self.__CARS[0].setX(self.__WINDOW.getWidth() + 50)
        self.__CARS[1].setX(self.__WINDOW.getWidth() + 200)
        self.__CARS[2].setX(self.__WINDOW.getWidth() + 400)

        self.__START_TEXT = Text("dodge!", TESTFONT, 30)
        self.__START_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__START_TEXT.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__START_TEXT.getHeight()//2)
        self.__START_TEXT.changeAlpha(0)
    def frameWipe(self):
        self.__FRAME_WIPE.setPOS(0, self.__WINDOW.getHeight() - self.__FRAME_WIPE.getHeight())


        var = 0
        for i in range(10):
            self.__updateWindowFrame()
        for i in range(60):
            var += 10
            self.__FRAME_WIPE.setPOS(0, self.__WINDOW.getHeight() - self.__FRAME_WIPE.getHeight() - var)
            self.__updateWindowFrame()

    def frameWipeOut(self):
        self.__FRAME_WIPE.setPOS(0, 0-self.__FRAME_WIPE.getHeight())
        var = 0
        for i in range(10):
            self.__updateWindowFrame()
        for i in range(60):
            var += 10
            self.__FRAME_WIPE.setPOS(0, 0-self.__FRAME_WIPE.getHeight()+var)
            self.__updateWindowFrame()

    def introFrames(self):
        self.__WINDOW.clearScreen()
        # text
        for i in range(60):
            self.__START_TEXT.changeAlpha(0+i*10)
            self.__updateWindowFrame()
        self.__START_TEXT.changeAlpha(0)

        for i in range(55):
            self.__PLAYER.setX(self.__PLAYER.getPOS()[0] + 3)
            self.__updateWindowFrame()



    def run(self, LIVES, SCORE, MULTIPLIER):

        self.__SCORE_TEXT = Text(f"SCORE: {SCORE}", TESTFONT, 20)
        self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 20, 20)
        self.frameWipe()

        if LIVES == 1:
            self.__LIVES[0].setPOS(20, 10)
        if LIVES == 2:
            self.__LIVES[0].setPOS(20, 10)
            self.__LIVES[1].setPOS(55, 10)
        if LIVES == 3:
            self.__LIVES[0].setPOS(20, 10)
            self.__LIVES[1].setPOS(55, 10)
            self.__LIVES[2].setPOS(90, 10)

        for i in range(MULTIPLIER):
            #SPD = randrange(4, 7) + 3 * MULTIPLIER
            #car.setSPD(SPD)
            #print(SPD)

            self.__CARS.append(Enemy())

            self.__CARS[-1].setY(randrange(100, 300))


            self.__CARS[-1].setX(self.__WINDOW.getWidth() + 200*i)
            self.__CARS[-1].setSPD(randrange(4, 8))
        print(f"num of cars: {len(self.__CARS)}")
        # intro frames
        self.introFrames()


        while True:
            # -- INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            KEYS_PRESSED = pygame.key.get_pressed()


            ### TIME BOX
            TIME_SIZE = self.__TIME_GAME.getWidth() -4 + MULTIPLIER
            if TIME_SIZE > 0:
                self.__TIME_GAME = Box(TIME_SIZE, 30)
                self.__TIME_GAME.setPOS(0, 50)
            if self.__TIME_GAME.getWidth() < 20:
                self.__WIN = 1
                #print("win")



            # -- PROCESSING
            self.__PLAYER.moveUpDown(KEYS_PRESSED)
            self.__PLAYER.checkBoundaries(0, self.__WINDOW.getHeight(), 0, 200)

            for car in self.__CARS:
                car.marqueeAngle(self.__WINDOW.getWidth())
                """print(f"x: {car.OGX}")
                print(f"y: {car.OGY}")"""

            #CHECK WIN
            if self.__WIN == 1:
                self.frameWipeOut()
                return True
            elif self.__WIN == 0:
                self.frameWipeOut()
                return False

            self.__updateWindowFrame()



    def __playerCarCollision(self):
        for i in range(len(self.__CARS)):
            if self.__CARS[i].maskOverlap(self.__PLAYER.MASK, self.__PLAYER.getPOS()):
                # MOVE CAR
                self.__CARS[i] = Enemy()
                self.__CARS[i].setY(randrange(100, 300))
                self.__CARS[i].setX(self.__WINDOW.getWidth()+self.__CARS[-1].getWidth())

                # REMOVE A LIFE
                self.__WIN = 0


                # GAME OVER
                self.__GAME_OVER = True

    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()
        self.__WINDOW.getSurface().blit(self.__BG.getSurface(), self.__BG.getPOS())
        self.__WINDOW.getSurface().blit(self.__START_TEXT.getSurface(), self.__START_TEXT.getPOS())

        # -- LAYOUTING
        self.__WINDOW.getSurface().blit(self.__TIME_GAME.getSurface(), self.__TIME_GAME.getPOS())
        self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
        self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())

        ### LIVES
        for live in self.__LIVES:
            self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())



        if not self.__GAME_OVER:
            # --- SPRITES
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            # --- CAR SPRITES
            for car in self.__CARS:
                self.__WINDOW.getSurface().blit(car.getSurface(), car.getPOS())




        if self.__GAME_OVER:
            self.__WINDOW.getSurface().blit(self.__GAME_OVER_TEXT.getSurface(),
                                            self.__GAME_OVER_TEXT.getPOS())

        # --- COLLISIONS
        self.__playerCarCollision()

        ### FRAME WIPE
        self.__WINDOW.getSurface().blit(self.__FRAME_WIPE.getSurface(), self.__FRAME_WIPE.getPOS())

        self.__WINDOW.updateFrame()




if __name__ == "__main__":
    GAME = MiniGame1()
    GAME.run(3, 0, 2)



