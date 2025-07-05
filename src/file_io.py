#--- file_io.py ---#
import os
from loguru import logger

def rename_file(path_to_src: str, path_to_dst: str):
    logger.debug(f"Renaming: {path_to_src} to {path_to_dst}")
    os.rename(src=path_to_src, dst=path_to_dst)

def replace_file(path_to_src: str, path_to_dst: str):
    logger.debug(f"Replacing: {path_to_src} to {path_to_dst}")
    os.replace(src=path_to_src, dst=path_to_dst)
