import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
    screen.fill((0, 170, 250))
