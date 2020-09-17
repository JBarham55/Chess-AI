import chess

board = chess.Board()

print(board)

print(board.legal_moves)

board.push_san("Nh3")

print(board)

print(board.legal_moves)