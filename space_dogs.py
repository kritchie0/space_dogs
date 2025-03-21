import sys
import pygame

from src.sprites import player
from src.muddy_paws import MuddyPlayer

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]

# Player
PLAYER_SPRITE_PATH = "./Assets"
PLAYER_DOWN_SPRITE = "./Assets/Player_Down_1.png"
PLAYER_UP_SPRITE = "./Assets/Player_Up_1.png"

PLAYER_POS_INIT = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
PLAYER_SPEED = 200


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
    SpaceDog = MuddyPlayer()
    Frame = SpaceDog.down[0]

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

        input_key =  pygame.key.get_pressed()
        if input_key[pygame.K_w]:
            DogPosition.y -= 200 * dt
            SpaceDog.currentFrame += 1 % 4
            Frame = SpaceDog.up[SpaceDog.currentFrame]

        if input_key[pygame.K_s]:
            DogPosition.y += 200 * dt
            SpaceDog.currentFrame += 1 % 4
            Frame = SpaceDog.down[SpaceDog.currentFrame]

        if input_key[pygame.K_a]:
            DogPosition.x -= 200 * dt
            SpaceDog.currentFrame += 1 % 4
            Frame = SpaceDog.left[SpaceDog.currentFrame]

        if input_key[pygame.K_d]:
            DogPosition.x += 200 * dt
            SpaceDog.currentFrame += 1 % 4
            Frame = SpaceDog.right[SpaceDog.currentFrame]

        # Player.Update(player_pos)
        # Limit fps to 60
        dt = clock.tick(60) / 1000
        show(Frame, DogPosition)

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
