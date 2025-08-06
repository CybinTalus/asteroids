import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shot_color = (255, 255, 255)
        self.shot_width = 2
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                    color=self.shot_color,
                    center=self.position,
                    radius=SHOT_RADIUS,
                    width=self.shot_width
                    )
        # return super().draw(screen)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # return super().update(dt)