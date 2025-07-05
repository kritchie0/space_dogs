import pygame
from numpy.matlib import zeros
from pygame import image
from pygame import Surface
from dataclasses import dataclass
import numpy as np
from loguru import logger

import globals
from config import PATH_TO_PLAYER
from runtime import load_image
from enums import Directions


BaseSpeed: int = 160

class Player:
    def __init__(self, path_to_player: str):
        self.path_to_player: str = PATH_TO_PLAYER
        self.path_to_movement: str = self.path_to_player + "/movement"
        self.frames: np.ndarray = np.zeros((globals.MAX_ANIMATION_FRAMES, len(globals.FRAME_TYPES)))

        # self.movement_sprites = 1
        # self.images = load_image(PATHS_PLAYER)
        # self.position = pygame.Vector2(0, 0)
        # self.FPSLimit = None
        # self.image_scale = 2
        #
        # self.frame: int = 0
        # self.direction = 0
        # self.image: pygame.Surface = self.images[Directions.Idle][self.frame]
        # self.surface = pygame.display.get_surface()

    def load_sprites(self, sprite_type: str):
        # Movement Sprites
        for index, frame_type in enumerate(globals.FRAME_TYPES):
            for n in range(len(frame_type)):
                path_to_sprite: str = f'{self.path_to_player}/movement/{frame_type[n]}_{n+1}'
                logger.debug(path_to_sprite)

                try:
                    self.frames[index, n] = image.load(path_to_sprite)
                finally:
                    logger.error(f"Path does not exist: {path_to_sprite}")

    # def update(self, fps_limit):
    #     self.FPSLimit = fps_limit
    #     self._get_position()
    #
    #     # Update sprite.
    #     self.frame = (self.frame + 1) % 4
    #     self.image = self.images[self.direction][self.frame]
    #     self.image = pygame.transform.scale_by(self.image, self.image_scale)
    #
    #     # Render updates.
    #     # surface = pygame.display.get_surface()
    #     # surface.fill((255, 255, 255))
    #     self.surface.blit(self.image, self.position)
    #     pygame.display.flip()


    # def _get_position(self):
    #     input_keyboard = pygame.key.get_pressed()
    #
    #     if input_keyboard[pygame.K_w]:
    #         self.direction = Directions.Up
    #         self.position.y -= BaseSpeed * self.FPSLimit
    #
    #     elif input_keyboard[pygame.K_s]:
    #         self.direction = Directions.Down
    #         self.position.y += BaseSpeed * self.FPSLimit
    #
    #     elif input_keyboard[pygame.K_a]:
    #         self.direction = Directions.Left
    #         self.position.x -= BaseSpeed * self.FPSLimit
    #
    #     elif input_keyboard[pygame.K_d]:
    #         self.direction = Directions.Right
    #         self.position.x += BaseSpeed * self.FPSLimit
    #
    #     else:
    #         self.direction = Directions.Idle
    #         self.frame = 0

def test_player():
    player = Player(config.Path_To_Player)
    player.load_sprites('movement')