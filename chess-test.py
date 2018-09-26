import chess
import time
import pygame

prog_name = "AI Chess Trainer"
version = "ALPHA 0.0.1"

square_start_pixel = [35, 35]
square_end_pixel = [465, 465]
square_size = [54, 54]

# board = chess.Board()

# print(board.legal_moves)
# print(board)

# ## Scholar's Mate
# scholars_mate = ["e4", "e5", "Qh5", "Nc6", "Bc4", "Nf6", "Qxf7"]

# for move in scholars_mate:
#     board.push_san(move)
#     print(board)
#     if board.is_checkmate():
#         checkmate_tag = "True"
#     else:
#         checkmate_tag = "False"
#     print("is_checkmate? :: " + checkmate_tag)
#     time.sleep(1)

def main():

    pygame.init()                                                   #Initialize a pygame
    logo = pygame.image.load("chess_title_icon.png")                #Load a logo
    pygame.display.set_icon(logo)                                   #Set icon
    pygame.display.set_caption(prog_name + "   -   " + version)     #Set program text
    screen = pygame.display.set_mode((500,500))                     #Set screensize
    bg = pygame.image.load("chess_background.jpg")                  #Load board background
    screen.blit(bg, (0,0))
    pygame.display.flip()
    running = True                                                  #Define the game as running
    while running:
        for event in pygame.event.get():                            #loop throughall the events
            if event.type == pygame.QUIT:
                running = False                                     #Stop running if the QUIT event is received
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickedPos = pygame.mouse.get_pos()
                clickedSquare = getClickedSquare(clickedPos)
                print(clickedSquare)

def getClickedPiece(clickedPos):
    print(clickedPos)

def getClickedSquare(clickedPos):#, bool isWhite):
    col = ""
    row = ""

    #Define col
    if square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 1 * square_size[0]):
        col = "a"
    elif square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 2 * square_size[0]):
        col = "b"
    elif square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 3 * square_size[0]):
        col = "c"
    elif square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 4 * square_size[0]):
        col = "d"
    elif square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 5 * square_size[0]):
        col = "e"
    elif square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 6 * square_size[0]):
        col = "f"
    elif square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 7 * square_size[0]):
        col = "g"
    elif square_start_pixel[0] < clickedPos[0] < (square_start_pixel[0] + 8 * square_size[0]):
        col = "h"
    #Define row
    if square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 1 * square_size[1]):
        row = "1"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 2 * square_size[1]):
        row = "2"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 3 * square_size[1]):
        row = "3"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 4 * square_size[1]):
        row = "4"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 5 * square_size[1]):
        row = "5"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 6 * square_size[1]):
        row = "6"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 7 * square_size[1]):
        row = "7"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 8 * square_size[1]):
        row = "8"

    if col == "":
        row = ""
    elif row == "":
        col = ""
    
    return (col+row)

if __name__=="__main__":
    main()