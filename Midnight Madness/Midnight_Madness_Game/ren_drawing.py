import pygame
import sys

x = 75
y = 50
win = pygame.display.set_mode((1500, 750), 0, 32)
win.fill((36,38,47))

BLACK = (0, 0, 0)

# Head
pygame.draw.ellipse(win, BLACK, [1 + x, y, 10, 10], 0)

# Legs
#Right leg (colour, length of leg....)
pygame.draw.line(win, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
#Left Leg
pygame.draw.line(win, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

# Body
pygame.draw.line(win, BLACK, [5 + x, 17 + y], [5 + x, 7 + y], 2)

# Arms
pygame.draw.line(win, BLACK, [5 + x, 7 + y], [9 + x, 17 + y], 2)
pygame.draw.line(win, BLACK, [5 + x, 7 + y], [1 + x, 17 + y], 2)