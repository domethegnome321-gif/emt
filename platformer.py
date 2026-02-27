import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
game_window = pygame.display.set_mode((800, 600))

# Colors
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (139, 69, 19)
gold = (255, 215, 0)
black = (0, 0, 0)

# Game variables
player_x = 50
player_y = 500
player_width = 50
player_height = 60
player_velocity = 5
jump = False
jump_count = 10
score = 0
lives = 3
levels = 1

# Bear properties
bears = []
for i in range(3):
    bears.append({'x': random.randint(600, 800), 'y': 500, 'width': 50, 'height': 60, 'velocity': random.randint(2, 5)})

# Coin properties
coins = [{'x': random.randint(100, 700), 'y': random.randint(100, 500)}]

# Main loop
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Player controls
    if keys[pygame.K_a] and player_x > player_velocity:
        player_x -= player_velocity
    if keys[pygame.K_d] and player_x < 800 - player_width - player_velocity:
        player_x += player_velocity
    if not jump:
        if keys[pygame.K_w]:
            jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump = False
            jump_count = 10

    # Background
    game_window.fill(green)
    pygame.draw.rect(game_window, brown, (0, 500, 800, 100))  # Ground
    for bear in bears:
        pygame.draw.rect(game_window, black, (bear['x'], bear['y'], bear['width'], bear['height']))
        bear['x'] -= bear['velocity']
        if bear['x'] < -50:
            bear['x'] = 800

    # Coins
    for coin in coins:
        pygame.draw.circle(game_window, gold, (coin['x'], coin['y']), 10)

    # Check for collisions
    for bear in bears:
        if (player_x < bear['x'] + bear['width'] and player_x + player_width > bear['x'] and player_y < bear['y'] + bear['height'] and player_y + player_height > bear['y']):
            lives -= 1
            if lives <= 0:
                running = False

    # Update score and level
    score += 1
    if score % 50 == 0:
        levels += 1
        bears.append({'x': random.randint(600, 800), 'y': 500, 'width': 50, 'height': 60, 'velocity': random.randint(2, 5)})

    # Display score and lives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, black)
    lives_text = font.render(f'Lives: {lives}', True, black)
    game_window.blit(score_text, (10, 10))
    game_window.blit(lives_text, (10, 50))

    pygame.display.update()

pygame.quit()