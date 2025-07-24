import pygame
import sys
import time
from pygame.locals import *

# initialize pygame
pygame.init()

# board characteristics
width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None] * 3, [None] * 3, [None] * 3]

# builds the display
pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((width, height + 100), 0, 32)
screen.fill(white)

# load and scale images
x_img = pygame.image.load(
    r"C:\Users\gchin\OneDrive\Documents\Python_MissionBit\tic_tac_toe\assets\tictactoe_X.jpg"
)
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.image.load(
    r"C:\Users\gchin\OneDrive\Documents\Python_MissionBit\tic_tac_toe\assets\tictactoe_O.png"
)
o_img = pygame.transform.scale(o_img, (80, 80))

# game state
letter = "X"
winner = None
tie = None
CLOCK = pygame.time.Clock()
fps = 30

# draw grid
def draw_grid():
    screen.fill(white)
    # vertical lines
    pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    # horizontal lines
    pygame.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pygame.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)



# display status
def tie_status():
    font = pygame.font.Font(None, 30)
    # endgame messages
    if winner is None:
        message = f"{letter}'s Turn"
    else:
        message = f"{winner} won!"
    if tie:
        message = "Draw game!"
    # text display area
    text = font.render(message, True, (50, 50, 50))
    screen.fill(white, (0, height, width, 100))
    text_rect = text.get_rect(center=(width / 2, height + 50))
    screen.blit(text, text_rect)
    pygame.display.update()


# draw letter
def draw_letter(row, col):
    global board
    cell_size = width // 3
    offset = (cell_size - 80) // 2
    posx = (col - 1) * cell_size + offset
    posy = (row - 1) * cell_size + offset

    if letter == 'X':
        screen.blit(x_img, (posx, posy))
        board[row - 1][col - 1] = 'X'
    else:
        screen.blit(o_img, (posx, posy))
        board[row - 1][col - 1] = 'O'

    pygame.display.update()

# check for win
# displays line that shows win scenario
def check_win():
    global winner, tie

    # horizontal check
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            pygame.draw.line(
                screen,
                (250, 0, 0),
                (0, (row + 1) * height / 3 - height / 6),
                (width, (row + 1) * height / 3 - height / 6),
                4,
            )
            time.sleep(1)
            return

    # column check
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            pygame.draw.line(
                screen,
                (250, 0, 0),
                ((col + 1) * width / 3 - width / 6, 0),
                ((col + 1) * width / 3 - width / 6, height),
                4,
            )
            time.sleep(1)
            return

    # diagnol checks
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        pygame.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
        return 

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        pygame.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
        return 

    # check if every cell is filled
    if all([all(i) for i in board]) and winner is None:
        # all(i) checks if all items in row are full
        # all([...]) then checks if all rows are full
        tie = True


# handle clicks
def user_click():
    global letter, winner, tie

    x, y = pygame.mouse.get_pos()
    if y > height:  # Ignore clicks below the grid
        return

    col = int(x // (width / 3)) + 1
    row = int(y // (height / 3)) + 1

    if row <= 3 and col <= 3 and board[row - 1][col - 1] is None:
        draw_letter(row, col)
        check_win()
        if not winner and not tie:
            letter = 'O' if letter == 'X' else 'X'
        tie_status()


# restart
def reset_game():
    global board, winner, letter, tie
    board = [[None] * 3, [None] * 3, [None] * 3]
    winner = None
    tie = False
    letter = "X"
    draw_grid()
    tie_status()


# start game
draw_grid()
tie_status()

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is pygame.MOUSEBUTTONDOWN:
            user_click()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_r:
                reset_game()

    pygame.display.update()
