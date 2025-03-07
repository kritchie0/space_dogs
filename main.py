import sys
import pygame

print("bork bork...in space...")


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
