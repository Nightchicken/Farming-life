import pygame


class Plant(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, image=None):
        # NOTE sprite render
        super().__init__()
        self.image = pygame.Surface([32, 32])
        if image is None:
            self.image.fill([0, 255, 160])
        self.rect = [x, y, 32, 32]

        # Plant logic
        self.hydration  # scales 0-100

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)
