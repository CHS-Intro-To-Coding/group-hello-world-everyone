# a test python project
# uses pygame

'''
developed for teaching the fundamentals
of a platformer game, of windows,
and of events
Dr. Nielsen 05/09/2023

name=display, caption, fill, while, quit check, quit 
'''

import pygame
import textClass

pygame.init()

WIDE = 800
HIGH = 400
screenSize = (WIDE, HIGH)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GRAY = (100,100,100)

lance = pygame.display.set_mode(screenSize)
white = False
domisworking = True
showBanner = True
while domisworking:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            domisworking = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if white:
                lance.fill(WHITE)  
            else:
                lance.fill(RED)
            white = not white
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_j) :
                if showBanner:
                    myText = textClass.Text(lance,"You failed math",50,RED,30,GRAY,200,200)
                    showBanner = not showBanner
                else:
                    showBanner = not showBanner


    # example: self,screen,textData,size,color,border,bk_color,posX,posY
    pygame.display.update()
    

# print ('between the init and the quit')

pygame.quit()

