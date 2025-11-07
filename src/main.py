import sys
import pygame

from animation_manager import AnimationManager

FPS = 60


pygame.init()
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 480))



clock = pygame.time.Clock()
animation_manager = AnimationManager(screen)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    animation_manager.update()

    frame_time = clock.get_time() / (1 / FPS * 1000)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
