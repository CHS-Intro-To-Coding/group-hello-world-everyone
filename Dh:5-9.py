import pygame 

pygame.init() 

Wide= 800 
High=400 
screenSize = (WIDE,HIGH)  
WHITE =(255,255,255)


dom= pygame.display.set_mode(screenSize) 
white = False
domisworking= True 
while domisworking: 
   for event in pygame.event.get(): 
       if event.type == Pygame.QUIT: 
          domisworking = False 
         if event.type == pygame.MOUSEBUTNOTDOM: 
           if white: 
              lance.fill(WHITE) 
           else: 
            
              
         
   pygame.time.wait(5000)  
   domisworking = False


pygame.quit()








