# enemy_sprite.py in jumping_minigame

"""
title: Enemy Sprite class
author: Jude Andersen, Judy Zhu
date-created: 2023-12-05
"""
from multiday_ware.general_classes.player import ImageSprite
import pygame

class Enemy(ImageSprite):
    def __init__(self, IMAGE_FILE_LOC="a_media/jumping_game_police.png"):
        ImageSprite.__init__(self, IMAGE_FILE_LOC, 0.225)
        self.__SPD = 5
        self.__X = ImageSprite.getX(self)
        self.__Y = ImageSprite.getY(self)

    def marqueeRtoL(self, HEIGHT, MAX_X, MIN_X=0, DELAY=0):
        ImageSprite.marqueeRtoL(self, HEIGHT, MAX_X)



if __name__ == "__main__":
    from multiday_ware.general_classes.window import Window

    WINDOW = Window("Testing Enemy", 800, 600, 30)
    ENEMY = Enemy("test-enemy.png")


    ENEMY.setImageDirX(False)
    ENEMY.setX(WINDOW.getWidth() // 2 - ENEMY.getWidth() // 2)
    ENEMY.setY(WINDOW.getHeight() // 2 - ENEMY.getHeight() // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        ENEMY.marqueeRtoL(WINDOW.getHeight()-ENEMY.getHeight()//2, WINDOW.getWidth()+ENEMY.getWidth())

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(ENEMY.getSurface(), ENEMY.getPOS())
        WINDOW.updateFrame()


