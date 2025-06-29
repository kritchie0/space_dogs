import pygame
from pygame import Surface
from dataclasses import dataclass

import globals
from runtime import load_image
from assets import PATHS_PLAYER
from enums import Directions


BaseSpeed: int = 160


class Player:
    def __init__(self):
        self.images = load_image(PATHS_PLAYER)
        self.position = pygame.Vector2(0, 0)
        self.FPSLimit = None
        self.image_scale = 2

        self.frame: int = 0
        self.direction = 0
        self.image: pygame.Surface = self.images[Directions.Idle][self.frame]
        self.surface = pygame.display.get_surface()

    def update(self, fps_limit):
        self.FPSLimit = fps_limit
        self._get_position()

        # Update sprite.
        self.frame = (self.frame + 1) % 4
        self.image = self.images[self.direction][self.frame]
        self.image = pygame.transform.scale_by(self.image, self.image_scale)

        # Render updates.
        # surface = pygame.display.get_surface()
        # surface.fill((255, 255, 255))
        self.surface.blit(self.image, self.position)
        pygame.display.flip()


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

        else:
            self.direction = Directions.Idle
            self.frame = 0

