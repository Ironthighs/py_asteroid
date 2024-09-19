import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        firstRandomVelocity = self.velocity.rotate(random_angle)
        secondRandomVelocity = self.velocity.rotate(-random_angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        firstNewAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
        firstNewAsteroid.velocity = firstRandomVelocity * 1.2
        secondNewAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
        secondNewAsteroid.velocity = secondRandomVelocity * 1.2
