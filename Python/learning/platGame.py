# build a game
from random import randint
import pygame
import platK
import platLevels
import platClass
import platPlayerClass
import platWorldClass




# initialize variables
clock = pygame.time.Clock()
world = platWorldClass.World(platLevels.level, 30, platK.block_color, platK.goal_color)
doom = platClass.Doom(platK.fireball_number,10,platK.doom_color)
player = platPlayerClass.Player(platK.player_spawn_x,platK.player_spawn_y,world)
player_plain = pygame.sprite.RenderPlain(player) # type: ignore

# initialize pygame
pygame.init()
window = pygame.display.set_mode((platK.screen_x,platK.screen_y))
pygame.display.set_caption(platK.game_name)
screen = pygame.display.get_surface()

# initialize pygame.mixer

def waitForQuit():
    # waint until user quits
    running = True
    while running:
        # blank screen
        screen.fill((255,255,255))
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # held keys
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            world.move(2)
            doom.move(2)
        if key_state[pygame.K_RIGHT]:
            world.move(-2)
            doom.move(-2)
        if key_state[pygame.K_SPACE] and key_state[pygame.K_RIGHT]:
            player.jump(platK.jump_speed)
            world.move(-2)
            doom.move(-2)
        elif key_state[pygame.K_SPACE] and key_state[pygame.K_LEFT]:
            player.jump(platK.jump_speed)
            world.move(2)
            doom.move(2)
        elif key_state[pygame.K_SPACE]:
            player.jump(platK.jump_speed)        
        if key_state[pygame.K_ESCAPE]:
            pygame.quit()
        # move gravity
        player.move_y()
        # render
        player_plain.draw(screen)
        doom.update(screen)
        world.update(screen)
        # update
        pygame.display.update()
        # alive/dead
        if doom.collided(player.rect):
            print("you lose")
            running = False
        # level complete
        if world.at_goal(player.rect):
            print("winner")
            running = False
        # set speed
        clock.tick(20)

    pygame.time.wait(3000)
    pygame.quit()


waitForQuit()


