import chess
import time
import pygame
import random
import collections
import numpy as np

prog_name = "AI Chess Trainer"
version = "ALPHA 0.0.1"

screen_size = [600, 600]

square_start_pixel = [60, 60]
square_end_pixel = [595, 590]
square_size = [60, 60] #square
square_centers = [[[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]/2]],
                  [[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[0]+square_size[0]/2, square_start_pixel[1]+square_size[1]+square_size[1]/2]],
                  [[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[1]+square_size[1]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[1]+square_size[1]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[1]+square_size[1]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[1]+square_size[1]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[1]+square_size[1]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[1]+square_size[1]/2, square_start_pixel[1]+2*square_size[1]+square_size[1]/2]],
                  [[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[1]+square_size[1]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[1]+square_size[1]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[1]+square_size[1]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[1]+square_size[1]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[1]+square_size[1]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[1]+square_size[1]/2, square_start_pixel[1]+3*square_size[1]+square_size[1]/2]],
                  [[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[1]+square_size[1]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[1]+square_size[1]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[1]+square_size[1]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[1]+square_size[1]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[1]+square_size[1]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[1]+square_size[1]/2, square_start_pixel[1]+4*square_size[1]+square_size[1]/2]],
                  [[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[1]+square_size[1]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[1]+square_size[1]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[1]+square_size[1]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[1]+square_size[1]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[1]+square_size[1]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[1]+square_size[1]/2, square_start_pixel[1]+5*square_size[1]+square_size[1]/2]],
                  [[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[1]+square_size[1]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[1]+square_size[1]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[1]+square_size[1]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[1]+square_size[1]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[1]+square_size[1]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[1]+square_size[1]/2, square_start_pixel[1]+6*square_size[1]+square_size[1]/2]],
                  [[square_start_pixel[0]+square_size[0]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2], [square_start_pixel[0]+square_size[0]+square_size[0]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2], [square_start_pixel[0]+2*square_size[1]+square_size[1]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2], [square_start_pixel[0]+3*square_size[1]+square_size[1]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2], [square_start_pixel[0]+4*square_size[1]+square_size[1]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2], [square_start_pixel[0]+5*square_size[1]+square_size[1]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2], [square_start_pixel[0]+6*square_size[1]+square_size[1]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2], [square_start_pixel[0]+7*square_size[1]+square_size[1]/2, square_start_pixel[1]+7*square_size[1]+square_size[1]/2]]]

## Scholar's Mate
scholars_mate = ["e4", "e5", "Qh5", "Nc6", "Bc4", "Nf6", "Qxf7"]

def main():

    pygame.init()                                                   #Initialize a pygame
    logo = pygame.image.load("chess_title_icon.png")                #Load a logo
    pygame.display.set_icon(logo)                                   #Set icon
    pygame.display.set_caption(prog_name + "   -   " + version)     #Set program text
    screen = pygame.display.set_mode(screen_size)                     #Set screensize
    board = chess.Board()
    drawBoard(screen, board)
    running = True                                                  #Define the game as running
    while running:
        for event in pygame.event.get():                            #loop throughall the events
            if event.type == pygame.QUIT:
                running = False                                     #Stop running if the QUIT event is received
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        init_games = []        
        for _ in range(5000):
            while not board.is_game_over():
                legal_moves = []
                for move in board.legal_moves:
                    legal_moves.append(move)
                    board.push(random.choice(legal_moves))
                    #time.sleep(.5)
                    #drawBoard(screen, board)
            init_games.append(board.result())
        running = False
        games = np.array(init_games)
        print(collections.Counter(games))
        

def drawBoard(screen, board):
    drawImage(screen, "chess-board-background.png", 0, 0, 180)
    for square in range(64):
        row = chess.square_rank(square)
        col = chess.square_file(square)
        piece = board.piece_at(square)
        if piece == chess.Piece(chess.PAWN, chess.WHITE):
            drawImage(screen, "chess_pieces\Chess_plt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a white pawn at the square
        elif piece == chess.Piece(chess.KNIGHT, chess.WHITE):
            drawImage(screen, "chess_pieces\Chess_nlt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a white knight at the square
        elif piece == chess.Piece(chess.BISHOP, chess.WHITE):
            drawImage(screen, "chess_pieces\Chess_blt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a white bishop at the square
        elif piece == chess.Piece(chess.ROOK, chess.WHITE):
            drawImage(screen, "chess_pieces\Chess_rlt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a white rooke at the square
        elif piece == chess.Piece(chess.QUEEN, chess.WHITE):
            drawImage(screen, "chess_pieces\Chess_qlt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a white queen at the square
        elif piece == chess.Piece(chess.KING, chess.WHITE):
            drawImage(screen, "chess_pieces\Chess_klt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a white king at the square
        elif piece == chess.Piece(chess.PAWN, chess.BLACK):
            drawImage(screen, "chess_pieces\Chess_pdt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a black pawn at the square
        elif piece == chess.Piece(chess.KNIGHT, chess.BLACK):
            drawImage(screen, "chess_pieces\Chess_ndt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a black knight at the square
        elif piece == chess.Piece(chess.BISHOP, chess.BLACK):
            drawImage(screen, "chess_pieces\Chess_bdt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a black bishop at the square
        elif piece == chess.Piece(chess.ROOK, chess.BLACK):
            drawImage(screen, "chess_pieces\Chess_rdt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a black rooke at the square
        elif piece == chess.Piece(chess.QUEEN, chess.BLACK):
            drawImage(screen, "chess_pieces\Chess_qdt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a black queen at the square
        elif piece == chess.Piece(chess.KING, chess.BLACK):
            drawImage(screen, "chess_pieces\Chess_kdt60.png", square_start_pixel[0]+col*square_size[0], square_start_pixel[1]+row*square_size[1], 0) #draw a black king at the square        print(board.piece_at(square))
        
def drawImage(screen, filename, xpos, ypos, rot):
    img = pygame.image.load(filename)                  #Load board background
    if rot != 0:
        img = pygame.transform.rotate(img, rot)
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
    
    return ([col,row])

if __name__=="__main__":
    main()