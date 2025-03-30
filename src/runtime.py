import pygame
from enum import StrEnum


EXTENSIONS: [int, str] = ['png', 'gif', 'jpg', 'jpeg', 'bmp']

FILE_PATH_ROOT = "space_dogs/"
FILE_PATH_ASSETS = "Assets/"

FILE_PATH_PLAYER_UP = "Player_Up/"
FILE_PATH_PLAYER_DOWN = "Player_Down/"
FILE_PATH_PLAYER_LEFT = "Player_Left/"
FILE_PATH_PLAYER_RIGHT = "Player_Right/"


def loadImage(file_: str, ext_: str):
    Path: str = FILE_PATH_ROOT + FILE_PATH_ASSETS + file_ + ext_
    return pygame.image.load(path_).convert_alpha()

class ImageLoader(object):
    TYPE = 'image'

    @staticmethod
    def _load(path):
        return pygame.image.load(path).convert_alpha()
