# enemy_sprite.py in asteroid_minigame

"""
title: Enemy Sprite class
author: Jude Andersen
date-created: 2023-11-29
"""
from multiday_ware.general_classes.image_sprite import ImageSprite
import pygame
import math

class Enemy(ImageSprite):
    def __init__(self, IMAGE_FILE_LOC="a_media/police_car.png"):

        ImageSprite.__init__(self, IMAGE_FILE_LOC, 0.1)
        self.__SPD = 5
        self.__X = ImageSprite.getX(self)
        self.__Y = ImageSprite.getY(self)
        self.rotateSprite(-12)
        self.__ANGLE = 0
        self.__X_RATIO = 0.0
        self.__Y_RATIO = 0.0
        self.OGY = 0
        self.setImageDirX(False)

    def setAngleRatios(self, X, Y):
        """
        updates the X and Y ratios for the position at (X, Y)
        :param X:
        :param Y:
        :return:
        """
        X_DELTA = abs(self.getX() - X)
        Y_DELTA = abs(self.getY() - Y)
        print(X_DELTA)
        print(Y_DELTA)
        self.__X_RATIO = math.cos(math.atan(Y_DELTA / X_DELTA))  # find angle first\, using inverse tan
        self.__Y_RATIO = math.sin(math.atan(X_DELTA / Y_DELTA))

    """def setAngle(self, ANGLE):
        
        updates the X and Y ratios for the position at (X, Y)
        :param X:
        :param Y:
        :return:
        

        self.__X_RATIO = math.cos(ANGLE)  # find angle first, using inverse tan
        self.__Y_RATIO = math.sin(ANGLE)


    def marqueeAngle(self, X, Y):
        if self.getX() < X - self.getWidth() // 2:
            self.setX(self.getX() - self._SPD * self.__X_RATIO)
        else:
            self.setX(self.getX() + self._SPD * self.__X_RATIO)

        if self.getY() < Y - self.getHeight() // 2:
            self.setY(self.getY() + self._SPD * self.__Y_RATIO)
        else:
            self.setY(self.getY() - self._SPD * self.__Y_RATIO)
"""



if __name__ == "__main__":
    from multiday_ware.general_classes.window import Window

    WINDOW = Window("Testing Enemy", 800, 600, 30)
    ENEMY = Enemy("test_sprite.png")


    ENEMY.setImageDirX(False)
    ENEMY.setX(WINDOW.getWidth()- ENEMY.getWidth())
    ENEMY.setY(200)
    ENEMY.setAngleRatios(WINDOW.getWidth()//2, WINDOW.getHeight()//2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #ENEMY.marqueeAngle(WINDOW.getWidth(), WINDOW.getHeight())

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(ENEMY.getSurface(), ENEMY.getPOS())
        WINDOW.updateFrame()


