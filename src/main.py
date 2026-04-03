# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pygame"
# ]
# ///
import pygame
from plant import Plant

screen = pygame.display.set_mode([500, 500])
running = True

plant = Plant(10, 10)


def draw():
    screen.fill(0)
    plant.draw(screen)
    pygame.display.update()
    pass


def physics():
    pass


if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
