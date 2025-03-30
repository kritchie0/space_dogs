import pygame

import assets
import globals

from enums import Inputs, Directions


class Player:
    def __init__(self, filepath_assets_):
        self.assets = assets.loadAssets(filepath_assets_)
        self.frame = 0
        self.sprite = None
        self.direction = None
        self.position = globals.PLAYER_STARTING_POSITION

    def Update(self, player_input_):
        player_input = player_input_
        self.__handleDirection(player_input[Inputs.Keyboard])


    def __handleDirection(self, input_keyboard_):
        input_keyboard = input_keyboard_

        if input_keyboard == pygame.K_w: self.direction = "up"
        if input_keyboard == pygame.K_s: self.direction = "down"
        if input_keyboard == pygame.K_a: self.direction = "left"
        if input_keyboard == pygame.K_d: self.direction = "right"
        else: self.direction = "idle"

    def __handleAnimation(self):
        if self.direction == Directions.Up:
            print("Direction: Up")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = globals.FRAME_OFFSET_UP + self.frame

        elif self.direction == Directions.Down:
            print("Direction: Down")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.down[self.frame]

        elif self.direction == Directions.Left:
            print("Direction: Left")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.left[self.frame]

        elif self.direction == Directions.Right:
            print("Direction: Right")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.right[self.frame]

        elif self.direction == Directions.Idle:
            print("Direction: Idle")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.idle[self.frame]
