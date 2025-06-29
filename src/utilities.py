# ------------- #
# - Utilities - #
# ------------- #
import os
from os import rename
import pygame

def rename_file(path_to_old_file: str, path_to_new_file):
    os.rename(path_to_old_file, path_to_new_file)

def load_image(fp_):
    return pygame.image.load(fp_).convert_alpha()

def load_images(file_: [str]):
    images = []

    for i in range(len(file_)):
        images.append([])

        for n in range(len(file_[0])):
            image = pygame.image.load(file_[i][n]).convert_alpha()
            images[i].append(image)

    return images


def place_dog(position):
    dog_fp = "../Assets/Player_Down_1.png"

    image = load_image(dog_fp)
    image = pygame.transform.scale_by(image, 4)

    surface = pygame.display.get_surface()
    surface.fill((255, 255, 255))
    surface.blit(image, position)
    pygame.display.flip()

