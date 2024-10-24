import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 72)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(BLACK)

    # Render some text
    text = font.render("Once upon a time...", False, WHITE)
    screen.blit(text, (1, 2))

    # Update the display
    pygame.display.flip()

pygame.quit()