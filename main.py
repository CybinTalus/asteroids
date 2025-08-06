import pygame
from constants import *

# Variables
background_color = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, background_color)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
