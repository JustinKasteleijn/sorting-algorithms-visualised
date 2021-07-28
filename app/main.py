import pygame
from pygameData.Screen import Screen

screen = Screen(500, 500)
screen.display("Hello")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
