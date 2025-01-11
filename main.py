# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # player.update(dt)
        #  update all item in the group "updatable"
        for item in updatable:
            item.update(dt)

        for item in asteroids:
            if item.is_collision(player):
                print("Game Over!")
                sys.exit(0)
            for item2 in shots:
                if item.is_collision(item2):
                    item.split()
                    item2.kill()

        screen.fill("black")
        
    
        # player.draw(screen)
        #   draw all items in the pygame group "drawable"
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit framerate to 60fps
        dt = clock.tick(60) / 1000

        

if __name__ == "__main__":
    main()