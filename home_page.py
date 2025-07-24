import pygame
from pygame.locals import *
import sys
import random

pygame.init()

width = 1100
height = 550
white = (255, 255, 255)
black = (0, 0, 0)
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Game library")

font = pygame.font.Font(None, 28)

button_rect = pygame.Rect(60, 400, 120, 40)


def draw_title():
    global font, random_color

    text = font.render("This is a Game Library", True, white, random_color)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 8)
    screen.blit(text, text_rect)


def draw_buttons():
    global font, button_rect

    pygame.draw.rect(screen, (250, 0, 0), button_rect)
    button_text = font.render("button 1", True, white)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


def button_click():
    global random_color

    x, y = pygame.mouse.get_pos()

    if button_rect.collidepoint(x, y):
        random_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        return


running = True
while running:
    screen.fill(white)
    draw_title()
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            button_click()

    pygame.display.update()
