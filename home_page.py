import pygame
from pygame.locals import *

pygame.init()

width = 1100
height = 550
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height), 0, 32)
screen.fill(white)
pygame.display.set_caption("Game library")
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
