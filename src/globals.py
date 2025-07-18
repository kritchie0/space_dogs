from enums import IntEnum

"""
    Constants
"""
MAX_FPS = 60

MAX_IDLE_FRAMES = 4
MAX_WALKING_FRAMES = 4
MAX_RUNNING_FRAMES = 3

MAX_ANIMATION_FRAMES = 4

FRAME_TYPES = [
    ['idle_down'],
    ['walking_up', 'walking_down', 'walking_left', 'walking_right'],
    ['running_up', 'running_down', 'running_left', 'running_right']
]

class FrameTypesEnum(IntEnum):
    Idle    = 0
    Walking = 1
    Running = 2

MAX_FPS_ANIMATION_COUNTS = MAX_FPS / MAX_ANIMATION_FRAMES

FRAME_OFFSET_UP = MAX_ANIMATION_FRAMES * 0
FRAME_OFFSET_DOWN = MAX_ANIMATION_FRAMES * 1
FRAME_OFFSET_LEFT = MAX_ANIMATION_FRAMES * 2
FRAME_OFFSET_RIGHT = MAX_ANIMATION_FRAMES * 3

PLAYER_STARTING_POSITION_X = 0.0
PLAYER_STARTING_POSITION_Y = 0.0
