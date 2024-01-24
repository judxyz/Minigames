# image_sprite.py in multiday_ware
"""
title: abstract Image Sprite
author: Jude Andersen, Judy Zhu
date-created: 2023-11-29
"""
from multiday_ware.general_classes.my_sprite import MySprite
import pygame


class ImageSprite(MySprite):
    def __init__(self, IMAGE_FILE_LOC, SIZE=1): #overwritten here
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE_LOC
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.setScale(SIZE)
        self.__IMAGE_DIR_X = True  # looking right: true, left: false
        self.__X = self.getX()
        self.__Y = self.getY()

        self.__RECT = self._SURFACE.get_rect()
        self.MASK = pygame.mask.from_surface(self._SURFACE)
        self.MASK_IMG = self.MASK.to_surface()
        self.RECT_TOPLEFT = (self.__X, self.__Y)


    # MODIFIER METHODS

    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        changes the scale of the image, making it bigger or smaller
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: None
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth() * SCALE_X, self.getHeight() * SCALE_Y))
        #self.MASK_IMG = pygame.mask.Mask.scale((self._SURFACE.get_width(), self._SURFACE.get_height()))

    def setImageDirX(self, BOOL):
        """
        sets the image direction X variable. True is Right, False is Left
        :param BOOL: bool
        :return: None
        """
        self.__IMAGE_DIR_X = BOOL
        if BOOL == True:
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
        else:
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)

    def rotateSprite(self, DEGREES):
        self._SURFACE = pygame.transform.rotate(self._SURFACE, DEGREES)

    def changeAlpha(self, VALUE:int):
        self._SURFACE.set_alpha(VALUE)

    def WASDmove(self, PRESSED_KEYS):
        MySprite.WASDmove(self, PRESSED_KEYS) # Call MySprite Parent class
        if PRESSED_KEYS[pygame.K_d] == 1 and not self.__IMAGE_DIR_X:
            # If d key is pressed and image in looking right
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__IMAGE_DIR_X = True
        if PRESSED_KEYS[pygame.K_a] == 1 and self.__IMAGE_DIR_X:
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__IMAGE_DIR_X = False

    """def marqueeX(self, MAX_X, MIN_X=0):
        MySprite.marqueeX(self, MAX_X, MIN_X=0)"""

    def SPOTLIGHTmove(self, PRESSED_KEYS):
        MySprite.WASDmove(self, PRESSED_KEYS) # as to not flip when moving


    def loopBG(self, MAX_X, MIN_X=0):

        self.__X -= self._SPD

        if self.__X < MIN_X - self.getWidth():
            self.__X = MAX_X

        self.__POS = (self.__X, self.__Y)

    def setImage(self, IMAGE_FILE_LOC, SCALE):
        self.__FILE_LOC = IMAGE_FILE_LOC
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.setScale(SCALE)

    def maskOverlap(self, OTHER_MASK, POS): #checking overlaps using masks
        if self.MASK.overlap(OTHER_MASK, (POS[0]- self.getX(), POS[1]-self.getY())): #POS is of the other sprite
            return True
        else:
            return False

if __name__ == "__main__":
    from multiday_ware.general_classes.window import Window

    WINDOW = Window("Image Sprites", 800, 600, 30)
    BG = ImageSprite("test_sprite.png", 200)
    BG.setX(10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        KEYS_PRESSED = pygame.key.get_pressed()


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BG.getSurface(), BG.getPOS())
        WINDOW.updateFrame()
