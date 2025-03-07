import pygame
from typing import Optional
from enum import StrEnum

class PlayerSprite(StrEnum):
    up: str = "./Assets/Player_Up_.png"
    down: str = "./Assets/Player_Down_.png"
    left: str = "./Assets/Player_Left_.png"
    right: str = "./Assets/Player_Right_.png"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Initialize base class.

        # Sprites
        self.player_sprite = None

    def load_sprites(self):
        self.player_sprite = pygame.image.load("../Assets/Dog000.png").convert_alpha()
