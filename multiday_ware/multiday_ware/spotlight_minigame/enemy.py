# enemy.py in multiday_ware (folder)
import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent))

import pygame

from multiday_ware.general_classes.image_sprite import ImageSprite



class Enemy(ImageSprite):

    def __init__(self, FILE_LOCATION, SPEED=4):
        ImageSprite.__init__(self, FILE_LOCATION)
        self.setScale(0.1)
        self.__X = 0
        self.__Y = 0
        self._SPD = SPEED
        self.rotateSprite(0)


    def running(self):
        """
        will set the running animation for the character
        :return: none
        """
        print("hello")





if __name__ == "__main__":
    from multiday_ware.general_classes.window import Window

    WINDOW = Window("Testing Game", 800, 600, 30)
    ENEMIES = []
    ENEMIES.append(Enemy("../spotlight_media/wario_running_1.png"))
    ENEMIES.append(Enemy("../spotlight_media/wario_running_2.png"))

    for i in range(len(ENEMIES)):
        ENEMIES[i].setScale(4)
        ENEMIES[i].setX(WINDOW.getWidth() // 2 - ENEMIES[i].getWidth() // 2)
        ENEMIES[i].setY(WINDOW.getHeight() // 2 - ENEMIES[i].getHeight() // 2)
    TIMER = 0
    FRAME = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        for i in range(len(ENEMIES)):
            ENEMIES[i].bounceX(WINDOW.getWidth())
            ENEMIES[i].bounceY(WINDOW.getHeight())

        if FRAME == 1:
            TIMER += 1
            if TIMER > 10:
                FRAME = 2
                TIMER = 0
        if FRAME == 2:
            TIMER += 1
            if TIMER > 10:
                FRAME = 1
                TIMER = 0


        WINDOW.clearScreen()

        if FRAME == 1:

            WINDOW.getSurface().blit(ENEMIES[0].getSurface(), ENEMIES[0].getPOS())
        else:
            WINDOW.getSurface().blit(ENEMIES[1].getSurface(), ENEMIES[1].getPOS())
        WINDOW.updateFrame()
