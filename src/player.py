import pygame
from pygame import Surface
from dataclasses import dataclass

import globals
import config
from runtime import load_image
from enums import Directions


BaseSpeed: int = 160

class Player:
    def __init__(self, path_to_player: str):
        self.path_to_player: str = path_to_player
        self.path_to_movement: str = self.path_to_player + "/movement"
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
        if sprite_type == 'movement':
            Movements = ['idle', 'walk', 'run']
            Directions = ['up', 'down', 'left', 'right']

            for movement in Movements:
                frame_index: int = 0
                path_to_sprite: str = f"{self.path_to_player}/{movement}"

                if movement == 'idle':
                    for i in range(2):
                        print(f"file={movement}/{movement}_frame_{frame_index + 1}")


                for direction in Directions:
                    if (movement == 'idle'):

                        print(f"file={movement}/{movement}_frame_{frame_index + 1}")
                    else:
                        print(f"file={movement}/{direction}_frame_{frame_index + 1}")
                    frame_index += 1
                # sprites: list = list()
                # path_to_sprites = []

        elif sprite_type == 'combat':
            ...
        else:
            return

    # images = []
    #
    # for i in range(len(file_)):
    #     images.append([])
    #
    #     for n in range(len(file_[0])):
    #         image = image.load(file_[i][n]).convert_alpha()
    #         images[i].append(image)
    #
    # return images

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