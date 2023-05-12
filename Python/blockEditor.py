import pygame
import random
import time
import png

def makePNG(imageName):
    width = 255
    height = 255
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            row = row + (x, max(0, 255 - x - y), y)
        img.append(row)
    with open(imageName, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

x = input("Do you want to edit an image? If yes, enter Y")

if  x == "Y":
    image_url = input("please enter image name, such as image.png")

else:
    x = input("Do you want to create a new image? Enter Y")
    if x == "Y":
        image_url = input("What would you like to name it, such as image.png")
        print (image_url)
        makePNG(image_url)
    else:
        x = input("okay quitting now, press the enter key")

image = pygame.image.load(image_url) 
i_edit = True




pygame.init()


red = (255,0,0)
orange = (255,165,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,215)
indigo = (75,0,130)
violet = (128,0,128)
black = (0, 0, 0)
white = (255,255,255)
BLACK = (1,1,1)

gameDisplay = pygame.display.set_mode((255, 255))
clock = pygame.time.Clock()

color = white

crashed = False
buttpressed = 0
rightkeypressed = False
radius = 10

image.set_colorkey(BLACK)
background_colour = (0,0,0)
gameDisplay.fill(BLACK)

if i_edit:
    gameDisplay.blit(image, (0, 0))

while not crashed:

    if radius < 5:
        radius = 5
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(gameDisplay,image_url)
            crashed = True


        pygame.display.set_caption("Your Pen Size is {0}".format(radius))

        if event.type == pygame.KEYDOWN and rightkeypressed is True:
            if event.unicode == 'n':
                background_colour = black
            if event.unicode == 'w':
                background_colour = white
            if event.unicode == 'r':
                background_colour = red
            if event.unicode == 'o':
                background_colour = orange
            if event.unicode == 'y':
                background_colour = yellow
            if event.unicode == 'g':
                background_colour = green
            if event.unicode == 'b':
                background_colour = blue
            if event.unicode == 'i':
                background_colour = indigo
            if event.unicode == 'p':
                background_colour = violet
            if event.unicode == 'e':
                color = background_colour
            gameDisplay.fill(background_colour)
            if event.unicode == 'q':
                gameDisplay.blit(image, (0, 0))


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                rightkeypressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                rightkeypressed = False
        
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'n':
                color = black
            if event.unicode == 'w':
                color = white
            if event.unicode == 'r':
                color = red
            if event.unicode == 'o':
                color = orange
            if event.unicode == 'y':
                color = yellow
            if event.unicode == 'g':
                color = green
            if event.unicode == 'b':
                color = blue
            if event.unicode == 'i':
                color = indigo
            if event.unicode == 'p':
                color = violet
            if event.unicode == 'e':
                color = background_colour
            if event.unicode == '=':
                radius += 5
            if event.unicode == '-':
                radius -= 5

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttpressed += 1


        if event.type == pygame.MOUSEMOTION and (buttpressed%2) != 0:
            pygame.draw.circle(gameDisplay, color, pygame.mouse.get_pos(), radius)

    pygame.display.update()
    clock.tick(60)