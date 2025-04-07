import pygame
from pygame import Surface
from dataclasses import dataclass

import globals
import runtime
from assets import PATHS_PLAYER
from enums import Directions


BaseSpeed: int = 160


class Player(runtime.Sprite):
    def __init__(self):
        runtime.Sprite.__init__(self, PATHS_PLAYER)
        self.position = pygame.Vector2(0, 0)
        self.FPSLimit = None

    def update(self, fps_limit):
        self.FPSLimit = fps_limit

        self._update_sprite()
        self._get_position()
        self._render(self.position)


    def _get_position(self):
        input_keyboard = pygame.key.get_pressed()

        if input_keyboard[pygame.K_w]:
            self.direction = Directions.Up
            self.position.y -= BaseSpeed * self.FPSLimit

        elif input_keyboard[pygame.K_s]:
            self.direction = Directions.Down
            self.position.y += BaseSpeed * self.FPSLimit

        elif input_keyboard[pygame.K_a]:
            self.direction = Directions.Left
            self.position.x -= BaseSpeed * self.FPSLimit

        elif input_keyboard[pygame.K_d]:
            self.direction = Directions.Right
            self.position.x += BaseSpeed * self.FPSLimit

        else: self.direction = Directions.Idle
