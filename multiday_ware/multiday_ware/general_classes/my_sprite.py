# my_sprite.py in multiday_ware
"""
title: Abstract Sprite Class
author: Jude Andersen, Judy Zhu
date-created: 2023-11-29
"""
import pygame
from random import *


class MySprite:
    """
    abstract sprite class to build other sprites
    """

    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPEED=5, COLOR=(255, 255, 255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self._DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self._COLOR = COLOR  # White
        self._SPD = SPEED
        self._SURFACE = pygame.Surface
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # MODIFIER

    def changeDirX(self):
        if self.__DIR_X == 1:
            self.__DIR_X = -1
        else:
            self.__DIR_Y = 1

    def changeDirY(self):
        if self.__DIR_Y == 1:
            self.__DIR_Y = -1
        else:
            self.__DIR_Y = 1


    def setX(self, X):
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setPOS(self, X, Y):
        self.setX(X)
        self.setY(Y)

    def marqueeX(self, MAX_X, MIN_X=0):
        self.__X -= self._SPD

        """if self.__X > MAX_X:
            self.__X = MIN_X - self.getWidth()"""

        if self.__X < MIN_X - self.getWidth():
            self.__X = MAX_X + self.getWidth()
            #self.__X = OG_X

        self.__POS = (self.__X, self.__Y)

    def marqueeAngle(self, MAX_X):
        self.__X -= self._SPD
        self.__Y += self._SPD / 4


        if self.__X < 0 - self.getWidth():
            self.__X = MAX_X + self.getWidth()
            self.__Y = randrange(100, 400)

        self.__POS = (self.__X, self.__Y)

    def marqueeRtoL(self, HEIGHT, MAX_X, MIN_X=0):
        self.__X -= self._SPD

        if self.__X < MIN_X - self.getWidth():
            DELAY = randint(0, 3)
            print(DELAY)
            self.__X = MAX_X + DELAY * 200



        self.__POS = (self.__X, self.__Y)



    def setSPD(self, SPEED):
        self._SPD = SPEED

    def WASDmove(self, PRESSED_KEYS):
        if PRESSED_KEYS[pygame.K_d] == 1:
            self.__X += self._SPD
        if PRESSED_KEYS[pygame.K_a] == 1:
            self.__X -= self._SPD
        if PRESSED_KEYS[pygame.K_w] == 1:
            self.__Y -= self._SPD
        if PRESSED_KEYS[pygame.K_s] == 1:
            self.__Y += self._SPD
        self.__POS = (self.__X, self.__Y)

    def UPDOWNmove(self, PRESSED_KEYS):
        if PRESSED_KEYS[pygame.K_w] == 1:
            self.__Y -= self._SPD
        if PRESSED_KEYS[pygame.K_s] == 1:
            self.__Y += self._SPD
        self.__POS = (self.__X, self.__Y)



    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X
        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y
        self.__POS = (self.__X, self.__Y)

    def bounceX(self, MAX_X, MIN_X=0):
        self.__X += self.__DIR_X * self._SPD # change the direction
        if self.__X > MAX_X - self.getWidth():
            self.__DIR_X = -1
        if self.__X < MIN_X:
            self.__DIR_X = 1
        self.__POS = (self.__X, self.__Y)

    def bounceY(self, MAX_Y, MIN_Y=0):
        self.__Y += self.__DIR_Y * self._SPD # change the direction
        if self.__Y > MAX_Y - self.getHeight():
            self.__DIR_Y = -1
        if self.__Y < MIN_Y:
            self.__DIR_Y = 1
        self.__POS = (self.__X, self.__Y)

    # ACCESSOR METHODS
    def getPOS(self):
        return self.__POS

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getSurface(self):
        return self._SURFACE

    def isCollision(self, WIDTH, HEIGHT, POS):
        """
        use the Width, Height, and Position of an EXTERNAL sprite to test if its is colling with the given sprite (self).
        :param WIDTH: int
        :param HEIGHT: int
        :param POS: tuple
        :return:
        """

        if POS[0] >= self.__X - WIDTH and POS[0] <= self.__X + self.getWidth() and \
            POS[1] >= self.__Y - HEIGHT and POS[1] <= self.__Y + self.getHeight():
           return True
        else:
            return False

    def _getCenter(self):
        """
        find the center position of the Surface and return the coordinate
        :return: tuple[int]
        """
        X_CENTER = self.__X + self.getWidth()//2
        Y_CENTER = self.__Y + self.getHeight()//2
        return (X_CENTER, Y_CENTER)








