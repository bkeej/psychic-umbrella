import chess.pgn

pgn_file = "test_pgn/myblitz.pgn"

player = "bkeej"

with open(pgn_file) as f:
	pgn = chess.pgn.read_game(f)
	while pgn:
		print(pgn)
		pgn = chess.pgn.read_game(f)