# box.py in multiday_ware
"""
title: Abstract Box class
author: Jude Andersen, Judy Zhu
date-created: 2023-11-29
"""

from multiday_ware.general_classes.my_sprite import MySprite
import pygame


class Box(MySprite):

    def __init__(self, WIDTH=1, HEIGHT=1):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIMENSIONS, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

    def setColor(self, COLOR):
        """
        update the color of the box
        :param COLOR: tuple
        :return:
        """
        self._COLOR = COLOR
        self._SURFACE.fill(COLOR)
    def changeAlpha(self, VALUE:int):
        self._SURFACE.set_alpha(VALUE)
