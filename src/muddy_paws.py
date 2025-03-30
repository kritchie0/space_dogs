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
