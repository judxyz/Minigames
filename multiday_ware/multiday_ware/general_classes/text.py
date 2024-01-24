# text.py in multiday_ware
"""
title: Text Sprites
author: Jude Andersen, Judy Zhu
date-created: 2023-11-29
"""

from multiday_ware.general_classes.my_sprite import MySprite
import pygame


class Text(MySprite):
    def __init__(self, TEXT, F_FAMILY="Arial", F_SIZE=36, X=0, Y=0):
        MySprite.__init__(self, X=X, Y=Y)
        self.__TEXT = TEXT
        self.__FONT_FAMILY = F_FAMILY
        self.__FONT_SIZE = F_SIZE
        self.__FONT = pygame.font.Font(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR) # single underscore - inherited class can see

    def setText(self, TEXT):
        self.__TEXT = TEXT
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def changeAlpha(self, VALUE:int):
        self._SURFACE.set_alpha(VALUE)

if __name__ == "__main__":
    from window import Window
    pygame.init()
    WINDOW = Window("TEXT Example", 800, 600, 30)
    TEXT = Text("Hello World")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())
        WINDOW.updateFrame()