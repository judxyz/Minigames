# spotlight_sprite.py in spotlight minigame in multiday ware

#from multiday_ware.asteroid_minigame.player import AbstractPlayer, ImageSprite
from multiday_ware.general_classes.image_sprite import ImageSprite
import pygame

class Player(ImageSprite):
    def __init__(self, SPEED=7):
        ImageSprite.__init__(self, "./spotlight_media/spotlight.png")
        self.setScale(0.1)
        self.__X = 0
        self.__Y = 0
        self._SPD = SPEED
        self._OPACITY = self.changeAlpha(200)
if __name__ == "__main__":
    from multiday_ware.general_classes.window import Window
    WINDOW = Window("Testing Game", 800, 600, 30)
    PLAYER = Player()
    PLAYER.setScale(6.05)
    PLAYER.setX(WINDOW.getWidth() // 2 - PLAYER.getWidth() // 2)
    PLAYER.setY(WINDOW.getHeight() // 2 - PLAYER.getHeight() // 2)
    PLAYER.changeAlpha(50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        KEYS_PRESSED = pygame.key.get_pressed()
        PLAYER.SPOTLIGHTmove(KEYS_PRESSED)
        PLAYER.checkBoundaries(WINDOW.getWidth() + 625, WINDOW.getHeight() + 675, -650, -600)
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        WINDOW.updateFrame()