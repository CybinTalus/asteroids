import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):  
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.asteroid_color = (255, 255, 255)
        self.asteroid_width = 2
        self.small_asteroid_velocity = 1.2
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                           color=self.asteroid_color,
                           center=self.position,
                           radius=self.radius,
                           width=self.asteroid_width
                           )
        # return super().draw(screen)
    
    def split_asteroid(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        small_asteroid1 = Asteroid(self.position.x,
                                   self.position.y,
                                   self.radius - ASTEROID_MIN_RADIUS)
        small_asteroid1.velocity = self.velocity.rotate(random_angle) * self.small_asteroid_velocity
        small_asteroid2 = Asteroid(self.position.x,
                                   self.position.y,
                                   self.radius - ASTEROID_MIN_RADIUS)
        small_asteroid2.velocity = self.velocity.rotate(-random_angle) * self.small_asteroid_velocity
    def update(self, dt):
        self.position += self.velocity * dt
        # return super().update(dt)