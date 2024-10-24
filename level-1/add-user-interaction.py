import pygame
import time

pygame.init()

# Set up the display
screen = pygame.display.set_mode((1900, 1000))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Story state
scene = 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scene = 1
            elif event.key == pygame.K_2:
                scene = 2
            elif event.key == pygame.K_3:
                scene = 3
            elif event.key == pygame.K_4:
                scene = 4


    # Fill the screen with white
    screen.fill(WHITE)

    # Render text based on the scene
    if scene == 1:
        text = font.render("You are in a forest... Click 2 to go to a castle. Click 3 to go into a hatch.", True, BLACK)
    elif scene == 2:
        text = font.render("You are in a castle... Click 1 to go back to the forest. Click 4 to go into complete darkness.", True, BLACK)
    elif scene == 3:
        text = font.render("You go into the hatch... You are dead. Click 1 to restart the game.", True, BLACK)
    elif scene == 4:
        text = font.render("You go into complete darkness... You are suddenly dragged int eternal abyss.", True, BLACK)
        screen.blit(text, (50, 50))
        pygame.display.flip()
        time.sleep(3) # Sleep for 3 seconds
        running = False

    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()