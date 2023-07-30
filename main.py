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


def draw_player(playerX: int, playerY: int):
    screen.blit(playerImg, (playerX, playerY))


playerX = 370
playerY = 480

running = True
while running:

    screen.fill((0, 0, 0))  # R,G,B
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_player(playerX, playerY)
    pygame.display.update()
