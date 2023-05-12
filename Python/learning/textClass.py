import pygame

class Text ():

    def __init__(self,screen,textData,size,color,border,bk_color,posX,posY):
        # set font size
        myFont = pygame.font.SysFont("Console",size)
        # turn text into image
        myImage = myFont.render(textData,True,color)

        imgWide = myImage.get_width()
        imgHigh = myImage.get_height()
        
        # values for correct border placement
        gap = (size/10)
        bkPosX = posX - border - gap
        bkPosY = posY - border
        bkWide = imgWide + (2*border) + (2*gap)
        bkHigh = imgHigh + (2*border)

        # draw background rectangle
        myRect = pygame.rect.Rect(bkPosX,bkPosY,bkWide,bkHigh)
        pygame.draw.rect(screen,bk_color,myRect)
        # draw the text
        screen.blit(myImage, (posX,posY))
