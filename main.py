# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()

    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # two groups to keep track of things
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add things to groups
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    while True:
        screen.fill((0,0,0))
        
        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()

        # quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #delays game to the point that it's 60 fps
        dt = clock.tick(60) / 1000 # convert ms to seconds


if __name__ == "__main__":
    main()