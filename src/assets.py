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


"""
    Player sprite file paths.
"""
FILE_PATH_PLAYER_UP_1 = "../Assets/Player_Up_1.png"
FILE_PATH_PLAYER_UP_2 = "../Assets/Player_Up_2.png"
FILE_PATH_PLAYER_UP_3 = "../Assets/Player_Up_3.png"
FILE_PATH_PLAYER_UP_4 = "../Assets/Player_Up_4.png"
PLAYER_UP_SPRITES = [FILE_PATH_PLAYER_UP_1, FILE_PATH_PLAYER_UP_2, FILE_PATH_PLAYER_UP_3, FILE_PATH_PLAYER_UP_4]

FILE_PATH_PLAYER_DOWN_1 = "../Assets/Player_Down_1.png"
FILE_PATH_PLAYER_DOWN_2 = "../Assets/Player_Down_2.png"
FILE_PATH_PLAYER_DOWN_3 = "../Assets/Player_Down_3.png"
FILE_PATH_PLAYER_DOWN_4 = "../Assets/Player_Down_4.png"
PLAYER_DOWN_SPRITES = [FILE_PATH_PLAYER_DOWN_1, FILE_PATH_PLAYER_DOWN_2, FILE_PATH_PLAYER_DOWN_3, FILE_PATH_PLAYER_DOWN_4]

FILE_PATH_PLAYER_LEFT_1 = "../Assets/Player_Left_1.png"
FILE_PATH_PLAYER_LEFT_2 = "../Assets/Player_Left_2.png"
FILE_PATH_PLAYER_LEFT_3 = "../Assets/Player_Left_3.png"
FILE_PATH_PLAYER_LEFT_4 = "../Assets/Player_Left_4.png"
PLAYER_LEFT_SPRITES = [FILE_PATH_PLAYER_LEFT_1, FILE_PATH_PLAYER_LEFT_2, FILE_PATH_PLAYER_LEFT_3, FILE_PATH_PLAYER_LEFT_4]

FILE_PATH_PLAYER_RIGHT_1 = "../Assets/Player_Right_1.png"
FILE_PATH_PLAYER_RIGHT_2 = "../Assets/Player_Right_2.png"
FILE_PATH_PLAYER_RIGHT_3 = "../Assets/Player_Right_3.png"
FILE_PATH_PLAYER_RIGHT_4 = "../Assets/Player_Right_4.png"
PLAYER_RIGHT_SPRITES = [FILE_PATH_PLAYER_RIGHT_1, FILE_PATH_PLAYER_RIGHT_2, FILE_PATH_PLAYER_RIGHT_3, FILE_PATH_PLAYER_RIGHT_4]

FILE_PATH_PLAYER_IDLE_1 = "../Assets/Player_Down_1.png"
PLAYER_IDLE_SPRITES = [FILE_PATH_PLAYER_IDLE_1, FILE_PATH_PLAYER_IDLE_1, FILE_PATH_PLAYER_IDLE_1, FILE_PATH_PLAYER_IDLE_1]

PATHS_PLAYER = [PLAYER_UP_SPRITES, PLAYER_DOWN_SPRITES, PLAYER_LEFT_SPRITES, PLAYER_RIGHT_SPRITES, PLAYER_IDLE_SPRITES]