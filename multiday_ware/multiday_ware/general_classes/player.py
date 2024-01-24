# player.py in multiday_ware
"""
title: Abstract Player Class
author: Jude Andersen, Judy Zhu
date-created: 2023-11-29
"""

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
