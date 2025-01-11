import pygame # type: ignore
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    #split the asteroid into smaller chunks on being destroyed by a shot.
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return print("this was a small asteroid")
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            speed1 = random.randint(40, 100)
            speed2 = random.randint(40,100)
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = pygame.Vector2(0,1).rotate(random_angle) * speed1 * 1.2
            new_asteroid_2.velocity = pygame.Vector2(0,1).rotate(-random_angle) * speed2 * 1.2