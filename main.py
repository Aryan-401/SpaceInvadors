import pygame

screen = pygame.display.set_mode((640, 480))

# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('assets/spaceships/entourage.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
