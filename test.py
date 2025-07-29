import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Floating Random-Colored Dots")
clock = pygame.time.Clock()


# Dot class
class Dot:
    def __init__(self):
        self.x = random.uniform(0, SCREEN_WIDTH)
        self.y = random.uniform(0, SCREEN_HEIGHT)
        self.radius = random.randint(2, 6)
        self.speed = random.uniform(0.1, 0.5)

        # Random direction
        angle = random.uniform(0, 2 * math.pi)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

        # Truly random color
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Wrap around screen edges
        if self.x < 0: 
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH: 
            self.x = 0
        if self.y < 0: 
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT: 
            self.y = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Create dots
NUM_DOTS = 150
dots = [Dot() for _ in range(NUM_DOTS)]

# Main loop
running = True
while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill((255, 255, 255))  # White background

    # Update and draw dots
    for dot in dots:
        dot.update()
        dot.draw(screen)

    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
