import pygame


class ImageLoader(object):
    EXTENSIONS: [int, str] = ['png', 'gif', 'jpg', 'jpeg', 'bmp']
    TYPE = 'image'

    @staticmethod
    def _load(path):
        return pygame.image.load(path).convert_alpha()
