# player_sprite.py in asteroid_minigame

"""
Title: Player Sprite for Asteroid Minigame
author: Jude Andersen, Judy Zhu
date-created: 2023-11-29
"""
from multiday_ware.general_classes.player import AbstractPlayer, ImageSprite
import pygame

class Player(ImageSprite):
    def __init__(self):
        ImageSprite.__init__(self, "a_media/player_car.png", 0.12)
        self.__X = 0
        self.__Y = 0
        self.rotateSprite(-12)



    def moveUpDown(self, PRESSED_KEYS):
        AbstractPlayer.UPDOWNmove(self, PRESSED_KEYS)




if __name__ == "__main__":
    from multiday_ware.general_classes.window import Window

    WINDOW = Window("Testing Game", 800, 600, 30)
    PLAYER = Player()

    PLAYER.setX(WINDOW.getWidth() // 2 - PLAYER.getWidth() // 2)
    PLAYER.setY(WINDOW.getHeight() // 2 - PLAYER.getHeight() // 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        KEYS_PRESSED = pygame.key.get_pressed()
        PLAYER.moveUpDown(KEYS_PRESSED)
        PLAYER.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        WINDOW.updateFrame()

