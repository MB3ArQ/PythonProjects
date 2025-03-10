import pygame
import attributes as attr
from math import sqrt
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((800, 800))

width = 15
height = 15

cell_size = int(sqrt(((screen.get_width() - (attr.PANEL_FRAME_INDENT * 2)) * (screen.get_height() - (attr.PANEL_FRAME_INDENT * 2))) / (width * height)))

g = attr.Grid(width = width, height = height, 
              cell_size = cell_size, 
              left = (screen.get_width() / 2) - (width * cell_size / 2),
              top = (screen.get_height() / 2) - (height * cell_size / 2),
              border_color = THECOLORS['darkred'])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(0)
    g.draw(screen)
    pygame.display.update()
    

