import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((640, 480))

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

player = pygame.image.load(f'assets/spaceships/{player}')
enemy = pygame.image.load(f'assets/enemy/{enemy}')
print(f"{player_name} vs. {enemy_name}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # R,G,B
    pygame.display.update()
