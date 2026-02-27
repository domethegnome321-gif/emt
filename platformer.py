import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500
        self.vel_y = 0
        self.vel_x = 0
        self.gravity = 0.6
        self.jumping = False
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        if keys[pygame.K_RIGHT]:
            self.vel_x = 5
        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = -15
            self.jumping = True
        
        self.vel_y += self.gravity
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Simple ground collision
        if self.rect.y >= 550:
            self.rect.y = 550
            self.vel_y = 0
            self.jumping = False

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    screen.fill((135, 206, 235))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()