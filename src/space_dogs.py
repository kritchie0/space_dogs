import sys
import pygame
from dataclasses import dataclass
# from src.sprites import player
# from src.muddy_paws import MuddyPlayer
import assets
from player import Player

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 430
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]


PLAYER_POS_INIT = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
PLAYER_SPEED = 200


class GameState:
    def __init__(self, position_):
        self.Direction = None
        self.Position = position_



def show(image, pos: pygame.Vector2,):
    screen = pygame.display.get_surface()
    screen.fill((255, 255, 255))
    screen.blit(image, (pos.x, pos.y))
    pygame.display.flip()


def Initialize_SpaceDogs():
    ...


def space_dogs():
    print("bork bork...in space...")

    # Setup
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    clock: pygame.Clock = pygame.time.Clock()
    is_running: bool = True
    dt: float = 0

    DogPosition = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
    SpaceDog = Player(assets.PATHS_PLAYER)

    # PlayerImages = player.PlayerImages()
    # Player = player.PlayerEntity(PlayerImages, PLAYER_POS_INIT)
    DogPosition.x = 0
    DogPosition.y = 0

    # image: pygame.Surface = pygame.image.load(PLAYER_DOWN_SPRITE).convert()
    # image2: pygame.Surface = pygame.image.load(PLAYER_UP_SPRITE).convert()


    # Quit game if user presses 'X' button on screen.
    while is_running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill("white")
        FPSLimiter = clock.tick(60) / 1000

        SpaceDog.Update(FPSLimiter)

        # Player Render
        surface = pygame.display.get_surface()
        surface.fill((255, 255, 255))
        surface.blit(SpaceDog.sprite, (SpaceDog.position_x, SpaceDog.position_y))
        pygame.display.flip()
        # if input_key[pygame.K_w]:
        #     DogPosition.y -= 200 * dt
        #     SpaceDog.currentFrame += 1 % 4
        #     Frame = SpaceDog.up[SpaceDog.currentFrame]
        #
        # if input_key[pygame.K_s]:
        #     DogPosition.y += 200 * dt
        #     SpaceDog.currentFrame += 1 % 4
        #     Frame = SpaceDog.down[SpaceDog.currentFrame]
        #
        # if input_key[pygame.K_a]:
        #     DogPosition.x -= 200 * dt
        #     SpaceDog.currentFrame += 1 % 4
        #     Frame = SpaceDog.left[SpaceDog.currentFrame]
        #
        # if input_key[pygame.K_d]:
        #     DogPosition.x += 200 * dt
        #     SpaceDog.currentFrame += 1 % 4
        #     Frame = SpaceDog.right[SpaceDog.currentFrame]

        # Player.Update(player_pos)
        # Limit fps to 60
        # dt = clock.tick(60) / 1000
        # show(Frame, DogPosition)

    pygame.quit()


# def show(image):
#     screen = pygame.display.get_surface()
#     screen.fill((255, 255, 255))
#     screen.blit(image, (0, 0))
#     pygame.display.flip()
#     while True:
#         event = pygame.event.wait()
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
#             break
#
#
# pygame.init()
# pygame.display.init()
#
# pygame.display.set_mode((255, 255))
# surface = pygame.image.load("./Assets/Dog000.png").convert()
# pygame.display.flip()
# show(surface)



if __name__ == "__main__":
    space_dogs()
