import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the window title
pygame.display.set_caption("Dice Roll")

# Set the font
font = pygame.font.Font(None, 36)

# Load the dice images
dice_images = [
   pygame.image.load("C:/photo/dice1.png"),
    pygame.image.load("C:/photo/dice2.png"),
    pygame.image.load("C:/photo/dice3.png"),
    pygame.image.load("C:/photo/dice4.png"),
    pygame.image.load("C:/photo/dice5.png"),
    pygame.image.load("C:/photo/dice6.png")
]

# Set the initial dice value
dice_value = random.randint(1, 6)

# Set the timer for the roll animation
ROLL_TIME = 500
roll_timer = 0

# The game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Roll the dice
                dice_value = random.randint(1, 6)
                roll_timer = pygame.time.get_ticks()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the dice image
    if roll_timer > 0:
        # If the roll animation is in progress, choose a random dice value
        elapsed_time = pygame.time.get_ticks() - roll_timer
        if elapsed_time < ROLL_TIME:
            dice_value = random.randint(1, 6)

        # Draw the dice image for the current value
        dice_image = dice_images[dice_value - 1]
        screen.blit(dice_image, (WINDOW_WIDTH / 2 - dice_image.get_width() / 2, WINDOW_HEIGHT / 2 - dice_image.get_height() / 2))
    else:
        # If the roll animation is not in progress, draw the dice image for the current value
        dice_image = dice_images[dice_value - 1]
        screen.blit(dice_image, (WINDOW_WIDTH / 2 - dice_image.get_width() / 2, WINDOW_HEIGHT / 2 - dice_image.get_height() / 2))

    # Draw the instructions
    instructions = font.render("Press SPACE to roll the dice", True, (0, 0, 0))
    instructions_rect = instructions.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    screen.blit(instructions, instructions_rect)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
