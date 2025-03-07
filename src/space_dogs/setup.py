import pygame

from src.sprites.player import Player


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.SCREEN_WIDTH: int = 1000
        self.SCREEN_HEIGHT: int = 500
    ...