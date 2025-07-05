import pygame
from pygame import image, transform
from pygame import Surface

import numpy as np
from loguru import logger

import globals
from config import PATH_TO_PLAYER
from runtime import load_image
from enums import Directions


BaseSpeed: int = 160

class Player:
    def __init__(self):
        self.path_to_player: str = PATH_TO_PLAYER
        
        self.sprites: np.ndarray = self.load_sprites()
        self.sprite: Surface = self.get_sprite(globals.FrameTypesEnum.Idle, 0)
        self.scaling_factor = 2
        
        self.position = pygame.Vector2(0, 0)
        self.FPSLimit: float = 60

        self.frame: int = 0
        self.direction = 0

        # self.image: pygame.Surface = self.images[Directions.Idle][self.frame]
        self.surface = pygame.display.get_surface()

    def update(self, fps_limit: float):
        self.FPSLimit = fps_limit
        self.frame = (self.frame + 1) % 4
        self.sprite = self.get_sprite(globals.FrameTypesEnum.Walking, self.frame)

        # Render updates.
        surface = pygame.display.get_surface()
        surface.fill((255, 255, 255))
        self.surface.blit(self.sprite, self.position)
        pygame.display.flip()

    def load_sprites(self):
        sprites: list = list()
        
        for index, frame_type in enumerate(globals.FRAME_TYPES):
            sprites.append([])
            for n in range(len(frame_type)):
                path_to_sprite: str = f'{self.path_to_player}/movement/{frame_type[n]}_{n+1}.png'
                logger.debug(path_to_sprite)

                try:
                    # TODO Fix sprites[index, n] so it allows [int, int] indexing. 
                    sprites[index, n] = image.load(path_to_sprite)
                finally:
                    logger.error(f"Path does not exist: {path_to_sprite}")

        return sprites
    
    # def update(self, fps_limit):
    #     self.FPSLimit = fps_limit
    #     self._get_position()
    #
    #     # Update sprite.
    #     self.frame = (self.frame + 1) % 4
    #     self.image = self.images[self.direction][self.frame]
    #     self.image = pygame.transform.scale_by(self.image, self.image_scale)
    #



    def _get_position(self):
        input_keyboard = pygame.key.get_pressed()

        # Up
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

    def get_sprite(self, sprite_type: int, frame: int) -> Surface:
        sprite: Surface = self.sprites[sprite_type, frame]
        return transform.scale_by(sprite, self.scaling_factor)
