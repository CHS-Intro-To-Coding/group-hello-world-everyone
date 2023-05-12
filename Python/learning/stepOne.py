import pygame

pygame.init()

WIDE = 800
HIGH = 400
screenSize = (WIDE,HIGH)
WHITE = (255,255,255)

window = pygame.display.set_mode(screenSize)
pygame.display.set_caption('hello')
window.fill(WHITE)

running = True
while running:
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    # pygame.time.wait(5000)
    # running = False
            
    

pygame.quit()