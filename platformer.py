import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Placeholder for bird shape
        self.image.fill((255, 255, 255))  # White background for testing
        self.rect = self.image.get_rect(center=(100, 100))
        self.wing_state = 0
        self.is_jumping = False
        self.gravity = 0.5
        self.velocity_y = 0

    def update(self):
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            if self.rect.y > 300:  # Ground level
                self.rect.y = 300
                self.is_jumping = False
                self.velocity_y = 0

        self.animate_wings()

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -15  # Jump strength
            self.is_jumping = True

    def animate_wings(self):
        if self.is_jumping or self.rect.y < 300:
            self.wing_state = (self.wing_state + 1) % 3  # Simple wing animation
            if self.wing_state == 1:
                self.image.fill((255, 255, 0))  # Yellow for wing down
            elif self.wing_state == 2:
                self.image.fill((255, 0, 0))  # Red for wing up
            else:
                self.image.fill((255, 255, 255))  # Back to bird body color

    def draw(self, screen):
        screen.blit(self.image, self.rect)
