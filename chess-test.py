import chess
import time
import pygame

prog_name = "AI Chess Trainer"
version = "ALPHA 0.0.1"

screen_size = [650, 645]

square_start_pixel = [50, 50]
square_end_pixel = [600, 600]
square_size = 69 #square
square_centers = [[[square_start_pixel[0]+square_size/2, square_start_pixel[1]+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+square_size/2]],
                  [[square_start_pixel[0]+square_size/2, square_start_pixel[1]+square_size+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+square_size+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+square_size+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+square_size+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+square_size+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+square_size+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+square_size+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+square_size+square_size/2]],
                  [[square_start_pixel[0]+square_size/2, square_start_pixel[1]+2*square_size+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+2*square_size+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+2*square_size+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+2*square_size+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+2*square_size+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+2*square_size+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+2*square_size+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+2*square_size+square_size/2]],
                  [[square_start_pixel[0]+square_size/2, square_start_pixel[1]+3*square_size+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+3*square_size+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+3*square_size+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+3*square_size+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+3*square_size+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+3*square_size+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+3*square_size+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+3*square_size+square_size/2]],
                  [[square_start_pixel[0]+square_size/2, square_start_pixel[1]+4*square_size+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+4*square_size+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+4*square_size+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+4*square_size+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+4*square_size+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+4*square_size+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+4*square_size+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+4*square_size+square_size/2]],
                  [[square_start_pixel[0]+square_size/2, square_start_pixel[1]+5*square_size+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+5*square_size+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+5*square_size+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+5*square_size+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+5*square_size+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+5*square_size+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+5*square_size+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+5*square_size+square_size/2]],
                  [[square_start_pixel[0]+square_size/2, square_start_pixel[1]+6*square_size+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+6*square_size+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+6*square_size+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+6*square_size+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+6*square_size+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+6*square_size+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+6*square_size+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+6*square_size+square_size/2]],
                  [[square_start_pixel[0]+square_size/2, square_start_pixel[1]+7*square_size+square_size/2], [square_start_pixel[0]+square_size+square_size/2, square_start_pixel[1]+7*square_size+square_size/2], [square_start_pixel[0]+2*square_size+square_size/2, square_start_pixel[1]+7*square_size+square_size/2], [square_start_pixel[0]+3*square_size+square_size/2, square_start_pixel[1]+7*square_size+square_size/2], [square_start_pixel[0]+4*square_size+square_size/2, square_start_pixel[1]+7*square_size+square_size/2], [square_start_pixel[0]+5*square_size+square_size/2, square_start_pixel[1]+7*square_size+square_size/2], [square_start_pixel[0]+6*square_size+square_size/2, square_start_pixel[1]+7*square_size+square_size/2], [square_start_pixel[0]+7*square_size+square_size/2, square_start_pixel[1]+7*square_size+square_size/2]]]

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
    screen = pygame.display.set_mode(screen_size)                     #Set screensize
    drawBoard(screen)
    running = True                                                  #Define the game as running
    while running:
        for event in pygame.event.get():                            #loop throughall the events
            if event.type == pygame.QUIT:
                running = False                                     #Stop running if the QUIT event is received

def drawBoard(screen):#board):
    drawImage(screen, "chess_background_w.jpg", 0, 0)
    for row in square_centers:
        for col in row:
            drawImage(screen, "chess_pieces\Chess_plt60.png", col[0]-30, col[1]-30) #draw a white pawn everywhere

def drawImage(screen, filename, xpos, ypos):
    img = pygame.image.load(filename)                  #Load board background
    screen.blit(img, (xpos,ypos))
    pygame.display.flip()

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
        row = "8"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 2 * square_size[1]):
        row = "7"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 3 * square_size[1]):
        row = "6"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 4 * square_size[1]):
        row = "5"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 5 * square_size[1]):
        row = "4"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 6 * square_size[1]):
        row = "3"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 7 * square_size[1]):
        row = "2"
    elif square_start_pixel[1] < clickedPos[1] < (square_start_pixel[1] + 8 * square_size[1]):
        row = "1"

    if col == "":
        row = ""
    elif row == "":
        col = ""
    
    return (col+row)

if __name__=="__main__":
    main()