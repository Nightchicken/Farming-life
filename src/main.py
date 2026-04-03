import pygame

screen = pygame.display.set_mode([500, 500])
running = True


def draw():
    screen.fill(0)
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
