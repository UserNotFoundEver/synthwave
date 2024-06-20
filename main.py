import pygame
from synth import Synth

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SynthWave")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
KEY_COLORS = [
    (255, 87, 51), (255, 189, 51), (219, 255, 51), (117, 255, 51),
    (51, 255, 87), (51, 255, 189), (51, 219, 255), (51, 117, 255),
    (87, 51, 255), (189, 51, 255), (255, 51, 219), (255, 51, 117),
    (255, 87, 51), (255, 189, 51), (219, 255, 51), (117, 255, 51)
]

# Create Synth object
synth = Synth()

# Define key positions
keys = []
key_width = WIDTH // 16
key_height = HEIGHT // 2

for i in range(16):
    key_rect = pygame.Rect(i * key_width, HEIGHT // 2, key_width, key_height)
    keys.append((key_rect, KEY_COLORS[i]))

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, (key_rect, color) in enumerate(keys):
                if key_rect.collidepoint(event.pos):
                    synth.play(i)
        elif event.type == pygame.MOUSEBUTTONUP:
            synth.stop()

    # Draw everything
    win.fill(BLACK)
    for key_rect, color in keys:
        pygame.draw.rect(win, color, key_rect)
    
    pygame.display.flip()

pygame.quit()
