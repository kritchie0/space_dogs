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


PLAYER_POS_INIT = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
PLAYER_SPEED = 200


class GameState:
    def __init__(self, position_):
        self.Direction = None
        self.Position = position_



def show(image, pos: pygame.Vector2,):
    screen = pygame.display.get_surface()
    screen.fill((255, 255, 255))
    screen.blit(image, (pos.x, pos.y))
    pygame.display.flip()


def Initialize_SpaceDogs():
    ...


def space_dogs():
    print("bork bork...in space...")

    # Setup
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    sysClock: pygame.Clock = pygame.time.Clock()
    is_running: bool = True
    dt: float = 0

    DogPosition = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
    SpaceDog = Player()

    # PlayerImages = player.PlayerImages()
    # Player = player.PlayerEntity(PlayerImages, PLAYER_POS_INIT)
    DogPosition.x = 0
    DogPosition.y = 0

    # image: pygame.Surface = pygame.image.load(PLAYER_DOWN_SPRITE).convert()
    # image2: pygame.Surface = pygame.image.load(PLAYER_UP_SPRITE).convert()


    # Quit game if user presses 'X' button on screen.
    while is_running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        FPSLimit = sysClock.tick(globals.MAX_FPS) / 1000 # Limit FPS

        screen.fill("white")

        SpaceDog.Update(FPSLimit)

        # Player Render
        # surface = pygame.display.get_surface()
        # surface.fill((255, 255, 255))
        # surface.blit(SpaceDog.sprite, (SpaceDog.position_x, SpaceDog.position_y))
        # pygame.display.flip()


if __name__ == "__main__":
    space_dogs()
