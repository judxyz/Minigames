# player_sprite.py in asteroid_minigame

"""
Title: Player Sprite for Jumping Minigame
author: Jude Andersen, Judy Zhu
date-created: 2023-12-05
"""
from multiday_ware.general_classes.player import ImageSprite
import pygame

import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent))

CLOCK = pygame.time.Clock()

class Player(ImageSprite):
    def __init__(self, IMAGE_FILE_LOC="a_media/wario_prisoner_running_1.png"):
        ImageSprite.__init__(self, IMAGE_FILE_LOC, 0.2)
        self.__X = 100
        self.__Y = 430
        self.setPOS(self.__X, self.__Y)
        self.setImageDirX(False)
        self.isJump = False
        self.__JUMP_HEIGHT = 25
        self.__Y_VEL = self.__JUMP_HEIGHT
        self.__GROUNDPOS = 430
        self.__Y_GRAVITY = 1.25
        self.__FRAME = 1
        self.__LAST_UPDATED = 0




    def checkjump(self, PRESSED_KEYS):
        if PRESSED_KEYS[pygame.K_SPACE]:
            self.isJump = True


        if self.isJump:
            self.__Y -= self.__Y_VEL
            self.__Y_VEL -=self.__Y_GRAVITY
            if self.__Y_VEL < -self.__JUMP_HEIGHT:
                self.isJump = False
                self.__Y_VEL = self.__JUMP_HEIGHT
            self.setImage("a_media/wario_prisoner_jumping.png", 0.2)
            self.setPOS(self.__X, self.__Y)
        #ANIMATION
        if not self.isJump:
            self.animate()

    def animate(self):
        CLOCK.tick(60)
        NOW = pygame.time.get_ticks()
        if not self.isJump:
            if NOW - self.__LAST_UPDATED > 200: #greater than 200 ms
                if self.__FRAME == 1:
                    self.__LAST_UPDATED = NOW
                    #self.__init__("a_media/wario_prisoner_running_1.png")
                    self.setImage("a_media/wario_prisoner_running_1.png", 0.2)

                    self.__FRAME = 2
                elif self.__FRAME == 2:
                    self.__LAST_UPDATED = NOW
                    #self.__init__("a_media/wario_prisoner_running_2.png")

                    self.setImage("a_media/wario_prisoner_running_2.png", 0.2)
                    self.__FRAME = 1


if __name__ == "__main__":
    from multiday_ware.general_classes.window import Window

    WINDOW = Window("Testing Game", 800, 600, 30)
    PLAYER = Player("test-enemy.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        KEYS_PRESSED = pygame.key.get_pressed()
        #PLAYER.checkjump(KEYS_PRESSED)
        PLAYER.animate()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        WINDOW.updateFrame()
        CLOCK.tick(60)

