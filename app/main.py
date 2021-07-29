import pygame
from pygameData.Screen import Screen


class App:
    def __init__(self):
        self.running = False
        pygame.init()

    def run(self) -> None:
        screen = Screen(800, 700)
        screen.fill((255, 255, 255))
        self.running = True
        while self.running:
            screen.draw(integers=[50, 500, 30])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()


if __name__ == "__main__":
    App().run()
