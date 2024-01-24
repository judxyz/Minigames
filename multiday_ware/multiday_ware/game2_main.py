# game2_main.py in jumping_minigame
"""
title: Minigame #2 Game Engine
author: Jude Andersen, Judy Zhu
date-created: 2023-12-05
"""
import pygame.font
import pygame
from general_classes.box import Box
from multiday_ware.general_classes.color import Color
from multiday_ware.jumping_minigame.enemy_sprite import Enemy
from multiday_ware.general_classes.image_sprite import ImageSprite
from multiday_ware.general_classes.text import Text
from multiday_ware.general_classes.window import Window
from multiday_ware.jumping_minigame.player_sprite import Player
from multiday_ware.general_classes.box import Box



from random import randrange
pygame.init()

TESTFONT = "a_fonts/Retro Gaming.ttf"


class MiniGame2:
    def __init__(self):
        self.__WINDOW = Window("JUMPING MINIGAME", 800, 600, 30)
        self.__BG = ImageSprite("a_media/jumping_game_background.png")
        self.__BG.setScale(0.6)
        self.__BG.setPOS(0, self.__WINDOW.getHeight() // 10)
        self.__BG2 = ImageSprite("a_media/jumping_game_background.png")
        self.__BG2.setPOS(self.__BG.getX() + self.__BG.getWidth(), self.__WINDOW.getHeight() // 10)
        self.__BG2.setScale(0.6)
        self.__TIME_GAME = Box(800, 30)
        self.__WIN = 5  # random variable changed to 0 for loss and 1 for win

        self.__PLAYER = Player("a_media/wario_prisoner_running_1.png")
        self.__PLAYER.setImageDirX(True)
        self.__PLAYER.setX(-100)

        self.__TITLE_BAR = Box(self.__WINDOW.getWidth(), self.__WINDOW.getHeight() // 10)
        self.__TITLE_BAR.setColor(Color.BLACK)
        self.__TITLE_TEXT = Text("JUMPING MINIGAME", TESTFONT, 25)
        self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2,
                                 12)
        self.__LIVES = [ImageSprite("a_media/heart.png", 0.4), ImageSprite("a_media/heart.png", 0.4), ImageSprite("a_media/heart.png", 0.4)]

        self.__START_TEXT = Text("jump!", TESTFONT, 30)
        self.__START_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__START_TEXT.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__START_TEXT.getHeight()//2)
        self.__START_TEXT.changeAlpha(0)

        self.__GAME_OVER = False
        self.__GAME_OVER_TEXT = Text("Game Over", TESTFONT)
        self.__GAME_OVER_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__GAME_OVER_TEXT.getWidth() // 2,
                                     self.__WINDOW.getHeight() // 2 - self.__GAME_OVER_TEXT.getHeight() // 2)

        self.__ENEMIES = []
        for i in range(2):
            self.__ENEMIES.append(Enemy("a_media/jumping_game_police.png"))

            if i == 0:
                self.__ENEMIES[-1].setY(400)
            if i == 1:
                self.__ENEMIES[-1].setY(600)

            self.__ENEMIES[-1].setX(self.__WINDOW.getWidth()+self.__ENEMIES[-1].getWidth())


        for live in self.__LIVES:
            live.setPOS(-100, -100)
        self.__FRAME_WIPE = Box(1000, 1600)

        self.__FADE_BOX = Box(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
        self.__FADE_BOX.setColor(Color.BLACK)


    def frameWipe(self):
        self.__FRAME_WIPE.setPOS(0, self.__WINDOW.getHeight() - self.__FRAME_WIPE.getHeight())
        var = 0
        for i in range(10):
            self.__updateWindowFrame()
        for i in range(60):
            var += 10
            self.__FRAME_WIPE.setPOS(0, self.__WINDOW.getHeight() - self.__FRAME_WIPE.getHeight() - var)
            self.__updateWindowFrame()

    def fadeIn(self):
        self.__FADE_BOX.changeAlpha(255)

        for i in range(60):
            self.__FADE_BOX.changeAlpha(255- i*10)
            self.__updateWindowFrame()


    def introFrames(self):
        self.__WINDOW.clearScreen()


        for i in range(60):
            self.__START_TEXT.changeAlpha(0+i*10)
            self.__updateWindowFrame()
        self.__START_TEXT.changeAlpha(0)

        for i in range(60):
            self.__PLAYER.setX(self.__PLAYER.getPOS()[0] + 3)
            self.__updateWindowFrame()

    def run(self, LIVES, SCORE, MULTIPLIER):
        self.__SCORE_TEXT = Text(f"SCORE: {SCORE}", TESTFONT, 20)
        self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 20, 20)

        self.fadeIn()


        #LIVES
        if LIVES == 1:
            self.__LIVES[0].setPOS(20, 10)
        if LIVES == 2:
            self.__LIVES[0].setPOS(20, 10)
            self.__LIVES[1].setPOS(55, 10)
        if LIVES == 3:
            self.__LIVES[0].setPOS(20, 10)
            self.__LIVES[1].setPOS(55, 10)
            self.__LIVES[2].setPOS(90, 10)


        self.introFrames()

        for enemy in self.__ENEMIES:
            SPD = randrange(13, 20) + 3 * MULTIPLIER
            enemy.setSPD(SPD)
            print(f"{SPD}")


        while True:
            # -- INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.__BG.marqueeRtoL(self.__WINDOW.getHeight(), self.__WINDOW.getWidth())
            self.__BG2.marqueeRtoL(self.__WINDOW.getHeight(), self.__WINDOW.getWidth())


            KEYS_PRESSED = pygame.key.get_pressed()
            if not self.__GAME_OVER:
                self.__PLAYER.checkjump(KEYS_PRESSED)

            TIME_SIZE = self.__TIME_GAME.getWidth() - 4 + MULTIPLIER

            if TIME_SIZE > 0:
                self.__TIME_GAME = Box(TIME_SIZE, 30)
                self.__TIME_GAME.setPOS(0, 50)
            if self.__TIME_GAME.getWidth() < 20:
                self.__WIN = 1
                #print("win")




            # -- PROCESSING
            for enemy in self.__ENEMIES:
                enemy.marqueeRtoL(self.__WINDOW.getHeight()-enemy.getHeight()//2, self.__WINDOW.getWidth()+enemy.getWidth(), 0, True)


            if self.__WIN == 1:
                return True
            elif self.__WIN == 0:
                return False

            self.__updateWindowFrame()
    def __playerEnemyCollision(self):
        for i in range(len(self.__ENEMIES)):
            """if self.__ENEMIES[i].isCollision(self.__PLAYER.getSurface().get_width(),
                                               self.__PLAYER.getSurface().get_height(),
                                               self.__PLAYER.getPOS()):"""
            if self.__ENEMIES[i].maskOverlap(self.__PLAYER.MASK, self.__PLAYER.getPOS()):
                self.__ENEMIES[i].setSPD(0)
                self.__ENEMIES[i].setPOS(self.__WINDOW.getWidth()+self.__ENEMIES[i].getWidth(), self.__ENEMIES[i].getY())

                self.__WIN = 0

                # GAME OVER
                self.__GAME_OVER = True

    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()
        self.__WINDOW.getSurface().blit(self.__BG.getSurface(), self.__BG.getPOS())
        self.__WINDOW.getSurface().blit(self.__BG2.getSurface(), self.__BG2.getPOS())
        # -- LAYOUTING
        self.__WINDOW.getSurface().blit(self.__START_TEXT.getSurface(), self.__START_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__TIME_GAME.getSurface(), self.__TIME_GAME.getPOS())
        self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
        self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())

        for live in self.__LIVES:
            self.__WINDOW.getSurface().blit(live.getSurface(), live.getPOS())

        if not self.__GAME_OVER:
            # --- SPRITES

            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            #self.__WINDOW.getSurface().blit(self.__PLAYER.MASK_IMG, self.__PLAYER.getPOS())


            # --- ENEMY SPRITES
            for enemy in self.__ENEMIES:
                self.__WINDOW.getSurface().blit(enemy.getSurface(), enemy.getPOS())
                #self.__WINDOW.getSurface().blit(enemy.MASK_IMG, enemy.getPOS())

            # --- COLLISIONS
            self.__playerEnemyCollision()
        if self.__GAME_OVER:
            #self.__WINDOW.getSurface().blit(self.__GAME_OVER_TEXT.getSurface(),self.__GAME_OVER_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            for enemy in self.__ENEMIES:
                self.__WINDOW.getSurface().blit(enemy.getSurface(), enemy.getPOS())

        ### FADE BOX
        self.__WINDOW.getSurface().blit(self.__FADE_BOX.getSurface(), self.__FADE_BOX.getPOS())

        self.__WINDOW.updateFrame()




if __name__ == "__main__":
    GAME = MiniGame2()
    GAME.run(3, 2, 0)



