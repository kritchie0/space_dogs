#--- test_game.py ---#

import globals

def test_space_dogs():
    for i, type in enumerate(globals.FRAME_TYPES):
        print(f"i={i}, type={type}")

        for n in range(len(type)):
            print(f"frame={type[n]}, n={n+1}")
