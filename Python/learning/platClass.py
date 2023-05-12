from random import randint
import pygame
import platK







class Doom():
    ''' this class holds all the things that can kill the player'''
    def __init__(self, fireball_num, pit_depth, color) -> None:
        self.base = pygame.Rect(0,platK.screen_y-pit_depth, platK.screen_x, pit_depth)
        self.color = color
        self.fireballs = []
        for i in range(0,fireball_num):
            self.fireballs.append(Fireball())
        self.fireball_plain = pygame.sprite.RenderPlain(self.fireballs)
    
    def move(self,dist):
        for fireball in self.fireballs:
            fireball.move_x(dist)

    def collided(self, player_rect):
        for fireball in self.fireballs:
            if fireball.rect.colliderect(player_rect):
                hit_box = fireball.rect.inflate(-int(platK.fireball_size/2), -int(platK.fireball_size/2))
                if hit_box.colliderect(player_rect):
                    return True
        return self.base.colliderect(player_rect)
    
    def update(self, screen):
        ''' move fireballs down and draw all '''
        for fireball in self.fireballs:
            fireball.move_y()
        self.fireball_plain.draw(screen)
        pygame.draw.rect(screen, self.color, self.base, 0)
    
    # end doom class





class Fireball(pygame.sprite.Sprite):
    ''' this class holds the fireballs that
    fall from the sky '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(platK.fireball_image),
                                            (platK.fireball_size,platK.fireball_size))
        self.rect = self.image.get_rect()
        self.reset()
    def reset(self):
        self.y = 0
        self.speed_y = randint(platK.fireball_low_speed,platK.fireball_high_speed)
        self.x = randint(0,platK.screen_x)
        self.rect.topleft = self.x, self.y
    def move_x(self,dist):
        self.rect.move_ip(dist,0)
        if self.rect.x < -50 or self.rect.x > platK.screen_x:
            self.reset
    def move_y(self):
        self.rect.move_ip(0,self.speed_y)
        if self.rect.y > platK.screen_y:
            self.reset()
    
    # end fireball class