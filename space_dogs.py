import sys
import pygame


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]

# Player
PLAYER_SPRITE_PATH = "./Assets"
PLAYER_SPRITE_UP = "/Player_Up"
PLAYER_SPRITE_DOWN = "/Player_Down"
PLAYER_SPRITE_LEFT = "/Player_Left"
PLAYER_SPRITE_RIGHT = "/Player_Right"

PLAYER_POS_INIT = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
PLAYER_SPEED = 200



def space_dogs():
    print("bork bork...in space...")

    # Setup
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    clock: pygame.Clock = pygame.time.Clock()
    is_running: bool = True
    dt: int = 0

    player_pos = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Quit game if user presses 'X' button on screen.
    while is_running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill("black")

        input_key =  pygame.key.get_pressed()
        if input_key[pygame.K_w]:
            player_pos.y -= 200 * dt


def show(image):
    screen = pygame.display.get_surface()
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pygame.display.flip()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
            break


pygame.init()
pygame.display.init()

pygame.display.set_mode((255, 255))
surface = pygame.image.load("./Assets/Dog000.png").convert()
pygame.display.flip()
show(surface)

if __name__ == "__main__":
    space_dogs()