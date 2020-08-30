import chess.pgn
import pandas as pd

pgn_file = 'test_pgn/myblitz.pgn'

player = 'bkeej'

time = '180+2'

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
		return pgn.headers['BlackElo']
	elif pgn.headers['Black'] == player:
		return pgn.headers['WhiteElo']

def tc(time,df):
	indexNames = df[df['TimeControl'] != time].index
	df.drop(indexNames, inplace=True)
	return df

def performance(df):
	winIndex = df[df['Result'] == 'win'].index
	lossIndex = df[df['Result'] == 'loss'].index
	drawIndex = df[df['Result'] == 'draw'].index
	df['Performance'] = df.loc[drawIndex]['Opponent Rating']
	df.loc[winIndex,'Performance'] = df.loc[winIndex]['Opponent Rating'] + 400
	df.loc[lossIndex,'Performance'] = df.loc[lossIndex]['Opponent Rating'] - 400
	return df
	# print(lossIndex)
	# print(drawIndex)

def average_performace(df):
	tc(time,df)
	df['Opponent Rating'] = df['Opponent Rating'].astype(int)
	performance(df)
	df.sort_values(by='Date', ascending=False, inplace=True)

	# print(df.head(10))

	print('\n', player+"'s", 'performance Ratings for', time, '\n', '-------------------------------------\n')
	print('Overall:', df['Performance'].mean(), '\n')
	print('Last 300:', df.head(300)['Performance'].mean(), '\n')
	print('Last 100:', df.head(100)['Performance'].mean(), '\n')
	print('Last 50:', df.head(50)['Performance'].mean(), '\n')
	print('Last 25:', df.head(25)['Performance'].mean(), '\n')
	print('Last 10:', df.head(10)['Performance'].mean(), '\n')

def parse_pgn(file):
	df = pd.DataFrame(columns=['Date','Result','Opponent Rating','TimeControl'])

	with open(pgn_file) as f:
		pgn = chess.pgn.read_game(f)
		while pgn:
			row = {'Date':pgn.headers['Date'], 'Result':win(pgn), 'Opponent Rating':elo(pgn), 'TimeControl':pgn.headers['TimeControl']}
			df = df.append(row, ignore_index=True)
			pgn = chess.pgn.read_game(f)
	return df

def main():
	df = parse_pgn(pgn_file)
	average_performace(df)

if __name__ == '__main__':
	main() 
