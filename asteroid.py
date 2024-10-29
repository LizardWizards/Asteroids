import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        difference = random.uniform(20, 50)
        left = pygame.math.Vector2.rotate(self.velocity, -difference)
        right = pygame.math.Vector2.rotate(self.velocity, difference)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = left * 1.2

        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid.velocity = right * 1.2
