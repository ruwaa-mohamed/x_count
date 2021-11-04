# ----- Header printing ----- #
print('='*50)
print('Counting the "X" charachters per sequence from a fasta file')
print('='*50)

# ----- Importing Libraries ----- #
import argparse
import subprocess

# ----- Getting the Variables from CLI ----- #
args = None
def get_args():
	parser = argparse.ArgumentParser(
		description="A standalone Python tool that counts the number of 'X' characters per sequence in a multi-FASTA file and return the results in CSV format.",
		epilog="Ex. python x_count.py -f <path/to/file_in.fasta> -o <path/to/file_out.csv>"
	)

	# required argument
	parser.add_argument('-f', action="store", required=True, help='Input FASTA file (*.fasta)')
	parser.add_argument('-o', action="store", required=True, help='Output CSV file')

	arguments = vars(parser.parse_args())
	return arguments
	
# ----- Actual Code ----- #
def main():
	path_in = args['f']
	path_out = args['o']
	
	#n = int(int(subprocess.check_output(["wc", "-l", path_in]).split()[0])/2)
	counts_dict = dict()
	
	file_in = open(path_in)
	file_out = open(path_out, "w")
	file_out.write("#SEQID,SLen,XLen,Per\n")

	for line in file_in:
		if line.startswith('>'):
			seqid = line.rstrip()
		else:
			l = line.count("X")
			L = len(line)
			if seqid not in counts_dict.keys():
				counts_dict[seqid] = [l, L]
			else:
				counts_dict[seqid] = [counts_dict[seqid][0]+l, counts_dict[seqid][1]+L]
	for key, val in counts_dict.items():
		perc = "%2.3f" %(val[0]/val[1]*100)
		file_out.write(','.join([key, str(val[0]), str(val[1]), perc])+'\n')
		

# ----- main() ----- #
if __name__ == '__main__':
	args = get_args()
	main()
