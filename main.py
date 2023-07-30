import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('assets/spaceships/entourage.png')
pygame.display.set_icon(icon)

spaceship_assets = [spaceship for spaceship in os.listdir('./assets/spaceships/')]
player = random.choice(spaceship_assets)
player_name = player.replace('_', ' ').replace('.png', '')
enemy_assets = [enemy for enemy in os.listdir('./assets/enemy/')]
enemy = random.choice(enemy_assets)
enemy_name = enemy.replace('_', ' ').replace('.png', '')
playerImg = pygame.image.load(f'assets/spaceships/{player}')
enemyImg = pygame.image.load(f'assets/enemy/{enemy}')
print(f"{player_name} vs. {enemy_name}")


def draw_player(playerXloc: float, playerYloc: float):
    screen.blit(playerImg, (playerXloc, playerYloc))


def draw_enemy(enemyXloc: float, enemyYloc: float):
    screen.blit(enemyImg, (enemyXloc, enemyYloc))


enemyX = random.randint(0, 650)
enemyY = -20

playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

running = True
while running:

    screen.fill((0, 0, 0))  # R,G,B
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            elif event.key == pygame.K_UP:
                playerY_change = -0.3
            elif event.key == pygame.K_DOWN:
                playerY_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    enemyY += 0.1
    draw_enemy(enemyX, enemyY)
    if playerX <= 30:
        playerX = 30
    elif playerX >= 700:
        playerX = 700
    if playerY <= 30:
        playerY = 30
    elif playerY >= 500:
        playerY = 500
    playerX += playerX_change
    playerY += playerY_change
    draw_player(playerX, playerY)
    draw_enemy(enemyX, enemyY)
    pygame.display.update()
