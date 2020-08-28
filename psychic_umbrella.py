import chess.pgn

pgn_file = "test_pgn/myblitz.pgn"

player = "bkeej"

def win(pgn):
	result = pgn.headers["Result"]
	if result == "1-0" and pgn.headers["White"] == player:
		return True
	elif result == "0-1" and pgn.headers["Black"] == player:
		return True
	else:
		return False

def draw(pgn):
	if pgn.headers["Result"] == "1/2-1/2":
		return True
	else:
		return False


with open(pgn_file) as f:
	pgn = chess.pgn.read_game(f)
	while pgn:
		if draw(pgn) == True:
			print("draw")
		elif win(pgn) == True:
			print("win")
		else:
			print("loss")
			
		pgn = chess.pgn.read_game(f)