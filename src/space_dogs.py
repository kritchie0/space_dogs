import sys
import pygame
from dataclasses import dataclass
# from src.sprites import player
# from src.muddy_paws import MuddyPlayer
import globals
import assets
from player import Player


SCREEN_WIDTH = 430
SCREEN_HEIGHT = 430
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]


@dataclass()
class SDCfg:
    screen: pygame.Surface
    sysClock: pygame.Clock
    isRunning: bool


def space_dogs():
    print("bork bork...in space...")

    # Setup
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    sysClock: pygame.Clock = pygame.time.Clock()
    is_running: bool = True

    SpaceDog = Player()

    # Quit game if user presses 'X' button on screen.
    while is_running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        FPSLimit = sysClock.tick(globals.MAX_FPS) / 1000 # Limit FPS
        screen.fill("white")

        SpaceDog.update(FPSLimit)


if __name__ == "__main__":
    space_dogs()
