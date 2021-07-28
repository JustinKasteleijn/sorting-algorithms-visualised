from pygame import display


class Screen:
    def __init__(self, width, height):
        self.display = display
        self.surface = self.display.set_mode((width, height))

    def fill(self, color):
        self.surface.fill(color=color)
        self.display.flip()
