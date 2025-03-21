import pygame


ASSET_FILE_PATH = "./Assets"


class SD_Sprite(object):
    def __init__(self, path_: str):
        self.sprites: str = path_
        self.spriteUp: str = path_ + "_Up"


class LoadFramesPNG:
    def __init__(self, filename_: str, tag_: str, frames_: int, filetype_: str):
        self.frames = []
        for i in range(frames_):
            path: str = ASSET_FILE_PATH + "/" + filename_ + "_" + tag_ + "_" + str(i+1) + "." + filetype_
            print(path)
            image: pygame.Surface = pygame.image.load(path).convert_alpha()
            self.frames.append(image)


class AnimationFrames:
    def __init__(self, filename_: str):
        self.idle = LoadFramesPNG(filename_=filename_, tag_="Down", frames_=1, filetype_="png")
        self.down = LoadFramesPNG(filename_=filename_, tag_="Down", frames_=4, filetype_="png")
        self.up = LoadFramesPNG(filename_=filename_, tag_="Up", frames_=4, filetype_="png")
        self.left = LoadFramesPNG(filename_=filename_, tag_="Left", frames_=4, filetype_="png")
        self.right = LoadFramesPNG(filename_=filename_, tag_="Right", frames_=4, filetype_="png")


class PlayerImages(AnimationFrames):
    def __init__(self):
        super().__init__("Player")


class PlayerEntity(pygame.sprite.Sprite):
    def __init__(self, images_: PlayerImages, position_):
        super().__init__()  # Initialize base class.

        self.animation: PlayerImages = images_
        self.frame: int = 0
        self.current = self.animation.idle
        self.image = self.current.frames[self.frame]
        self.collision_box = self.image.get_rect(center=position_)

    def _load(self):
        ...

    def Update(self, position_):
        self.frame = (self.frame + 1) % len(self.current.frames)
        self.collision_box = self.image.get_rect(center=position_)

        screen = pygame.display.get_surface()
        screen.blit(self.image, position_)

