import pygame
import platK
class Player (pygame.sprite.Sprite):
    ''' the class that holds the main player and controls
    how they jump. Also, the player doesn't move left or
    right, t
    he world moves around them'''

    def __init__(self, start_x, start_y, world) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(platK.player_image),(platK.player_width,platK.player_height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.speed_y = 0
        self.base = pygame.Rect (start_x, start_y + platK.player_height, platK.player_width, 2)
        self.myWorld = world
    
    def move_y(self):
        ''' this calculates the y-axis movement
        for the player in the current speed'''
        self.rect.y = self.rect.y + 1
        collided_y = self.myWorld.collided_get_y(self.base)
        if self.speed_y <= 0 or collided_y < 0:
            self.rect.y = self.rect.y + self.speed_y
            self.speed_y = self.speed_y + platK.gravity
        if collided_y > 0 and self.speed_y > 0:
            self.rect.y = collided_y
        self.base.y = self.rect.y + self.rect.height

    def jump(self,speed):
        ''' this set the player to jump,
        but it only can if its feet are on the floor'''
        if self.myWorld.collided_get_y(self.base) > 0:
            self.speed_y = speed

    # end Player class


