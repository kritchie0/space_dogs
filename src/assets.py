import os

import pygame
from os import rename

def loadAssets(files):
    assets = []

    for i in range(len(files)):
        assets.append([])

        for n in range(len(files[0])):
            image = pygame.image.load(files[i][n]).convert_alpha()
            assets[i].append(image)

    return assets


