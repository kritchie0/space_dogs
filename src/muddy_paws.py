import enum

import pygame
from enum import auto
from dataclasses import dataclass


@dataclass
class Ext:
    png: str = 'png'
    gif: str = 'gif'
    bmp: str = 'bmp'
    jpg: str = 'jpg'
    jpeg: str = 'jpeg'

@dataclass
class Direction(auto):
    Up: int = auto
    Down: int = auto
    Left: int = auto
    Right: int = auto
    Idle: int = auto

# FRAME CONSTANTS
MAX_FPS = 60
MAX_ANIMATION_FRAMES = 4
MAX_FPS_ANIMATION_COUNTS = MAX_FPS / MAX_ANIMATION_FRAMES


## ASSET FILE PATHS
FILE_PATH_PLAYER_UP_1 = "./Assets/Player_Up_1.png"
FILE_PATH_PLAYER_UP_2 = "./Assets/Player_Up_2.png"
FILE_PATH_PLAYER_UP_3 = "./Assets/Player_Up_3.png"
FILE_PATH_PLAYER_UP_4 = "./Assets/Player_Up_4.png"
PLAYER_UP_SPRITES = [FILE_PATH_PLAYER_UP_1, FILE_PATH_PLAYER_UP_2, FILE_PATH_PLAYER_UP_3, FILE_PATH_PLAYER_UP_4]

FILE_PATH_PLAYER_DOWN_1 = "./Assets/Player_Down_1.png"
FILE_PATH_PLAYER_DOWN_2 = "./Assets/Player_Down_2.png"
FILE_PATH_PLAYER_DOWN_3 = "./Assets/Player_Down_3.png"
FILE_PATH_PLAYER_DOWN_4 = "./Assets/Player_Down_4.png"
PLAYER_DOWN_SPRITES = [FILE_PATH_PLAYER_DOWN_1, FILE_PATH_PLAYER_DOWN_2, FILE_PATH_PLAYER_DOWN_3, FILE_PATH_PLAYER_DOWN_4]

FILE_PATH_PLAYER_LEFT_1 = "./Assets/Player_Left_1.png"
FILE_PATH_PLAYER_LEFT_2 = "./Assets/Player_Left_2.png"
FILE_PATH_PLAYER_LEFT_3 = "./Assets/Player_Left_3.png"
FILE_PATH_PLAYER_LEFT_4 = "./Assets/Player_Left_4.png"
PLAYER_LEFT_SPRITES = [FILE_PATH_PLAYER_LEFT_1, FILE_PATH_PLAYER_LEFT_2, FILE_PATH_PLAYER_LEFT_3, FILE_PATH_PLAYER_LEFT_4]

FILE_PATH_PLAYER_RIGHT_1 = "./Assets/Player_Right_1.png"
FILE_PATH_PLAYER_RIGHT_2 = "./Assets/Player_Right_2.png"
FILE_PATH_PLAYER_RIGHT_3 = "./Assets/Player_Right_3.png"
FILE_PATH_PLAYER_RIGHT_4 = "./Assets/Player_Right_4.png"
PLAYER_RIGHT_SPRITES = [FILE_PATH_PLAYER_RIGHT_1, FILE_PATH_PLAYER_RIGHT_2, FILE_PATH_PLAYER_RIGHT_3, FILE_PATH_PLAYER_RIGHT_4]

FILE_PATH_PLAYER_IDLE_1 = "./Assets/Player_Idle_1.png"
PLAYER_IDLE_SPRITES = [FILE_PATH_PLAYER_IDLE_1, FILE_PATH_PLAYER_IDLE_1, FILE_PATH_PLAYER_IDLE_1, FILE_PATH_PLAYER_IDLE_1]


class MuddySprite(object):
    def __init__(self, fp_up_: [int, str], fp_down_: [int, str],
                 fp_right_: [int, str], fp_left_: [int, str], fp_idle_: [int, str]):
        self.up = self.__load(fp_up_)
        self.down = self.__load(fp_down_)
        self.left = self.__load(fp_left_)
        self.right = self.__load(fp_right_)
        self.idle = self.__load(fp_idle_)

    @staticmethod
    def __load(fp_: [int, str]):
        frames = []
        for i in range(len(fp_)):
            print(fp_[i])
            image = pygame.image.load(fp_[i]).convert_alpha()
            frames.append(image)

        return frames


class MuddyPlayer(MuddySprite):
    def __init__(self):
        super().__init__(PLAYER_UP_SPRITES, PLAYER_DOWN_SPRITES,
                         PLAYER_RIGHT_SPRITES, PLAYER_LEFT_SPRITES, PLAYER_IDLE_SPRITES)
        self.frame: int = 0
        self.sprite: pygame.Surface = self.idle[self.frame]

        self.position: pygame.Vector2 = pygame.Vector2(0.0, 0.0)

    def Update(self):
        ...

    def __handleAnimation(self):
        if self.direction == Direction.Up:
            print("Direction: Up")
            self.frame = (self.frame + 1) % MAX_ANIMATION_FRAMES
            self.sprite = self.up[self.frame]

        elif self.direction == Direction.Down:
            print("Direction: Down")
            self.frame = (self.frame + 1) % MAX_ANIMATION_FRAMES
            self.sprite = self.down[self.frame]

        elif self.direction == Direction.Left:
            print("Direction: Left")
            self.frame = (self.frame + 1) % MAX_ANIMATION_FRAMES
            self.sprite = self.left[self.frame]

        elif self.direction == Direction.Right:
            print("Direction: Right")
            self.frame = (self.frame + 1) % MAX_ANIMATION_FRAMES
            self.sprite = self.right[self.frame]

        elif self.direction == Direction.Idle:
            print("Direction: Idle")
            self.frame = (self.frame + 1) % MAX_ANIMATION_FRAMES
            self.sprite = self.idle[self.frame]
