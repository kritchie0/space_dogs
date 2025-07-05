from enum import IntEnum


class FrameTypes(IntEnum):
    Idle = 0,
    Walking = 1,
    Running = 2

class Directions(IntEnum):
    Up = 0,
    Down = 1,
    Left = 2,
    Right = 3,
    Idle = 4
