import pygame
from pygame import Surface
from dataclasses import dataclass

import assets
import globals

from enums import Directions


class Player:
    def __init__(self, filepath_assets):
        self.assets = assets.loadAssets(filepath_assets)
        self.frame = 0
        self.sprite = None
        self.direction = None
        self.position = globals.PLAYER_STARTING_POSITION
        self.FPSLimiter = None

    def Update(self, clock: pygame.Clock):
        self.FPSLimiter = clock.tick(globals.MAX_FPS) / 1000
        self.__handlePosition()
        self.__handleAnimation()


    def __handlePosition(self):
        input_keyboard = pygame.key.get_pressed()

        if self.direction != input_keyboard:
            self.frame = 0

        if input_keyboard == pygame.K_w: self.direction = Directions.Up
        elif input_keyboard == pygame.K_s: self.direction = Directions.Down
        elif input_keyboard == pygame.K_a: self.direction = Directions.Left
        elif input_keyboard == pygame.K_d: self.direction = Directions.Right
        else: self.direction = Directions.Idle


    def __handleAnimation(self):
        if self.direction == Directions.Up:
            print("Direction: Up")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.assets[self.direction][self.frame]

        elif self.direction == Directions.Down:
            print("Direction: Down")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.assets[self.direction][self.frame]

        elif self.direction == Directions.Left:
            print("Direction: Left")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.assets[self.direction][self.frame]

        elif self.direction == Directions.Right:
            print("Direction: Right")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.assets[self.direction][self.frame]

        elif self.direction == Directions.Idle:
            print("Direction: Idle")
            self.frame = (self.frame + 1) % globals.MAX_ANIMATION_FRAMES
            self.sprite = self.assets[self.direction][self.frame]

        def __handlePosition(self):
            ...
