import pygame
from dataclasses import dataclass

from globals import MAX_FPS

class Sprite:
    def __init__(self, paths_):
        self.images = load_image(paths_)
        self.frame: int = 0
        self.direction = 0
        self.image: pygame.Surface


    def _update_sprite(self):
        self.frame = (self.frame + 1) % 4
        self.image = self.images[self.direction][self.frame]


    def _render(self, position_):
        surface = pygame.display.get_surface()
        surface.fill((255, 255, 255))
        surface.blit(self.image, position_)
        pygame.display.flip()

def load_image(file_: [str]):
    images = []

    for i in range(len(file_)):
        images.append([])

        for n in range(len(file_[0])):
            image = pygame.image.load(file_[i][n]).convert_alpha()
            images[i].append(image)

    return images