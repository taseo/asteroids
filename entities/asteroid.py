import pygame
import random

from shapes.circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        rotation_a = self.velocity.rotate(angle)
        rotation_b = self.velocity.rotate(-angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, radius)

        asteroid_a.velocity = rotation_a * 1.2

        asteroid_b = Asteroid(self.position.x, self.position.y, radius)

        asteroid_b.velocity = rotation_b * 1.2

