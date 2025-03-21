import pygame
from dataclasses import dataclass


@dataclass
class Ext:
    png: str = 'png'
    gif: str = 'gif'
    bmp: str = 'bmp'
    jpg: str = 'jpg'
    jpeg: str = 'jpeg'


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


class MuddySprite(object):
    def __init__(self, fp_up_: [int, str], fp_down_: [int, str], fp_right_: [int, str], fp_left_: [int, str]):
        self.up = self.__load(fp_up_)
        self.down = self.__load(fp_down_)
        self.left = self.__load(fp_left_)
        self.right = self.__load(fp_right_)

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
        super().__init__(PLAYER_UP_SPRITES, PLAYER_DOWN_SPRITES, PLAYER_RIGHT_SPRITES, PLAYER_LEFT_SPRITES)
        self.currentFrame: int = 0

