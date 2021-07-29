import pygame
from pygameData.Screen import Screen


class App:
    def __init__(self):
        self.running = False
        pygame.init()

    def run(self):
        screen = Screen(500, 500)
        screen.fill((255, 255, 0))
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()


if __name__ == "__main__":
    App().run()
