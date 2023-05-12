import pygame

class World():
    '''this will hold the platforms and the goal
    world moves left while player is still
    '''
    def __init__(self, level, block_size, color_platform, color_goals):
        self.platforms = []
        self.goals = []
        self.posn_y = 0
        self.color = color_platform
        self.color_goals = color_goals
        self.block_size = block_size

        for line in level:
            self.posn_x = 0
            for block in line:
                if block == "1":
                    self.platforms.append(pygame.Rect(self.posn_x, self.posn_y, block_size, block_size))
                if block == "G":
                    self.goals.append(pygame.Rect(self.posn_x, self.posn_y,block_size,block_size))
                self.posn_x = self.posn_x + block_size
            self.posn_y = self.posn_y + block_size
        # end init
    
    def update (self, screen):
        for block in self.platforms:
            pygame.draw.rect(screen, self.color, block, 0)
        for block in self.goals:
            pygame.draw.rect(screen,self.color_goals, block, 0)
        # end update

    def collided_get_y(self, player_rect):
        ''' get y value for platform player is on '''
        return_y = -1
        for block in self.platforms:
            if block.colliderect(player_rect):
                return_y = block.y - block.height + 1
        return return_y
        # end collided
    
    def move(self, dist):
        for block in self.platforms + self.goals:
            block.move_ip(dist, 0)
        # end move
    
    def at_goal(self, player_rect):
        for block in self.goals:
            if block.colliderect(player_rect):
                return True
        return False
        # end at goal

    # end World class




