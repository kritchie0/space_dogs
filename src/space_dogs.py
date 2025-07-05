import pygame
from loguru import logger

import globals
from player import Player

RESOLUTION_SCALER = 4
SCREEN_WIDTH = 320 * RESOLUTION_SCALER
SCREEN_HEIGHT = 180 * RESOLUTION_SCALER
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]

def space_dogs():
    print("bork bork...in space...")

    # Setup
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    sysClock: pygame.time.Clock = pygame.time.Clock()
    is_running: bool = True

    SpaceDog = Player()

    # Quit game if user presses 'X' button on screen.
    while is_running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        fps_limit: float = sysClock.tick(globals.MAX_FPS) / 1000 # Limit FPS
        screen.fill("white")

        SpaceDog.update(fps_limit)
        
if __name__ == "__main__":
    logger.debug("Starting Space Dogs..." )
    space_dogs()
    