import pygame
from pygame import Surface
from dataclasses import dataclass

import globals
from assets import loadAssets
from enums import Directions


class Player:
    def __init__(self, filepath_assets):
        self.assets = loadAssets(filepath_assets)
        self.frame = 0
        self.sprite = None
        self.direction = None
        self.position_x = globals.PLAYER_STARTING_POSITION[0]
        self.position_y = globals.PLAYER_STARTING_POSITION[1]
        self.FPSLimiter = None

        print(self.assets)

    def Update(self, FPSLimiter):
        self.FPSLimiter = FPSLimiter

        self.__handlePosition()
        self.__handleAnimation()
        self.__render()


    def __handlePosition(self):
        input_keyboard = pygame.key.get_pressed()

        if input_keyboard[pygame.K_w]:
            self.direction = Directions.Up
            self.position_y -= 200 * self.FPSLimiter
            print(f"direction: {self.direction}")

        elif input_keyboard[pygame.K_s]:
            self.direction = Directions.Down
            self.position_y += 200 * self.FPSLimiter

        elif input_keyboard[pygame.K_a]:
            self.direction = Directions.Left
            self.position_x -= 200 * self.FPSLimiter

        elif input_keyboard[pygame.K_d]:
            self.direction = Directions.Right
            self.position_x += 200 * self.FPSLimiter

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

    def __render(self):
        print(f"direction: {self.direction} frame: {self.frame}")
        surface = pygame.display.get_surface()
        surface.fill((255, 255, 255))
        surface.blit(self.sprite, (self.position_x, self.position_y))
        pygame.display.flip()
