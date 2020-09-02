import performance as per
import argparse

pgn_file = 'test_pgn/myblitz.pgn'

player = 'bkeej'

time = '180+2'

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument('infile', type=argparse.FileType('r'), help="A pgn file")
parser.add_argument(dest='player', type=str, help="The player whose performance to track.")
parser.add_argument(dest='time', type=str, help="The time control, e.g., 180+2.")



# Parse and print the results
args = parser.parse_args()
# print(args.infile)
# print(args.player)
# print(args.time)


def main():
	df = per.parse_pgn(args.infile,args.player)
	per.average_performace(df,args.player,args.time)

if __name__ == '__main__':
	main() 
