import pygame

class Text ():

    def __init__(self,screen,textData,size,color,border,bk_color,posX,posY):
        # set font size
        myFont = pygame.font.SysFont("Console",size)
        # turn text into image
        self.myImage = myFont.render(textData,True,color)

        imgWide = self.myImage.get_width()
        imgHigh = self.myImage.get_height()
        
        # values for correct border placement
        gap = (size/10)
        bkPosX = posX - border - gap
        bkPosY = posY - border
        bkWide = imgWide + (2*border) + (2*gap)
        bkHigh = imgHigh + (2*border)

        # draw background rectangle
        self.myRect = pygame.rect.Rect(bkPosX,bkPosY,bkWide,bkHigh)
        pygame.draw.rect(screen,bk_color,self.myRect)
        # draw the text
        screen.blit(self.myImage, (posX,posY))
