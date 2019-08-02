import pygame
import sys
import random
from ground import Ground
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player((110, 191, 78))
grounds = []

pygame.time.set_timer(pygame.USEREVENT+1, 700)

def addGround(xLeft, yUp, yVelocity, width):
    global grounds
    grounds.append(Ground(xLeft, yUp, yVelocity, width, (166, 50, 168)))

def touchingGround():
    global grounds, player
    for ground in grounds:
        if player.yUp + player.size < ground.yUp + 21 and player.xLeft + player.size > ground.xLeft and player.xLeft < ground.xLeft + ground.width and player.yUp > ground.yUp - 20:
            return True
    return False

def init():
    addGround(300, 50, 2, 200)

init()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT+1:
            addGround(random.randint(0, 700), 50, 2, random.randint(50, 300))
            addGround(random.randint(0, 700), 50, 2, random.randint(50, 300))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and touchingGround():
                player.jump(10)
            if event.key == pygame.K_LEFT:
                player.xVelocity = -5
            if event.key == pygame.K_RIGHT:
                player.xVelocity = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.xVelocity = 0
            if event.key == pygame.K_RIGHT:
                player.xVelocity = 0
    for ground in grounds:
        pygame.draw.rect(screen, ground.color, pygame.Rect(ground.xLeft, ground.yUp, ground.width, ground.height), 0)
        ground.move()
        if ground.checkDestroy():
            grounds.remove(ground)
    pygame.draw.rect(screen, player.color, pygame.Rect(player.xLeft, player.yUp, player.width, player.height), 0)
    if not touchingGround():
        player.applyGravity(0.5)
    else:
        player.yVelocity = 2
    player.move()
    pygame.display.flip()
    screen.fill((0, 170, 250))
