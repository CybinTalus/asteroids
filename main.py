import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Variables
background_color = (0, 0, 0)

def main():
    # Initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Pygame Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2) # Start player in center
    asteroid_field = AsteroidField() # Create asteroid field
    
    dt = 0
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, background_color)
        
        for item in updatable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen)
            
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                exit()
            for shot in shots:
                if asteroid.collision(shot):        
                    pygame.sprite.Sprite.kill(asteroid)
                
        # for shot in shots:
        #     if asteroid.collision(shot):
        #         pygame.sprite.Sprite.kill(asteroid)

        pygame.display.flip() # (re)renders the screen
        
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
