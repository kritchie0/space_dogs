# ------------- #
# - Utilities - #
# ------------- #
import os
from pygame import Surface
from pygame import image

from loguru import logger

def rename_file(path_to_src: str, path_to_dst: str):
    logger.debug(f"Renaming: {path_to_src} to {path_to_dst}")
    os.rename(src=path_to_src, dst=path_to_dst)

def replace_file(path_to_src: str, path_to_dst: str):
    logger.debug(f"Replacing: {path_to_src} to {path_to_dst}")
    os.replace(src=path_to_src, dst=path_to_dst)

def load_png(path_to_file: str) -> Surface:
    return image.load(path_to_file).convert_alpha()


def load_images(file_: [str]):
    images = []

    for i in range(len(file_)):
        images.append([])

        for n in range(len(file_[0])):
            image = image.load(file_[i][n]).convert_alpha()
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

