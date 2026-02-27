import pygame, random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bird Platformer')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Load assets
background = pygame.image.load('forest_background.jpg')
bird_image = pygame.image.load('bird_image.png')
bird_rect = bird_image.get_rect(center=(100, HEIGHT // 2))

# Game variables
velocity_y = 0
gravity = 0.5
jump_strength = -10

# Main game loop
running = True
ticks = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move up
        bird_rect.y += velocity_y
        velocity_y += gravity
    if keys[pygame.K_s]:  # Move down
        bird_rect.y += 5
    if keys[pygame.K_a]:  # Move left
        bird_rect.x -= 5
    if keys[pygame.K_d]:  # Move right
        bird_rect.x += 5
    if keys[pygame.K_SPACE]:  # Jump
        velocity_y = jump_strength

    # Keep bird within the screen
    if bird_rect.y <= 0:
        bird_rect.y = 0
    if bird_rect.y >= HEIGHT:
        bird_rect.y = HEIGHT - bird_rect.height

    # Draw everything
    screen.blit(background, (0, 0))
    screen.blit(bird_image, bird_rect)
    pygame.display.flip()
    ticks += 1

pygame.quit()