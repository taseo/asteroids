import pygame

from constants import *
from entities.player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000000)

        for updatable in updatables:
            updatable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

