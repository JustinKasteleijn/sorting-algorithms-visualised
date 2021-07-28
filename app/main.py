import pygame
from pygameData.Screen import Screen

screen = Screen(500, 500)
screen.fill((255, 255, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
