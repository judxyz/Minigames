# window.py in multiday_ware

"""
Title: Window Class for pygame
Author: Jude Andersen, Judy Zhu
Date-created: 2023-11-29
"""

import pygame
from multiday_ware.general_classes.color import Color

class Window():
    """
    Create the window that will load program
    """

    def __init__(self, TITLE, WIDTH, HEIGHT, FPS):
        # super().__init__()
        self.__TITLE = TITLE
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIMENSIONS)
        self.__SURFACE.fill(Color.GREY)
        pygame.display.set_caption(self.__TITLE) # window is named TITLE

    def clearScreen(self):
        self.__SURFACE.fill(Color.GREY)

    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT

    def getFPS(self):
        return self.__FPS
