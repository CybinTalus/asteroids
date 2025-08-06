import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):  
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.asteroid_color = (255, 255, 255)
        self.asteroid_width = 2
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                           color=self.asteroid_color,
                           center=self.position,
                           radius=self.radius,
                           width=self.asteroid_width
                           )
        # return super().draw(screen)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # return super().update(dt)