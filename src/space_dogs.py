import sys
import pygame
from dataclasses import dataclass
# from src.sprites import player
# from src.muddy_paws import MuddyPlayer
import globals
import assets
from utilities import place_dog
from player import Player

class SpaceDogs:
    def __init__(self):
        self.path_to_player_sprites: str = ''

RESOLUTION_SCALER = 4
SCREEN_WIDTH = 320 * RESOLUTION_SCALER
SCREEN_HEIGHT = 180 * RESOLUTION_SCALER
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]


@dataclass()
class SDCfg:
    screen: pygame.Surface
    sysClock: pygame.Clock
    isRunning: bool

def load_spaceDogs():
    # Setup
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    sysClock: pygame.Clock = pygame.time.Clock()
    is_running: bool = True
    player = Player()

    screen.fill("white")

    # Quit game if user presses 'X' button on screen.
    while is_running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        FPSLimit = sysClock.tick(globals.MAX_FPS) / 1000  # Limit FPS

        player.update(FPSLimit)
        place_dog([0,0])

def sd_runtime():
    place_dog([250, 250])


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