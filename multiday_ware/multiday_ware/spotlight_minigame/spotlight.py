# spotlight.py in spotlight_minigame(folder) in multiday_ware(folder)

"""
Title: Spotlight Class
Author: Judy & Jude
Date: 2023-12-05
"""
from multiday_ware.a_fonts import*
import pygame
from multiday_ware.general_classes.my_sprite import MySprite
from multiday_ware.general_classes.image_sprite import ImageSprite
from multiday_ware.general_classes.box import Box

class AbstractPlayer(ImageSprite):
    def __init__(self, IMAGE_FILE_LOC):
        ImageSprite.__init__(self, IMAGE_FILE_LOC)
        self.__PLAYER_SPRITE = Box(100, 50)
        self._SURFACE = self.__PLAYER_SPRITE.getSurface()
        self.__LIVES = 5


    # MODIFIER METHODS
    ### Inputs

    def setX(self, X):
        MySprite.setX(self, X)

    def setY(self, Y):
        MySprite.setY(self, Y)

    def setPOS(self, X, Y):
        MySprite.setPOS(self, X, Y)


    ### PROCESSING

    # ACCESSOR METHODS





