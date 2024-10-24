import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("Interactive Story")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill((120, 200, 255))

    # Update the display
    pygame.display.flip()

pygame.quit()