# -------------- #
# - Space Dogs - #
# -------------- #
import os
import assets
from loguru import logger

import assets
from space_dogs import load_spaceDogs

if __name__ == "__main__":
    logger.info("Renaming files...")
    os.replace("../player/walk_up_1.png", "../player/walk/up_frame_1.png")
    os.replace("../player/walk_up_2.png", "../player/walk/up_frame_1.png")
    os.replace("../player/walk_up_3.png", "../player/walk/up_frame_1.png")
    os.replace("../player/walk_up_4.png", "../player/walk/up_frame_1.png")

    os.replace("../player/walk_down_1.png", "../player/walk/down_frame_1.png")
    os.replace("../player/walk_down_2.png", "../player/walk/down_frame_2.png")
    os.replace("../player/walk_down_3.png", "../player/walk/down_frame_3.png")
    os.replace("../player/walk_down_4.png", "../player/walk/down_frame_4.png")

    os.replace("../player/walk_left_1.png", "../player/walk/left_frame_1.png")
    os.replace("../player/walk_left_2.png", "../player/walk/left_frame_2.png")
    os.replace("../player/walk_left_3.png", "../player/walk/left_frame_3.png")
    os.replace("../player/walk_left_4.png", "../player/walk/left_frame_4.png")

    os.replace("../player/walk_right_1.png", "../player/walk/right_frame_1.png")
    os.replace("../player/walk_right_2.png", "../player/walk/right_frame_2.png")
    os.replace("../player/walk_right_3.png", "../player/walk/right_frame_3.png")
    os.replace("../player/walk_right_4.png", "../player/walk/right_frame_4.png")

    os.replace("../player/run_left_1.png", "../player/run/left_frame_1.png")
    os.replace("../player/run_left_2.png", "../player/run/left_frame_2.png")
    os.replace("../player/run_left_3.png", "../player/run/left_frame_3.png")

    os.replace("../player/run_right_1.png", "../player/run/right_frame_1.png")
    os.replace("../player/run_right_2.png", "../player/run/right_frame_2.png")
    os.replace("../player/run_right_3.png", "../player/run/right_frame_3.png")

    os.replace("../player/idle_1.png", "../player/idle/frame_1.png")
    os.replace("../player/idle_2.png", "../player/idle/frame_2.png")


    logger.info("Done.")
    # logger.info("Starting Space Dogs..." )
    # load_spaceDogs()