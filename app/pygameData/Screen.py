from pygame import display


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def display(self, caption: str):
        display.set_caption(caption)
        display.set_mode((self.width, self.height))
