import chess
import time

board = chess.Board()

print(board.legal_moves)
print(board)

## Scholar's Mate
scholars_mate = ["e4", "e5", "Qh5", "Nc6", "Bc4", "Nf6", "Qxf7"]

for move in scholars_mate:
    board.push_san(move)
    print(board)
    if board.is_checkmate():
        checkmate_tag = "True"
    else:
        checkmate_tag = "False"
    print("is_checkmate? :: " + checkmate_tag)
    time.sleep(1)