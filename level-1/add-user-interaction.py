import pygame
import time

pygame.init()

# Set up the display
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Attack of the brown thing.")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
cyan = (0, 3, 3)

wallet = 0
inventory = []

file_name = "1.jpg"

def prepare_backround(file_name):
    backround_image = pygame.image.load(file_name)
    backround_image = pygame.transform.scale(backround_image, [screen_width, screen_height])
    screen.blit(backround_image, (0, 0))

def render_text(lines):
    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (50, 50 + y_offset))
        y_offset += font.get_linesize()

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
                file_name = "1.jpg"
            elif event.key == pygame.K_2:
                scene = 2
                file_name = "2.jpg"
            elif event.key == pygame.K_3:
                scene = 3 
                file_name = "3.jpeg"
            elif event.key == pygame.K_4:
                scene = 4
                file_name = "5.jpeg"
            elif event.key == pygame.K_m:
                scene = 98
                file_name = "4.jpg"
            elif event.key == pygame.K_e:
                scene = 100
            elif event.key == pygame.K_w:
                scene = 99  
            elif event.key == pygame.K_a:
                if "Plunger" not in inventory and wallet > 0:
                    inventory.append("Plunger")
                    wallet -= 15
                else:
                    print("no more plungers.")
            elif event.key == pygame.K_c:
                if "AK74U" not in inventory and wallet > 0:
                    inventory.append("AK74U")
                    wallet -= 520
                else:
                    print("Nuh uh...")
            elif event.key == pygame.K_b:
                if "Banana" not in inventory and wallet > 0:
                    inventory.append("Banana")
                    wallet -= 2
                else:
                    print("You have enough.")
            elif event.key == pygame.K_UP:
                wallet += 10000
            elif event.key == pygame.K_d:
                if "Glock 19X" not in inventory and wallet > 0:
                    inventory.append("Glock 19X")
                    wallet -= 320
                else:
                    print("Nuh uh...")

    prepare_backround(file_name)

    # Render text based on the scene
    if scene == 1:
        lines = [
            "You are in a forest...",
            "",
            "Click 2 to go to a castle.",
            "",
            "Click 3 to go into a hatch.",
            "",
            "Click M to go to the Market.",
        ]
    elif scene == 2:
        lines = [
            "You are in a castle...",
            "",
            "Click 1 to go back to the forest.",
            "",
            "Click 4 to go into complete darkness.",
        ]
    elif scene == 3:
        lines = [
            "You go into the hatch...",
            "",
            "You are dead. Click 1 to restart the game.",
        ]
    elif scene == 4:
        lines = [
            "You go into complete darkness...",
            "",
            "You are suddenly dragged into eternal abyss.",
        ]
    elif scene == 98:
        lines = [
            "Hello! Welcome to the Shop.", 
            "Check the list below.", 
            "Press A to add Plunger to inventory",
            "Press B to add Bananas to inventory.",
            "Press C to add AK74U to inventory.",
            "Press D to add Glock 19X to inventory.",
            ]
    elif scene == 99:
        lines = ["Wallet:", "£"+str(wallet)]
    elif scene == 100:
        lines = [
            "Guess what you have in your invenny bro"
        ]
        lines = lines + inventory
    
    render_text(lines)

    # Update the display
    pygame.display.flip()

pygame.quit()