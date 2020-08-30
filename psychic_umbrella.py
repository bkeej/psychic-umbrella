import chess.pgn
import pandas as pd

pgn_file = 'test_pgn/myblitz.pgn'

player = 'bkeej'

def win(pgn):
	result = pgn.headers['Result']
	if pgn.headers['Result'] == '1/2-1/2':
		return 'draw'
	elif result == '1-0' and pgn.headers['White'] == player:
		return 'win'
	elif result == '0-1' and pgn.headers['Black'] == player:
		return 'win'
	else:
		return 'loss'

def elo(pgn):
	if pgn.headers['White'] == player:
		return pgn.headers['WhiteElo']
	elif pgn.headers['Black'] == player:
		return pgn.headers['BlackElo']

df = pd.DataFrame(columns=['Date','Result','Rating','TimeControl'])

with open(pgn_file) as f:
	pgn = chess.pgn.read_game(f)
	while pgn:
		row = {'Date':pgn.headers['Date'], 'Result':win(pgn), 'Rating':elo(pgn), 'TimeControl':pgn.headers['TimeControl']}
		df = df.append(row, ignore_index=True)
		pgn = chess.pgn.read_game(f)

print(df)