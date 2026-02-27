import pygame

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sulka Onglema')

# Colors
SKY_BLUE = (135, 206, 235)
ORANGE = (255, 165, 0)
DARK_BROWN = (101, 67, 33)
GOLD = (255, 215, 0)

# Load assets
bird_image = pygame.Surface((50, 50))  # Placeholder for bird image
bird_image.fill(ORANGE)

bear_image = pygame.Surface((50, 50))  # Placeholder for bear image
bear_image.fill(DARK_BROWN)

coin_image = pygame.Surface((30, 30))  # Placeholder for coin image
coin_image.fill(GOLD)

# Game variables
score = 0
level = 1
lives = 3

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move up
        pass
    if keys[pygame.K_s]:  # Move down
        pass
    if keys[pygame.K_a]:  # Move left
        pass
    if keys[pygame.K_d]:  # Move right
        pass

    # Update game state
    # Drawing code
    window.fill(SKY_BLUE)  # Set the sky blue background
    # Draw the bird, bears, coins, etc.

    # Display score and lives
    pygame.display.flip()

pygame.quit()