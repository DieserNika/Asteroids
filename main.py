import shot
import asteroid
import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state, log_event
from player import *
from shot import *

def main():
    pygame.init()
    time = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = updatable
    
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = time.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.vernum}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
