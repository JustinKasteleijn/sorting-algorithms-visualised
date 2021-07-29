from pygame import display, draw, Rect
from typing import List


class Screen:

    def __init__(self, width, height):
        self.display = display
        self.surface = self.display.set_mode((width, height))

    def fill(self, color) -> None:
        self.surface.fill(color=color)
        self.display.flip()

    def draw(self, integers: List[int]) -> None:
        for integer in integers:
            self.drawRect(integer, 50)
            self.display.flip()

    def drawRect(self, height: int, width: int) -> None:
        draw.rect(self.surface, (0, 0, 0), Rect(0, self.surface.get_height() - height, width, height))
