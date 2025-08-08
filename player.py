import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.player_color = (255, 255, 255)
        self.player_width = 2
        self.shot_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen,
                            color=self.player_color,
                            points=self.triangle(),
                            width=self.player_width
                            )
        # return super().draw(screen)
    
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED # turn player
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # get player forward position
        self.position += forward * PLAYER_SPEED * dt # adjust player forward position
    
    def shoot(self):
        if self.shot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) # Set up shot
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) *  PLAYER_SHOOT_SPEED # Set up velocity
        shot.velocity = shot_velocity # Apply velocity to shot
        self.shot_cooldown = PLAYER_SHOT_COOLDOWN
        
    def update(self, dt):
        self.shot_cooldown -= dt # reduce shot_cooldown by dt
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # turn player left
            dt = abs(dt) * -1
            self.rotate(dt)
        if keys[pygame.K_d]: # turn player right
            dt = abs(dt)
            self.rotate(dt)
        if keys[pygame.K_w]: # move player forward
            dt = abs(dt)
            self.move(dt)
        if keys[pygame.K_s]: # move player backward
            dt = abs(dt) * -1
            self.move(dt)
        if keys[pygame.K_SPACE]: # make player shoot
            self.shoot()