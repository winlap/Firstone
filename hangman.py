import pygame
import random
# set up Pygame
pygame.init()

# set up the window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")
# set up the fonts
font = pygame.font.Font(None, 60)

# set up the word list
words = ['mouth', 'enormous', 'visit', 'expansion', 'sack', 'pour', 'long', 'wink', 'husband', 'sparkle', 'disappear', 'lucky', 'tranquil', 'burst', 'jazz', 'scale', 'need', 'specialist', 'offend', 'ship', 'knock', 'bridge', 'pleasure', 'distance', 'blame', 'pen', 'turkey', 'destruction', 'cheerful', 'sun', 'scandalous', 'whisper', 'hospital', 'wrap', 'doubt', 'frequent', 'button', 'yielding', 'rain', 'inquiry', 'nerve', 'fold', 'historical', 'luxuriant', 'laughable', 'meddle', 'cactus', 'minute', 'riddle', 'hysterical', 'fertile', 'guide', 'injure', 'soil', 'toad', 'maddening', 'test', 'wide-eyed', 'boil', 'scratch', 'mammoth', 'unit', 'scent', 'sincere', 'shut', 'buzz', 'marry', 'route', 'sort', 'balance', 'spark', 'enjoy', 'unknown', 'hall', 'cracker', 'middle', 'responsible', 'discovery', 'organic', 'repulsive', 'pineapple', 'tedious', 'accuse', 'unique', 'wind', 'borrow', 'attract', 'basin', 'sew', 'busy', 'motionless', 'control', 'thoughtful', 'comfort', 'faulty', 'horse', 'arm', 'ambitious', 'equal', 'supreme', 'valuable', 'nasty', 'stranger', 'sky', 'chew', 'place']

# set up the game variables
word = random.choice(words)
letters_guessed = set()
incorrect_guesses = 0
max_incorrect_guesses = 6

# set up the images
images = []
for i in range(max_incorrect_guesses + 1):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# set up the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                letter = event.unicode.lower()
                letters_guessed.add(letter)
                if letter not in word:
                    incorrect_guesses += 1

    # clear the screen
    screen.fill((255, 255, 255))

    # draw the word
    # draw the word
    text = ""
    for letter in word:
       if letter in letters_guessed:
          text += letter + " "
       else:
         text += "_ "
    word_surface = font.render(text, True, (0, 0, 0))
    screen.blit(word_surface, (50, 50))


    # draw the hangman image
    screen.blit(images[incorrect_guesses], (400, 100))

    # check for game over
    if incorrect_guesses >= max_incorrect_guesses:
        text = "Game Over"
        game_over_surface = font.render(text, True, (255, 0, 0))
        screen.blit(game_over_surface, (width // 2 - game_over_surface.get_width() // 2, height // 2 - game_over_surface.get_height() // 2))
        running = False
    elif set(word) == letters_guessed:
        text = "You Win!"
        win_surface = font.render(text, True, (0, 255, 0))
        screen.blit(win_surface, (width // 2 - win_surface.get_width() // 2, height // 2 - win_surface.get_height() // 2))
        running = False

    # update the screen
    pygame.display.flip()

# quit Pygame
pygame.quit()
